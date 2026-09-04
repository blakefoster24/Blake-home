import os
import sys
import subprocess
import zipfile
import urllib.request
import json
import yaml
import shutil
from datetime import datetime


# --- CONFIGURATION ---

CONFIG_DIR = "/config"
BACKUP_DIR = os.path.join(CONFIG_DIR, "ha_info")
ZIP_FILE = os.path.join(CONFIG_DIR, "www", "ha_ai_context.zip")

SUPERVISOR_TOKEN = os.environ.get("SUPERVISOR_TOKEN")
HEADERS = {
    "Authorization": f"Bearer {SUPERVISOR_TOKEN}"
}

CUSTOM_ICONS_DIR = "/config/custom_icons"


# --- FUNCTIONS ---


def backup_yaml_file(filename):
    """Copies a core YAML file directly into the backup directory."""

    src = os.path.join(CONFIG_DIR, filename)
    dest = os.path.join(BACKUP_DIR, filename)

    if os.path.exists(src):
        with open(src, "r", encoding="utf-8") as f_in, \
                open(dest, "w", encoding="utf-8") as f_out:
            f_out.write(f_in.read())

    return dest


def backup_manager_script():
    """
    Copies this backup manager script into the ha_info folder.

    This allows the current Python backup manager to be included
    in both the GitHub backup and the downloadable AI context ZIP.
    """

    src = os.path.join(
        CONFIG_DIR,
        "ha_backup_manager.py"
    )

    dest = os.path.join(
        BACKUP_DIR,
        "ha_backup_manager.py"
    )

    print("Backing up ha_backup_manager.py...")

    if not os.path.exists(src):
        print(
            "ha_backup_manager.py not found "
            "at /config/ha_backup_manager.py"
        )
        return None

    try:
        shutil.copy2(
            src,
            dest
        )

        print(
            "Successfully copied "
            "ha_backup_manager.py into ha_info."
        )

        return dest

    except Exception as e:
        print(
            f"Error backing up "
            f"ha_backup_manager.py: {e}"
        )
        return None


def backup_notes_folder():
    """
    Copies the Notes folder into the ha_info directory,
    handling case-sensitivity.
    """

    print("Backing up notes folder...")

    src = None

    for possible_name in [
        "Notes",
        "notes"
    ]:
        candidate = os.path.join(
            CONFIG_DIR,
            possible_name
        )

        if (
            os.path.exists(candidate)
            and os.path.isdir(candidate)
        ):
            src = candidate
            break

    if not src:
        print(
            "Notes folder not found in /config/ "
            "(checked 'Notes' and 'notes')."
        )
        return None

    dest = os.path.join(
        BACKUP_DIR,
        "notes"
    )

    try:
        if os.path.exists(dest):
            shutil.rmtree(dest)

        shutil.copytree(
            src,
            dest
        )

        print(
            f"Successfully backed up notes "
            f"from {src} to {dest}"
        )

        return dest

    except Exception as e:
        print(
            f"Error copying notes folder: {e}"
        )
        return None


def get_log_data(
    log_name,
    line_count=1000,
    grep_filter=None
):
    """
    Fetches logs from Supervisor API and returns them
    as a formatted string.
    """

    url = "http://supervisor/core/logs"

    print(
        f"Fetching {log_name}..."
    )

    try:
        req = urllib.request.Request(
            url,
            headers=HEADERS
        )

        with urllib.request.urlopen(
            req
        ) as response:

            data = (
                response
                .read()
                .decode("utf-8")
                .splitlines()
            )

            if grep_filter:
                data = [
                    line
                    for line in data
                    if any(
                        x in line.lower()
                        for x in grep_filter
                    )
                ]

            data = data[-line_count:]

            header = (
                f"\n\n{'=' * 40}\n"
                f"LOG: {log_name}\n"
                f"{'=' * 40}\n"
                f"===== "
                f"{datetime.now().isoformat()} "
                f"=====\n"
            )

            return (
                header
                + "\n".join(data)
                + "\n"
            )

    except Exception as e:
        return (
            f"\n\n{'=' * 40}\n"
            f"LOG: {log_name}\n"
            f"{'=' * 40}\n"
            f"[Error fetching "
            f"{log_name}: {e}]\n"
        )


def compile_icons_to_json():
    """
    Reads all SVG files and saves them
    as a single JSON object.
    """

    print(
        "Compiling icons to JSON..."
    )

    output_path = os.path.join(
        BACKUP_DIR,
        "custom_icons.json"
    )

    icons_data = {}

    if os.path.exists(
        CUSTOM_ICONS_DIR
    ):

        for root, dirs, files in os.walk(
            CUSTOM_ICONS_DIR
        ):

            for file in sorted(files):

                if file.endswith(
                    ".svg"
                ):

                    full_path = os.path.join(
                        root,
                        file
                    )

                    rel_path = os.path.relpath(
                        full_path,
                        CUSTOM_ICONS_DIR
                    )

                    try:
                        with open(
                            full_path,
                            "r",
                            encoding="utf-8"
                        ) as icon_file:

                            icons_data[
                                rel_path
                            ] = (
                                icon_file
                                .read()
                                .strip()
                            )

                    except Exception as e:
                        print(
                            f"Error reading "
                            f"{file}: {e}"
                        )

    try:
        with open(
            output_path,
            "w",
            encoding="utf-8"
        ) as json_file:

            json.dump(
                icons_data,
                json_file,
                indent=2
            )

    except Exception as e:
        print(
            f"Error saving JSON: {e}"
        )


def get_dashboard_files():
    """
    Dynamically finds all dashboard files to merge.
    """

    files = []

    base_files = [
        "/config/.storage/lovelace",
        "/config/.storage/lovelace_dashboards"
    ]

    for f in base_files:

        if os.path.exists(f):
            files.append(f)

    lovelace_dir = (
        "/config/.storage"
    )

    if os.path.exists(
        lovelace_dir
    ):

        for file in os.listdir(
            lovelace_dir
        ):

            if file.startswith(
                "lovelace."
            ):

                full_path = os.path.join(
                    lovelace_dir,
                    file
                )

                if full_path not in files:
                    files.append(
                        full_path
                    )

    return files


def merge_dashboards_to_yaml(
    output_filename,
    source_files
):
    """
    Converts Lovelace JSON dashboards to YAML
    and merges them.
    """

    print(
        f"Converting dashboards to YAML "
        f"and merging into "
        f"{output_filename}..."
    )

    output_path = os.path.join(
        BACKUP_DIR,
        output_filename
    )

    with open(
        output_path,
        "w",
        encoding="utf-8"
    ) as outfile:

        for fname in source_files:

            if os.path.exists(
                fname
            ):

                try:
                    with open(
                        fname,
                        "r",
                        encoding="utf-8"
                    ) as infile:

                        data = json.load(
                            infile
                        )

                        outfile.write(
                            f"\n\n"
                            f"{'#' * 40}\n"
                        )

                        outfile.write(
                            f"# DASHBOARD: "
                            f"{os.path.basename(fname)}\n"
                        )

                        outfile.write(
                            f"{'#' * 40}\n"
                        )

                        if (
                            "data" in data
                            and
                            "config"
                            in data["data"]
                        ):

                            config_data = (
                                data[
                                    "data"
                                ][
                                    "config"
                                ]
                            )

                            yaml_str = (
                                yaml.dump(
                                    config_data,
                                    default_flow_style=False,
                                    sort_keys=False,
                                    allow_unicode=True
                                )
                            )

                            outfile.write(
                                yaml_str
                            )

                        else:

                            yaml_str = (
                                yaml.dump(
                                    data,
                                    default_flow_style=False,
                                    sort_keys=False,
                                    allow_unicode=True
                                )
                            )

                            outfile.write(
                                yaml_str
                            )

                except Exception as e:

                    outfile.write(
                        f"\n"
                        f"# [Error processing "
                        f"{fname}: {e}]\n"
                    )

            else:
                print(
                    f"Skipping missing file: "
                    f"{fname}"
                )

    return output_path


def run_git():
    """
    Runs Git add, commit, and push.

    Only the ha_info directory is staged.

    Any failure is printed and raised so Home Assistant
    receives a non-zero return code instead of silently
    treating the backup as successful.
    """

    print(
        "Running Git commands..."
    )

    commands = [
        (
            "git config "
            "user.name 'Home Assistant'"
        ),

        (
            "git config "
            "user.email 'ha@local'"
        ),

        (
            "git -c "
            "credential.helper="
            "'store --file=/config/.git-credentials' "
            "add -A -- ha_info"
        ),

        (
            "git diff --cached --quiet || "
            f"git commit -m "
            f"'Auto commit "
            f"{datetime.now().isoformat()}'"
        ),

        (
            "git -c "
            "credential.helper="
            "'store --file=/config/.git-credentials' "
            "push origin main"
        )
    ]

    for cmd in commands:

        print(
            "\n"
            "----------------------------------------"
        )

        print(
            f"$ {cmd}"
        )

        print(
            "----------------------------------------"
        )

        result = subprocess.run(
            cmd,
            cwd=CONFIG_DIR,
            shell=True,
            text=True,
            capture_output=True
        )

        if result.stdout:
            print(
                "STDOUT:"
            )

            print(
                result.stdout
            )

        if result.stderr:
            print(
                "STDERR:"
            )

            print(
                result.stderr
            )

        print(
            f"Return code: "
            f"{result.returncode}"
        )

        if result.returncode != 0:

            raise RuntimeError(
                "\n"
                "Git command failed.\n"
                f"Command: {cmd}\n"
                f"Return code: "
                f"{result.returncode}\n"
                f"STDOUT:\n"
                f"{result.stdout}\n"
                f"STDERR:\n"
                f"{result.stderr}"
            )

    print(
        "\n"
        "Git push completed successfully."
    )


def create_zip(
    files_to_zip
):
    """
    Zips collected files and directories,
    preserving relative paths.
    """

    print(
        "Creating Zip file..."
    )

    if os.path.exists(
        ZIP_FILE
    ):

        try:
            os.remove(
                ZIP_FILE
            )

        except OSError:
            pass

    with zipfile.ZipFile(
        ZIP_FILE,
        "w",
        zipfile.ZIP_DEFLATED
    ) as z:

        for f in files_to_zip:

            if not f:
                continue

            if os.path.exists(
                f
            ):

                if os.path.isdir(
                    f
                ):

                    for (
                        root,
                        dirs,
                        files
                    ) in os.walk(f):

                        for file in files:

                            full_path = (
                                os.path.join(
                                    root,
                                    file
                                )
                            )

                            arcname = (
                                os.path.relpath(
                                    full_path,
                                    BACKUP_DIR
                                )
                            )
                                
                            if (
                                arcname.startswith("notes" + os.sep)
                                and not os.path.splitext(file)[1]
                            ):
                                arcname += ".txt"

                            z.write(
                                full_path,
                                arcname
                            )

                else:

                    if f.startswith(
                        BACKUP_DIR
                    ):

                        arcname = (
                            os.path.relpath(
                                f,
                                BACKUP_DIR
                            )
                        )

                    else:

                        arcname = (
                            os.path.basename(
                                f
                            )
                        )

                    z.write(
                        f,
                        arcname
                    )

    print(
        f"Zip created successfully: "
        f"{ZIP_FILE}"
    )


# --- MAIN EXECUTION ---


if __name__ == "__main__":

    os.makedirs(
        BACKUP_DIR,
        exist_ok=True
    )

    # -------------------------------------------------
    # 1. Fetch logs directly into full_logs.txt
    # -------------------------------------------------

    merged_logs_path = (
        os.path.join(
            BACKUP_DIR,
            "full_logs.txt"
        )
    )

    print(
        "Generating full_logs.txt..."
    )

    with open(
        merged_logs_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            get_log_data(
                "last_log.txt",
                1000
            )
        )

        f.write(
            get_log_data(
                "automation_runs.txt",
                5000,
                grep_filter=[
                    "automation",
                    "triggered",
                    "script",
                    "scene.turn",
                    "light.turn"
                ]
            )
        )

        f.write(
            get_log_data(
                "error_log.txt",
                500,
                grep_filter=[
                    "error",
                    "warning",
                    "fatal"
                ]
            )
        )

    # -------------------------------------------------
    # 2. Compile custom icons
    # -------------------------------------------------

    compile_icons_to_json()

    # -------------------------------------------------
    # 3. Process dashboards, YAML files, Notes,
    #    and backup this Python manager itself.
    # -------------------------------------------------

    merged_dashboards = (
        merge_dashboards_to_yaml(
            "full_dashboards.yaml",
            get_dashboard_files()
        )
    )

    config_yaml = (
        backup_yaml_file(
            "configuration.yaml"
        )
    )

    automations_yaml = (
        backup_yaml_file(
            "automations.yaml"
        )
    )

    scripts_yaml = (
        backup_yaml_file(
            "scripts.yaml"
        )
    )

    scenes_yaml = (
        backup_yaml_file(
            "scenes.yaml"
        )
    )

    notes_dir = (
        backup_notes_folder()
    )

    backup_manager = (
        backup_manager_script()
    )

    # -------------------------------------------------
    # 4. Define final ZIP contents
    # -------------------------------------------------

    final_zip_list = [
        config_yaml,
        automations_yaml,
        scripts_yaml,
        scenes_yaml,
        merged_logs_path,
        merged_dashboards,
        os.path.join(
            BACKUP_DIR,
            "custom_icons.json"
        ),
        os.path.join(
            BACKUP_DIR,
            "HA_Overview.md"
        )
    ]

    if backup_manager:
        final_zip_list.append(
            backup_manager
        )

    if notes_dir:
        final_zip_list.append(
            notes_dir
        )

    # -------------------------------------------------
    # 5. Git push
    #
    # If Git fails, remember the error but continue
    # so the AI/download ZIP is still created.
    # -------------------------------------------------

    git_error = None

    try:
        run_git()

    except Exception as e:

        git_error = str(e)

        print(
            "\n"
            "========================================\n"
            "GIT PUSH FAILED\n"
            "========================================",
            file=sys.stderr
        )

        print(
            git_error,
            file=sys.stderr
        )

    # -------------------------------------------------
    # 6. Create downloadable ZIP regardless of Git
    # success/failure.
    # -------------------------------------------------

    try:
        create_zip(
            final_zip_list
        )

    except Exception as e:

        print(
            "\n"
            "========================================\n"
            "ZIP CREATION FAILED\n"
            "========================================",
            file=sys.stderr
        )

        print(
            str(e),
            file=sys.stderr
        )

        sys.exit(2)

    # -------------------------------------------------
    # 7. Return Git failure to Home Assistant only
    # AFTER the downloadable ZIP has been created.
    # -------------------------------------------------

    if git_error:

        print(
            "\n"
            "The local AI context ZIP was created, "
            "but the GitHub push failed.",
            file=sys.stderr
        )

        sys.exit(1)

    print(
        "\n"
        "========================================\n"
        "BACKUP COMPLETED SUCCESSFULLY\n"
        "========================================"
    )

    print(
        "GitHub push succeeded and "
        "the AI context ZIP was created."
    )

    sys.exit(0)