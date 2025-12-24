_Last Updated: 2025-12-24T02:00:00.313288-06:00_

## 🛠 UI Helpers
Below are the input helpers configured in Home Assistant.





### Boolean
| Entity ID | Name | State | Attributes |
|---|---|---|---|



| `input_boolean.disable_toggle` | **Disable toggle ** | off |  |



| `input_boolean.phone_active` | **Phone active** | off |  |



| `input_boolean.workday_today_toggle` | **Workday Today Toggle** | on |  |



| `input_boolean.workday_toggle_helper` | **General Toggle Helper** | off |  |



| `input_boolean.workday_tomorrow_toggle` | **Workday Tomorrow Toggle** | on |  |









### Datetime
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  

| `input_datetime.home_timestamp` | **Home Timestamp** | 2025-12-23 18:24:52 | has_date=True, has_time=True |



  

| `input_datetime.last_door_open` | **Last Door Open** | 2025-12-23 18:33:28 | has_date=True, has_time=True |



  

| `input_datetime.scheduled_off` | **Scheduled Off** | 1969-12-31 | has_date=True, has_time=False |



  

| `input_datetime.working_override` | **Working Override** | 1969-12-31 | has_date=True, has_time=False |















### Counter
| Entity ID | Name | State | Attributes |
|---|---|---|---|



   

| `counter.counter_helper` | **Counter helper** | 0 | min=0, max=20 |



   

| `counter.door_stuck` | **Door Stuck** | 9 | min=0, max=1000 |



   

| `counter.motion_anomaly` | **Motion anomaly** | 1 | min=, max= |






### Timer
| Entity ID | Name | State | Attributes |
|---|---|---|---|



   

| `timer.timer_helper` | **Timer Helper** | idle | duration=0:00:15 |








---

## 🏠 All Entities (By Domain)


<details><summary><b>Automation (14)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `automation.battery_low_automation` | Battery Low Automation | on |

| `automation.bedroom_ceiling_lights_3_set_my_room` | Bedroom Ceiling Lights (3) -> Set My Room | on |

| `automation.door_automation` | Door Automation | on |

| `automation.flic_butttons` | Flic Button | on |

| `automation.goodnight` | Goodnight | on |

| `automation.helper_automation` | Helper Automation | on |

| `automation.hue_dimmer` | Hue Dimmer | on |

| `automation.light_triggers_another_light` | Light Triggers another Light | on |

| `automation.living_room_lamp` | Living Room Lamp | on |

| `automation.living_room_tv_ghost_buster` | Living Room TV Ghost Buster | on |

| `automation.nightly_github_sync` | Nightly GitHub sync | on |

| `automation.thermostat` | Thermostat | on |

| `automation.work_schedule_automations` | Work Schedule Automations | on |

| `automation.workday_wake_up` | Workday Wake-up | on |

</details>




<details><summary><b>Binary_sensor (58)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `binary_sensor.50_onn_roku_tv_headphones_connected` | Bedroom TV Headphones connected | off |

| `binary_sensor.50_onn_roku_tv_supports_airplay` | Bedroom TV Supports AirPlay | on |

| `binary_sensor.50_onn_roku_tv_supports_ethernet` | Bedroom TV Supports Ethernet | on |

| `binary_sensor.50_onn_roku_tv_supports_find_remote` | Bedroom TV Supports find remote | on |

| `binary_sensor.apartment_presence` | Apartment Presence | on |

| `binary_sensor.bathroom_light_cloud_connection` | Bathroom Light Cloud connection | on |

| `binary_sensor.bathroom_light_overheated` | Bathroom Light Overheated | off |

| `binary_sensor.bed_presence_bb8594_bed_occupied_both` | Bed Presence Sensor Bed Occupied Both | off |

| `binary_sensor.bed_presence_bb8594_bed_occupied_either` | Bed Presence Sensor Bed Occupied Either | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left` | Bed Presence Sensor Bed Occupied Left | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left_fast` | Bed Presence Sensor Bed Occupied Left (Fast) | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left_normal` | Bed Presence Sensor Bed Occupied Left (Normal) | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_right` | Bed Presence Sensor Bed Occupied Right | off |

| `binary_sensor.bed_presence_bb8594_status` | Bed Presence Sensor Status | on |

| `binary_sensor.bedroom_presence` | Everything Presence Lite Occupancy | on |

| `binary_sensor.blake_s_echo_dot_connectivity` | Blake's Echo Dot Connectivity | on |

| `binary_sensor.blake_s_echo_pop_connectivity` | Blake's Echo Pop Connectivity | on |

| `binary_sensor.closet_light_cloud_connection` | Closet Light Cloud connection | on |

| `binary_sensor.closet_light_overheated` | Closet Light Overheated | off |

| `binary_sensor.everything_presence_lite_922d28_target_1_active` | Everything Presence Lite Target 1 Active | on |

| `binary_sensor.everything_presence_lite_922d28_target_2_active` | Everything Presence Lite Target 2 Active | off |

| `binary_sensor.everything_presence_lite_922d28_target_3_active` | Everything Presence Lite Target 3 Active | off |

| `binary_sensor.everything_presence_lite_922d28_zone_1_occupancy` | Everything Presence Lite Zone 1 Occupancy | on |

| `binary_sensor.everything_presence_lite_922d28_zone_2_occupancy` | Everything Presence Lite Zone 2 Occupancy | off |

| `binary_sensor.everything_presence_lite_922d28_zone_3_occupancy` | Everything Presence Lite Zone 3 Occupancy | off |

| `binary_sensor.everything_presence_lite_922d28_zone_4_occupancy` | Everything Presence Lite Zone 4 Occupancy | off |

| `binary_sensor.everywhere_connectivity` | Everywhere Connectivity | on |

| `binary_sensor.fan_outlet_cloud_connection` | Fan Outlet Cloud connection | on |

| `binary_sensor.front_door` | Front door | off |

| `binary_sensor.kitchen_lights_cloud_connection` | Kitchen Lights Cloud connection | on |

| `binary_sensor.kitchen_lights_overheated` | Kitchen Lights Overheated | off |

| `binary_sensor.kitchen_presence` | Aqara FP300 Presence | off |

| `binary_sensor.living_room_ceiling_fan_cloud_connection` | Living Room Ceiling Fan Cloud connection | on |

| `binary_sensor.living_room_ceiling_fan_overheated` | Living Room Ceiling Fan Overheated | off |

| `binary_sensor.living_room_ceiling_lights_cloud_connection` | Living Room Ceiling Lights Cloud connection | on |

| `binary_sensor.living_room_ceiling_lights_overheated` | Living Room Ceiling Lights Overheated | off |

| `binary_sensor.main_lights_cloud_connection` | Main Lights Cloud connection | on |

| `binary_sensor.motion_1_motion` | Motion 1 | on |

| `binary_sensor.philips_rwl020_binary_input` | Hue Dimmer Binary input | off |

| `binary_sensor.phone_browser` | phone browser | unavailable |

| `binary_sensor.phone_browser_browser_dark_mode` | phone browser Browser dark mode | unavailable |

| `binary_sensor.phone_browser_browser_fullykiosk` | phone browser Browser FullyKiosk | unavailable |

| `binary_sensor.remote_ui` | Remote UI | on |

| `binary_sensor.shelly_ceiling_fan_overcurrent` | Bedroom Ceiling Fan Overcurrent | off |

| `binary_sensor.shelly_ceiling_fan_overheating` | Bedroom Ceiling Fan Overheating | off |

| `binary_sensor.shelly_ceiling_fan_overpowering` | Bedroom Ceiling Fan Overpowering | off |

| `binary_sensor.shelly_ceiling_fan_overvoltage` | Bedroom Ceiling Fan Overvoltage | off |

| `binary_sensor.shelly_ceiling_lights_overcurrent` | Bedroom Ceiling Lights Overcurrent | off |

| `binary_sensor.shelly_ceiling_lights_overheating` | Bedroom Ceiling Lights Overheating | off |

| `binary_sensor.shelly_ceiling_lights_overpowering` | Bedroom Ceiling Lights Overpowering | off |

| `binary_sensor.shelly_ceiling_lights_overvoltage` | Bedroom Ceiling Lights Overvoltage | off |

| `binary_sensor.shellyplus2pm_3c8a1fe82824_cloud` | Shelly Device Cloud | off |

| `binary_sensor.slzb_mr1_ethernet` | SLZB-MR1 Ethernet | off |

| `binary_sensor.slzb_mr1_internet` | SLZB-MR1 Internet | on |

| `binary_sensor.space_heater_cloud_connection` | Space Heater Cloud connection | unavailable |

| `binary_sensor.space_heater_overheated` | Space Heater Overheated | unavailable |

| `binary_sensor.space_heater_overloaded` | Space Heater Overloaded | unavailable |

| `binary_sensor.workday_tomorrow_template_sensor` | Workday Tomorrow Template Sensor | off |

</details>




<details><summary><b>Button (19)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `button.aqara_fp300_identify` | Aqara FP300 Identify | unknown |

| `button.aqara_fp300_restart_device` | Aqara FP300 Restart device | unknown |

| `button.aqara_fp300_start_spatial_learning` | Aqara FP300 Start spatial learning | 2025-12-15T04:11:25.804002+00:00 |

| `button.aqara_fp300_start_target_distance_tracking` | Aqara FP300 Start target distance tracking | 2025-12-15T04:09:48.237866+00:00 |

| `button.bed_presence_bb8594_calibrate_left_occupied` | Bed Presence Sensor Calibrate Left Occupied | 2025-12-02T05:21:48.234043+00:00 |

| `button.bed_presence_bb8594_calibrate_left_unoccupied` | Bed Presence Sensor Calibrate Left Unoccupied | 2025-12-02T05:29:13.586934+00:00 |

| `button.bed_presence_bb8594_calibrate_right_occupied` | Bed Presence Sensor Calibrate Right Occupied | 2025-12-09T01:13:45.583631+00:00 |

| `button.bed_presence_bb8594_calibrate_right_unoccupied` | Bed Presence Sensor Calibrate Right Unoccupied | 2025-12-09T01:13:31.413415+00:00 |

| `button.bed_presence_bb8594_restart` | Bed Presence Sensor Restart | unknown |

| `button.bedroom_lamp_identify` | Bedroom Lamp Identify | 2025-12-08T08:30:05.569038+00:00 |

| `button.everything_presence_lite_922d28_esp_reboot` | Everything Presence Lite ESP Reboot | unknown |

| `button.everything_presence_lite_922d28_factory_reset_mmwave_sensor` | Everything Presence Lite Factory Reset mmWave Sensor | unknown |

| `button.everything_presence_lite_922d28_reboot_mmwave_sensor` | Everything Presence Lite Reboot mmWave Sensor | unknown |

| `button.living_room_lamp_identify` | Living Room Lamp Identify | 2025-12-12T05:16:53.886398+00:00 |

| `button.nest_thermostat_identify` | Nest Thermostat Identify | unknown |

| `button.philips_rwl020_identify` | Hue Dimmer Identify | unknown |

| `button.shelly_device_reboot` | Shelly Device Restart | unknown |

| `button.slzb_mr1_core_restart` | SLZB-MR1 Core restart | unknown |

| `button.slzb_mr1_zigbee_restart` | SLZB-MR1 Zigbee restart | unknown |

</details>




<details><summary><b>Climate (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `climate.nest_thermostat` | Nest Thermostat | heat |

</details>




<details><summary><b>Conversation (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `conversation.home_assistant` | Home Assistant | unknown |

</details>






<details><summary><b>Device_tracker (11)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `device_tracker.blakes_apple_watch` | Blake’s Apple Watch | home |

| `device_tracker.blakes_iphone` | Blakes iPhone | home |

| `device_tracker.blakes_iphone_2` | Blakes iPhone | home |

| `device_tracker.ipad` | iPad | home |

| `device_tracker.rachels_phone` | Rachels Phone | not_home |

| `device_tracker.rivian_phone_key_2060` | Rivian Phone Key 2060 | home |

| `device_tracker.s58cdfccea0786690c_d4a2` | S58cdfccea0786690C D4A2 | not_home |

| `device_tracker.scd0ed4bcbf3abdf0c_652d` | scd0ed4bcbf3abdf0c 652d | unavailable |

| `device_tracker.sd78d075d9fbca645c_788d` | sd78d075d9fbca645c 788d | unavailable |

| `device_tracker.sdf631c51986d49cdc_295e` | Sdf631c51986d49cdC 295E | not_home |

| `device_tracker.xkglowrgb_0451` | xkglowrgb 0451 | unavailable |

</details>




<details><summary><b>Event (3)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `event.backup_automatic_backup` | Backup Automatic backup | 2025-12-23T10:54:24.173+00:00 |

| `event.bthome_sensor_3370_button` | Motion 1 Button | 2025-10-19T05:15:17.292+00:00 |

| `event.front_door_sensor_button` | Front Door Sensor Button | 2025-12-14T04:27:51.375+00:00 |

</details>




<details><summary><b>Fan (3)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `fan.bedroom_ceiling_fan` | Bedroom Ceiling Fan | off |

| `fan.bedroom_fan` | Fan | on |

| `fan.living_room_ceiling_fan` | Living Room Ceiling Fan | off |

</details>








<details><summary><b>Light (10)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `light.bathroom_light` | Bathroom Light | off |

| `light.bedroom_ceiling_lights` | Bedroom Ceiling Lights | off |

| `light.bedroom_lamp` | Bedroom Lamp | off |

| `light.closet_light` | Closet Light | off |

| `light.everything_presence_lite_922d28_esp32_led` | Everything Presence Lite ESP32 LED | off |

| `light.kitchen_lights` | Kitchen Lights | off |

| `light.living_room_ceiling_lights` | Living Room Ceiling Lights | off |

| `light.living_room_lamp` | Living Room Lamp | on |

| `light.main_lights` | Main Lights | off |

| `light.phone_browser_screen` | phone browser Screen | unavailable |

</details>




<details><summary><b>Media_player (6)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `media_player.bedroom_tv` | Bedroom Tv | off |

| `media_player.blake_s_echo_dot` | Blake's Echo Dot | paused |

| `media_player.blake_s_echo_pop` | Blake's Echo Pop | paused |

| `media_player.everywhere` | Everywhere | paused |

| `media_player.living_room_tv` | Living Room TV | unavailable |

| `media_player.phone_browser` | phone browser | unavailable |

</details>




<details><summary><b>Notify (5)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `notify.blake_s_echo_dot_announce` | Blake's Echo Dot Announce | unknown |

| `notify.blake_s_echo_dot_speak` | Blake's Echo Dot Speak | unknown |

| `notify.blake_s_echo_pop_announce` | Blake's Echo Pop Announce | unknown |

| `notify.blake_s_echo_pop_speak` | Blake's Echo Pop Speak | unknown |

| `notify.everywhere_announce` | Everywhere Announce | unknown |

</details>




<details><summary><b>Number (56)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `number.aqara_fp300_absence_delay_timer` | Aqara FP300 Absence delay timer | 10 |

| `number.aqara_fp300_humidity_reporting_interval` | Aqara FP300 Humidity reporting interval | 3600.0 |

| `number.aqara_fp300_humidity_reporting_threshold` | Aqara FP300 Humidity reporting threshold | 15.0 |

| `number.aqara_fp300_light_reporting_interval` | Aqara FP300 Light reporting interval | 3600.0 |

| `number.aqara_fp300_light_reporting_threshold` | Aqara FP300 Light reporting threshold | 10.0 |

| `number.aqara_fp300_light_sampling_period` | Aqara FP300 Light sampling period | 120.0 |

| `number.aqara_fp300_pir_detection_interval` | Aqara FP300 PIR detection interval | 15 |

| `number.aqara_fp300_temp_humidity_sampling_period` | Aqara FP300 Temp & humidity sampling period | 600.0 |

| `number.aqara_fp300_temperature_reporting_interval` | Aqara FP300 Temperature reporting interval | 3600.0 |

| `number.aqara_fp300_temperature_reporting_threshold` | Aqara FP300 Temperature reporting threshold | 0.5 |

| `number.bathroom_light_turn_off_in` | Bathroom Light Turn off in | 120 |

| `number.bed_presence_bb8594_left_occupied_pressure` | Bed Presence Sensor Left Occupied Pressure | 95.96 |

| `number.bed_presence_bb8594_left_trigger_pressure` | Bed Presence Sensor Left Trigger Pressure | 91.6 |

| `number.bed_presence_bb8594_left_unoccupied_pressure` | Bed Presence Sensor Left Unoccupied Pressure | 78.5 |

| `number.bed_presence_bb8594_right_occupied_pressure` | Bed Presence Sensor Right Occupied Pressure | 93.68 |

| `number.bed_presence_bb8594_right_trigger_pressure` | Bed Presence Sensor Right Trigger Pressure | 90.21 |

| `number.bed_presence_bb8594_right_unoccupied_pressure` | Bed Presence Sensor Right Unoccupied Pressure | 79.8 |

| `number.bedroom_lamp_start_up_color_temperature` | Bedroom Lamp Start-up color temperature | 366 |

| `number.bedroom_lamp_start_up_current_level` | Bedroom Lamp Start-up current level | 255 |

| `number.closet_light_turn_off_in` | Closet Light Turn off in | 120 |

| `number.everything_presence_lite_922d28_illuminance_offset` | Everything Presence Lite Illuminance Offset | 0.0 |

| `number.everything_presence_lite_922d28_installation_angle` | Everything Presence Lite Installation Angle | 0.0 |

| `number.everything_presence_lite_922d28_max_distance` | Everything Presence Lite Max Distance | 600.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_begin_x` | Everything Presence Lite Occupancy Mask 1 Begin X | -6000.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_begin_y` | Everything Presence Lite Occupancy Mask 1 Begin Y | -1560.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_end_x` | Everything Presence Lite Occupancy Mask 1 End X | -6000.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_end_y` | Everything Presence Lite Occupancy Mask 1 End Y | -1560.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_begin_x` | Everything Presence Lite Occupancy Mask 2 Begin X | -6000.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_begin_y` | Everything Presence Lite Occupancy Mask 2 Begin Y | -1560.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_end_x` | Everything Presence Lite Occupancy Mask 2 End X | -6000.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_end_y` | Everything Presence Lite Occupancy Mask 2 End Y | -1560.0 |

| `number.everything_presence_lite_922d28_occupancy_off_delay` | Everything Presence Lite Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_stale_target_reset_timeout` | Everything Presence Lite Stale Target Reset Timeout | 3.0 |

| `number.everything_presence_lite_922d28_zone_1_begin_x` | Everything Presence Lite Zone 1 Begin X | -4000.0 |

| `number.everything_presence_lite_922d28_zone_1_begin_y` | Everything Presence Lite Zone 1 Begin Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_1_end_x` | Everything Presence Lite Zone 1 End X | 4000.0 |

| `number.everything_presence_lite_922d28_zone_1_end_y` | Everything Presence Lite Zone 1 End Y | 6000.0 |

| `number.everything_presence_lite_922d28_zone_1_occupancy_off_delay` | Everything Presence Lite Zone 1 Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_zone_2_begin_x` | Everything Presence Lite Zone 2 Begin X | -6000.0 |

| `number.everything_presence_lite_922d28_zone_2_begin_y` | Everything Presence Lite Zone 2 Begin Y | -1560.0 |

| `number.everything_presence_lite_922d28_zone_2_end_x` | Everything Presence Lite Zone 2 End X | -6000.0 |

| `number.everything_presence_lite_922d28_zone_2_end_y` | Everything Presence Lite Zone 2 End Y | -1560.0 |

| `number.everything_presence_lite_922d28_zone_2_occupancy_off_delay` | Everything Presence Lite Zone 2 Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_zone_3_begin_x` | Everything Presence Lite Zone 3 Begin X | -6000.0 |

| `number.everything_presence_lite_922d28_zone_3_begin_y` | Everything Presence Lite Zone 3 Begin Y | -1560.0 |

| `number.everything_presence_lite_922d28_zone_3_end_x` | Everything Presence Lite Zone 3 End X | -6000.0 |

| `number.everything_presence_lite_922d28_zone_4_begin_x` | Everything Presence Lite Zone 4 Begin X | -6000.0 |

| `number.everything_presence_lite_922d28_zone_4_end_x` | Everything Presence Lite Zone 4 End X | -6000.0 |

| `number.everything_presence_lite_922d28_zone_4_occupancy_off_delay` | Everything Presence Lite Zone 4 Occupancy Off Delay | 15.0 |

| `number.kitchen_lights_turn_off_in` | Kitchen Lights Turn off in | 120 |

| `number.living_room_ceiling_fan_turn_off_in` | Living Room Ceiling Fan Turn off in | 120 |

| `number.living_room_ceiling_lights_turn_off_in` | Living Room Ceiling Lights Turn off in | 120 |

| `number.living_room_lamp_start_up_current_level` | Living Room Lamp Start-up current level | 254 |

| `number.main_lights_turn_off_in` | Main Lights Turn off in | 120 |

| `number.space_heater_power_protection` | Space Heater Power protection | unavailable |

| `number.space_heater_turn_off_in` | Space Heater Turn off in | unavailable |

</details>




<details><summary><b>Person (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `person.blake_foster` | Blake Foster | home |

| `person.rachel` | Rachel | not_home |

</details>




<details><summary><b>Remote (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `remote.bedroom_tv` | Bedroom Tv Remote | off |

</details>




<details><summary><b>Scene (14)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `scene.all_lights` | All Lights | 2025-12-24T00:33:28.503230+00:00 |

| `scene.all_lights_off` | All Lights Off | 2025-12-14T00:08:33.465716+00:00 |

| `scene.all_off` | All Off | 2025-12-23T15:08:19.421517+00:00 |

| `scene.bedroom_lights_off` | Bedroom Lights Off | 2025-12-23T06:12:23.133030+00:00 |

| `scene.dimmed` | Dimmed | 2025-12-14T20:06:22.380333+00:00 |

| `scene.full_lamp` | Full Lamp | 2025-12-24T00:33:29.221010+00:00 |

| `scene.goodnight_scene` | Goodnight | 2025-12-24T05:30:37.127988+00:00 |

| `scene.im_awake` | I’m Awake | 2025-12-02T12:31:03.745110+00:00 |

| `scene.lamp_snapshot` | lamp_snapshot | 2025-12-24T03:20:31.491563+00:00 |

| `scene.night_light` | Night Light | 2025-09-26T00:17:04.739409+00:00 |

| `scene.set_my_room` | Set My Room | 2025-12-24T02:27:45.286774+00:00 |

| `scene.temp_thermostat_snapshot` | temp_thermostat_snapshot | 2025-12-22T14:02:12.711937+00:00 |

| `scene.thermostat_away` | Thermostat Away | 2025-12-23T19:41:26.065313+00:00 |

| `scene.thermostat_ideal_evening` | Thermostat 68/70 | 2025-11-28T11:14:37.942932+00:00 |

</details>




<details><summary><b>Script (6)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `script.alarm_music_script` | Alarm Music Script | off |

| `script.create_push_ha_info_to_github_gemini_zip` | Create & Push HA Info to GitHub & Gemini Zip | on |

| `script.find_my_phone` | Find My Phone | off |

| `script.find_remote` | Find Remote | off |

| `script.set_date_to_today` | Scheduled Off & Working Override dashboard script | off |

| `script.temporary_thermostat_adjustment` | Temporary Thermostat Adjustment | off |

</details>




<details><summary><b>Select (14)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `select.aqara_fp300_humidity_reporting_mode` | Aqara FP300 Humidity reporting mode | THRESHOLD AND INTERVAL |

| `select.aqara_fp300_light_reporting_mode` | Aqara FP300 Light reporting mode | THRESHOLD AND INTERVAL |

| `select.aqara_fp300_light_sampling` | Aqara FP300 Light sampling | CUSTOM |

| `select.aqara_fp300_motion_sensitivity` | Aqara FP300 Motion sensitivity | HIGH |

| `select.aqara_fp300_presence_detection_options` | Aqara FP300 Presence detection options | BOTH |

| `select.aqara_fp300_temp_humidity_sampling` | Aqara FP300 Temp & humidity sampling | OFF |

| `select.aqara_fp300_temperature_reporting_mode` | Aqara FP300 Temperature reporting mode | THRESHOLD AND INTERVAL |

| `select.bed_presence_bb8594_bluetooth_scanner_mode` | Bed Presence Sensor Bluetooth Scanner Mode | Passive |

| `select.bed_presence_bb8594_response_speed` | Bed Presence Sensor Response Speed | Slow |

| `select.bedroom_lamp_start_up_behavior` | Bedroom Lamp Start-up behavior | PreviousValue |

| `select.everything_presence_lite_922d28_extra_entities_update` | Everything Presence Lite Extra entities update | Every update |

| `select.everything_presence_lite_922d28_tracking_behaviour` | Everything Presence Lite Tracking Behaviour | Above + Speed and Resolution |

| `select.everything_presence_lite_922d28_update_speed` | Everything Presence Lite Update speed | Normal (0.3s) |

| `select.living_room_lamp_start_up_behavior` | Living Room Lamp Start-up behavior | PreviousValue |

</details>




<details><summary><b>Sensor (167)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `sensor.50_onn_roku_tv_active_app` | Bedroom TV Active app | unknown |

| `sensor.50_onn_roku_tv_active_app_id` | Bedroom TV Active app ID | unknown |

| `sensor.aqara_fp300_battery` | Aqara FP300 Battery | 100.0 |

| `sensor.aqara_fp300_humidity` | Aqara FP300 Humidity | 39.0 |

| `sensor.aqara_fp300_illuminance` | Aqara FP300 Illuminance | 0 |

| `sensor.aqara_fp300_target_distance` | Aqara FP300 Target distance | unknown |

| `sensor.aqara_fp300_temperature` | Aqara FP300 Temperature | 70.448 |

| `sensor.backup_backup_manager_state` | Backup Backup Manager state | idle |

| `sensor.backup_last_attempted_automatic_backup` | Backup Last attempted automatic backup | 2025-12-23T10:53:02+00:00 |

| `sensor.backup_last_successful_automatic_backup` | Backup Last successful automatic backup | 2025-12-23T10:54:23+00:00 |

| `sensor.backup_next_scheduled_automatic_backup` | Backup Next scheduled automatic backup | 2025-12-24T10:56:03+00:00 |

| `sensor.bathroom_light_auto_off_at` | Bathroom Light Auto-off at | unknown |

| `sensor.bathroom_light_signal_level` | Bathroom Light Signal level | 3 |

| `sensor.bed_presence_bb8594_left_pressure` | Bed Presence Sensor Left Pressure | 96.0543441772461 |

| `sensor.bed_presence_bb8594_right_pressure` | Bed Presence Sensor Right Pressure | 90.1773834228516 |

| `sensor.bed_presence_bb8594_uptime` | Bed Presence Sensor Uptime | 1181936.25 |

| `sensor.bed_presence_bb8594_wifi_signal_db` | Bed Presence Sensor WiFi Signal dB | -48.0 |

| `sensor.bed_presence_bb8594_wifi_signal_percent` | Bed Presence Sensor WiFi Signal Percent | 100.0 |

| `sensor.bedroom_ceiling_fan_energy_consumed` | Bedroom Ceiling Fan Energy consumed | 6.848384 |

| `sensor.blake_foster30_gmail_com_vacation_end_date` | blake.foster30@gmail.com Vacation end date | unknown |

| `sensor.blake_s_echo_dot_illuminance` | Illuminance | unavailable |

| `sensor.blake_s_echo_dot_next_alarm` | Blake's Echo Dot next Alarm | unknown |

| `sensor.blake_s_echo_dot_next_alarm_2` | Blake's Echo Dot Next alarm | unavailable |

| `sensor.blake_s_echo_dot_next_reminder` | Blake's Echo Dot next Reminder | unknown |

| `sensor.blake_s_echo_dot_next_reminder_2` | Blake's Echo Dot Next reminder | unavailable |

| `sensor.blake_s_echo_dot_next_timer` | Blake's Echo Dot next Timer | unknown |

| `sensor.blake_s_echo_dot_next_timer_2` | Blake's Echo Dot Next timer | unavailable |

| `sensor.blake_s_echo_pop_next_alarm` | Blake's Echo Pop next Alarm | unknown |

| `sensor.blake_s_echo_pop_next_alarm_2` | Blake's Echo Pop Next alarm | unavailable |

| `sensor.blake_s_echo_pop_next_reminder` | Blake's Echo Pop next Reminder | unknown |

| `sensor.blake_s_echo_pop_next_reminder_2` | Blake's Echo Pop Next reminder | unavailable |

| `sensor.blake_s_echo_pop_next_timer` | Blake's Echo Pop next Timer | unknown |

| `sensor.blake_s_echo_pop_next_timer_2` | Blake's Echo Pop Next timer | unavailable |

| `sensor.blakes_apple_watch_battery` | Blake’s Apple Watch Battery | 99 |

| `sensor.blakes_iphone_app_version` | Blakes iPhone App Version | 2025.12.1 |

| `sensor.blakes_iphone_battery` | Blakes iPhone Battery | 100 |

| `sensor.blakes_iphone_battery_level` | Blakes iPhone Battery Level | 80 |

| `sensor.blakes_iphone_battery_state` | Blakes iPhone Battery State | Charging |

| `sensor.blakes_iphone_geocoded_location` | Blakes iPhone Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.blakes_iphone_ssid` | Blakes iPhone SSID | ATTEPISyDS |

| `sensor.bthome_sensor_3370_battery` | Motion 1 Battery | 100 |

| `sensor.bthome_sensor_3370_illuminance` | Motion 1 Illuminance | 36.0 |

| `sensor.bthome_sensor_3370_packet_id` | Motion 1 Packet Id | 102 |

| `sensor.bthome_sensor_3370_signal_strength` | Motion 1 Signal Strength | -56 |

| `sensor.closet_light_auto_off_at` | Closet Light Auto-off at | unknown |

| `sensor.closet_light_signal_level` | Closet Light Signal level | 3 |

| `sensor.everything_presence_lite_922d28_illuminance` | Everything Presence Lite Illuminance | 0.0 |

| `sensor.everything_presence_lite_922d28_mmwave_firmware` | Everything Presence Lite mmWave Firmware | V2.04 |

| `sensor.everything_presence_lite_922d28_occupancy_mask_1_target_count` | Everything Presence Lite Occupancy Mask 1 Target Count | 0.0 |

| `sensor.everything_presence_lite_922d28_occupancy_mask_2_target_count` | Everything Presence Lite Occupancy Mask 2 Target Count | 0.0 |

| `sensor.everything_presence_lite_922d28_target_1_angle` | Everything Presence Lite Target 1 Angle | -54.9764747619629 |

| `sensor.everything_presence_lite_922d28_target_1_distance` | Everything Presence Lite Target 1 Distance | 11.7304992675781 |

| `sensor.everything_presence_lite_922d28_target_1_resolution` | Everything Presence Lite Target 1 Resolution | 14.1732283464567 |

| `sensor.everything_presence_lite_922d28_target_1_speed` | Everything Presence Lite Target 1 Speed | 0.0 |

| `sensor.everything_presence_lite_922d28_target_1_x` | Everything Presence Lite Target 1 X | 9.60629921259843 |

| `sensor.everything_presence_lite_922d28_target_1_y` | Everything Presence Lite Target 1 Y | 6.73228346456693 |

| `sensor.everything_presence_lite_922d28_target_2_angle` | Everything Presence Lite Target 2 Angle | 0.0 |

| `sensor.everything_presence_lite_922d28_target_2_distance` | Everything Presence Lite Target 2 Distance | 0.0 |

| `sensor.everything_presence_lite_922d28_target_2_resolution` | Everything Presence Lite Target 2 Resolution | 0.0 |

| `sensor.everything_presence_lite_922d28_target_2_speed` | Everything Presence Lite Target 2 Speed | 0.0 |

| `sensor.everything_presence_lite_922d28_target_2_x` | Everything Presence Lite Target 2 X | 0.0 |

| `sensor.everything_presence_lite_922d28_target_2_y` | Everything Presence Lite Target 2 Y | 0.0 |

| `sensor.everything_presence_lite_922d28_target_3_angle` | Everything Presence Lite Target 3 Angle | 0.0 |

| `sensor.everything_presence_lite_922d28_target_3_distance` | Everything Presence Lite Target 3 Distance | 0.0 |

| `sensor.everything_presence_lite_922d28_target_3_resolution` | Everything Presence Lite Target 3 Resolution | 0.0 |

| `sensor.everything_presence_lite_922d28_target_3_speed` | Everything Presence Lite Target 3 Speed | 0.0 |

| `sensor.everything_presence_lite_922d28_target_3_x` | Everything Presence Lite Target 3 X | 0.0 |

| `sensor.everything_presence_lite_922d28_target_3_y` | Everything Presence Lite Target 3 Y | 0.0 |

| `sensor.everything_presence_lite_922d28_zone_2_target_count` | Everything Presence Lite Zone 2 Target Count | 0.0 |

| `sensor.everything_presence_lite_922d28_zone_3_target_count` | Everything Presence Lite Zone 3 Target Count | 0.0 |

| `sensor.everything_presence_lite_922d28_zone_4_target_count` | Everything Presence Lite Zone 4 Target Count | 0.0 |

| `sensor.everything_presence_lite_zone_1_target_count` | Everything Presence Lite Zone 1 Target Count | 1.0 |

| `sensor.everywhere_next_alarm` | Everywhere Next alarm | unavailable |

| `sensor.everywhere_next_reminder` | Everywhere Next reminder | unavailable |

| `sensor.everywhere_next_timer` | Everywhere Next timer | unavailable |

| `sensor.front_door_sensor_battery` | Front Door Sensor Battery | 90 |

| `sensor.front_door_sensor_illuminance` | Front Door Sensor Illuminance | 18.0 |

| `sensor.front_door_sensor_rotation` | Front Door Sensor Rotation | 0.0 |

| `sensor.ipad_app_version` | iPad App Version | 2025.12.1 |

| `sensor.ipad_battery_level` | iPad Battery Level | 5 |

| `sensor.ipad_battery_state` | iPad Battery State | Charging |

| `sensor.ipad_geocoded_location` | iPad Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.ipad_ssid` | iPad SSID | ATTEPISyDS |

| `sensor.kitchen_lights_auto_off_at` | Kitchen Lights Auto-off at | unknown |

| `sensor.kitchen_lights_signal_level` | Kitchen Lights Signal level | 3 |

| `sensor.living_room_ceiling_fan_auto_off_at` | Living Room Ceiling Fan Auto-off at | unknown |

| `sensor.living_room_ceiling_fan_signal_level` | Living Room Ceiling Fan Signal level | 3 |

| `sensor.living_room_ceiling_lights_auto_off_at` | Living Room Ceiling Lights Auto-off at | unknown |

| `sensor.living_room_ceiling_lights_signal_level` | Living Room Ceiling Lights Signal level | 3 |

| `sensor.main_lights_auto_off_at` | Main Lights Auto-off at | unknown |

| `sensor.main_lights_current` | Main Lights Current | 0.0 |

| `sensor.main_lights_current_consumption` | Main Lights Current consumption | 0.0 |

| `sensor.main_lights_signal_level` | Main Lights Signal level | 3 |

| `sensor.main_lights_this_month_s_consumption` | Main Lights This month's consumption | 3.522 |

| `sensor.main_lights_today_s_consumption` | Main Lights Today's consumption | 0.0 |

| `sensor.main_lights_voltage` | Main Lights Voltage | 124.4 |

| `sensor.nest_thermostat_temperature` | Nest Thermostat Temperature | 70.682 |

| `sensor.openweathermap_cloud_coverage_2` | OpenWeatherMap Cloud coverage | 100 |

| `sensor.openweathermap_condition_2` | OpenWeatherMap Condition | cloudy |

| `sensor.openweathermap_dew_point_2` | OpenWeatherMap Dew point temperature | 46.058 |

| `sensor.openweathermap_feels_like_temperature_2` | OpenWeatherMap Apparent temperature | 47.696 |

| `sensor.openweathermap_humidity_2` | OpenWeatherMap Humidity | 94 |

| `sensor.openweathermap_precipitation_kind_2` | OpenWeatherMap Precipitation kind | None |

| `sensor.openweathermap_pressure_2` | OpenWeatherMap Pressure | 14.8518649750818 |

| `sensor.openweathermap_rain_2` | OpenWeatherMap Rain intensity | 0.0 |

| `sensor.openweathermap_snow_2` | OpenWeatherMap Snow intensity | 0.0 |

| `sensor.openweathermap_temperature_2` | OpenWeatherMap Temperature | 47.696 |

| `sensor.openweathermap_uv_index_2` | OpenWeatherMap UV index | 0 |

| `sensor.openweathermap_visibility_2` | OpenWeatherMap Visibility | 32808.3989501312 |

| `sensor.openweathermap_weather_2` | OpenWeatherMap Weather | overcast clouds |

| `sensor.openweathermap_weather_code_2` | OpenWeatherMap Weather code | 804 |

| `sensor.openweathermap_wind_bearing_2` | OpenWeatherMap Wind direction | 70 |

| `sensor.openweathermap_wind_gust_2` | OpenWeatherMap Wind gust speed | 2.9974946313529 |

| `sensor.openweathermap_wind_speed_2` | OpenWeatherMap Wind speed | 1.99087329992842 |

| `sensor.philips_rwl020_battery` | Hue Dimmer Battery | 100.0 |

| `sensor.phone_browser_browser_height` | phone browser Browser height | unavailable |

| `sensor.phone_browser_browser_id` | phone browser Browser ID | unavailable |

| `sensor.phone_browser_browser_path` | phone browser Browser path | unavailable |

| `sensor.phone_browser_browser_user` | phone browser Browser user | unavailable |

| `sensor.phone_browser_browser_useragent` | phone browser Browser userAgent | unavailable |

| `sensor.phone_browser_browser_visibility` | phone browser Browser visibility | unavailable |

| `sensor.phone_browser_browser_width` | phone browser Browser width | unavailable |

| `sensor.phone_browser_panel` | phone browser Panel | unavailable |

| `sensor.rachels_phone_app_version` | Rachels Phone App Version | 2025.12.1 |

| `sensor.rachels_phone_audio_output` | Rachels Phone Audio Output | unavailable |

| `sensor.rachels_phone_battery_level` | Rachels Phone Battery Level | 25 |

| `sensor.rachels_phone_battery_state` | Rachels Phone Battery State | Not Charging |

| `sensor.rachels_phone_bssid` | Rachels Phone BSSID | unavailable |

| `sensor.rachels_phone_connection_type` | Rachels Phone Connection Type | unavailable |

| `sensor.rachels_phone_geocoded_location` | Rachels Phone Geocoded Location | unavailable |

| `sensor.rachels_phone_last_update_trigger` | Rachels Phone Last Update Trigger | unavailable |

| `sensor.rachels_phone_location_permission` | Rachels Phone Location permission | Authorized Always |

| `sensor.rachels_phone_sim_1` | Rachels Phone SIM 1 | unavailable |

| `sensor.rachels_phone_sim_2` | Rachels Phone SIM 2 | unavailable |

| `sensor.rachels_phone_ssid` | Rachels Phone SSID | unavailable |

| `sensor.rachels_phone_storage` | Rachels Phone Storage | unavailable |

| `sensor.rivian_phone_key_2060_estimated_distance` | Rivian Phone Key 2060 Estimated distance | 72.1784776902887 |

| `sensor.s58cdfccea0786690c_d4a2_estimated_distance` | S58cdfccea0786690C D4A2 Estimated distance | unavailable |

| `sensor.scd0ed4bcbf3abdf0c_652d_estimated_distance` | Estimated distance | unavailable |

| `sensor.sd78d075d9fbca645c_788d_estimated_distance` | Estimated distance | unavailable |

| `sensor.sdf631c51986d49cdc_295e_estimated_distance` | Sdf631c51986d49cdC 295E Estimated distance | unavailable |

| `sensor.shelly_ceiling_fan_energy` | Bedroom Ceiling Fan Energy | 6.848384 |

| `sensor.shelly_ceiling_fan_power` | Bedroom Ceiling Fan Power | 0 |

| `sensor.shelly_ceiling_lights_energy` | Bedroom Ceiling Lights Energy | 5.934152 |

| `sensor.shelly_ceiling_lights_power` | Bedroom Ceiling Lights Power | 0 |

| `sensor.slzb_mr1_connection_mode` | SLZB-MR1 Connection mode | wifi |

| `sensor.slzb_mr1_core_chip_temp` | SLZB-MR1 Core chip temp | 131.0 |

| `sensor.slzb_mr1_firmware_channel` | SLZB-MR1 Firmware channel | release |

| `sensor.slzb_mr1_zigbee_chip_temp` | SLZB-MR1 Zigbee chip temp | 126.554 |

| `sensor.slzb_mr1_zigbee_chip_temp_2` | SLZB-MR1 Zigbee chip temp | 125.636 |

| `sensor.slzb_mr1_zigbee_type` | SLZB-MR1 Zigbee type | thread |

| `sensor.slzb_mr1_zigbee_type_2` | SLZB-MR1 Zigbee type | coordinator |

| `sensor.space_heater_auto_off_at` | Space Heater Auto-off at | unavailable |

| `sensor.space_heater_current` | Space Heater Current | unavailable |

| `sensor.space_heater_current_consumption` | Space Heater Current consumption | unavailable |

| `sensor.space_heater_signal_level` | Space Heater Signal level | unavailable |

| `sensor.space_heater_this_month_s_consumption` | Space Heater This month's consumption | unavailable |

| `sensor.space_heater_today_s_consumption` | Space Heater Today's consumption | unavailable |

| `sensor.space_heater_voltage` | Space Heater Voltage | unavailable |

| `sensor.sun_next_dawn` | Sun Next dawn | 2025-12-24T12:48:36+00:00 |

| `sensor.sun_next_dusk` | Sun Next dusk | 2025-12-24T23:16:42+00:00 |

| `sensor.sun_next_midnight` | Sun Next midnight | 2025-12-25T06:03:07+00:00 |

| `sensor.sun_next_noon` | Sun Next noon | 2025-12-24T18:02:15+00:00 |

| `sensor.sun_next_rising` | Sun Next rising | 2025-12-24T13:19:04+00:00 |

| `sensor.sun_next_setting` | Sun Next setting | 2025-12-24T22:46:14+00:00 |

| `sensor.uptime` | Uptime | 2025-12-19T04:37:24+00:00 |

| `sensor.xkglowrgb_0451_estimated_distance` | Estimated distance | unavailable |

</details>




<details><summary><b>Stt (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `stt.home_assistant_cloud` | Home Assistant Cloud | unknown |

</details>




<details><summary><b>Sun (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `sun.sun` | Sun | below_horizon |

</details>




<details><summary><b>Switch (63)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `switch.alexa_media_player_pre_release` | Alexa Media Player Pre-release | off |

| `switch.aqara_fp300_ai_adaptive_sensitivity` | Aqara FP300 AI adaptive sensitivity | off |

| `switch.aqara_fp300_ai_interference_source_self_identification` | Aqara FP300 AI interference source self-identification | off |

| `switch.aqara_fp300_detection_range_0_1_m` | Aqara FP300 Detection range 0–1 m | on |

| `switch.aqara_fp300_detection_range_1_2_m` | Aqara FP300 Detection range 1–2 m | on |

| `switch.aqara_fp300_detection_range_2_3_m` | Aqara FP300 Detection range 2–3 m | on |

| `switch.aqara_fp300_detection_range_3_4_m` | Aqara FP300 Detection range 3–4 m | on |

| `switch.aqara_fp300_detection_range_4_5_m` | Aqara FP300 Detection range 4–5 m | on |

| `switch.aqara_fp300_detection_range_5_6_m` | Aqara FP300 Detection range 5–6 m | on |

| `switch.bathroom_light` | Bathroom Light | off |

| `switch.bathroom_light_auto_off_enabled` | Bathroom Light Auto-off enabled | off |

| `switch.bathroom_light_auto_update_enabled` | Bathroom Light Auto-update enabled | on |

| `switch.bathroom_light_led` | Bathroom Light LED | off |

| `switch.bed_presence_bb8594_full_range` | Bed Presence Sensor Full Range | off |

| `switch.bedroom_ceiling_fan` | Bedroom ceiling fan | off |

| `switch.bedroom_ceiling_lights` | Bedroom Ceiling Lights | off |

| `switch.bedroom_fan` | Fan | on |

| `switch.blake_s_echo_dot_do_not_disturb` | Blake's Echo Dot Do not disturb | on |

| `switch.blake_s_echo_dot_do_not_disturb_switch` | Blake's Echo Dot do not disturb switch | on |

| `switch.blake_s_echo_dot_repeat_switch` | Blake's Echo Dot repeat switch | unavailable |

| `switch.blake_s_echo_dot_shuffle_switch` | Blake's Echo Dot shuffle switch | unavailable |

| `switch.blake_s_echo_pop_do_not_disturb` | Blake's Echo Pop Do not disturb | on |

| `switch.blake_s_echo_pop_do_not_disturb_switch` | Blake's Echo Pop do not disturb switch | on |

| `switch.blake_s_echo_pop_repeat_switch` | Blake's Echo Pop repeat switch | unavailable |

| `switch.blake_s_echo_pop_shuffle_switch` | Blake's Echo Pop shuffle switch | unavailable |

| `switch.closet_light` | Closet Light | off |

| `switch.closet_light_auto_off_enabled` | Closet Light Auto-off enabled | off |

| `switch.closet_light_auto_update_enabled` | Closet Light Auto-update enabled | on |

| `switch.closet_light_led` | Closet Light LED | off |

| `switch.custom_icons_pre_release` | Custom Icons Pre-release | off |

| `switch.everything_presence_lite_922d28_mmwave_bluetooth` | Everything Presence Lite mmWave Bluetooth | off |

| `switch.everything_presence_lite_922d28_stale_target_reset` | Everything Presence Lite Stale Target Reset | off |

| `switch.everything_presence_lite_922d28_upside_down_mounting` | Everything Presence Lite Upside Down Mounting | off |

| `switch.everywhere_do_not_disturb_switch` | Everywhere do not disturb switch | off |

| `switch.everywhere_repeat_switch` | Everywhere repeat switch | off |

| `switch.everywhere_shuffle_switch` | Everywhere shuffle switch | on |

| `switch.fan_outlet_led` | Fan Outlet LED | off |

| `switch.file_editor` | File editor | on |

| `switch.hacs_pre_release` | HACS Pre-release | off |

| `switch.kitchen_lights` | Kitchen Lights | off |

| `switch.kitchen_lights_auto_off_enabled` | Kitchen Lights Auto-off enabled | off |

| `switch.kitchen_lights_auto_update_enabled` | Kitchen Lights Auto-update enabled | on |

| `switch.kitchen_lights_led` | Kitchen Lights LED | off |

| `switch.living_room_ceiling_fan` | Living Room Ceiling Fan | off |

| `switch.living_room_ceiling_fan_auto_off_enabled` | Living Room Ceiling Fan Auto-off enabled | off |

| `switch.living_room_ceiling_fan_auto_update_enabled` | Living Room Ceiling Fan Auto-update enabled | on |

| `switch.living_room_ceiling_fan_led` | Living Room Ceiling Fan LED | off |

| `switch.living_room_ceiling_lights` | Living Room Ceiling Lights | off |

| `switch.living_room_ceiling_lights_auto_off_enabled` | Living Room Ceiling Lights Auto-off enabled | off |

| `switch.living_room_ceiling_lights_auto_update_enabled` | Living Room Ceiling Lights Auto-update enabled | on |

| `switch.living_room_ceiling_lights_led` | Living Room Ceiling Lights LED | off |

| `switch.main_lights` | Main Lights | off |

| `switch.main_lights_auto_off_enabled` | Main Lights Auto-off enabled | off |

| `switch.main_lights_auto_update_enabled` | Main Lights Auto-update enabled | on |

| `switch.main_lights_led` | Main Lights LED | off |

| `switch.nest_thermostat` | Nest Thermostat | on |

| `switch.shelly_device_aioshelly_ble_integration` | Shelly Device aioshelly_ble_integration | on |

| `switch.slzb_mr1_disable_leds` | SLZB-MR1 Disable LEDs | on |

| `switch.slzb_mr1_led_night_mode` | SLZB-MR1 LED night mode | off |

| `switch.space_heater` | Space Heater | unavailable |

| `switch.space_heater_auto_off_enabled` | Space Heater Auto-off enabled | unavailable |

| `switch.space_heater_auto_update_enabled` | Space Heater Auto-update enabled | unavailable |

| `switch.space_heater_led` | Space Heater LED | unavailable |

</details>






<details><summary><b>Tts (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `tts.home_assistant_cloud` | Home Assistant Cloud | unknown |

</details>




<details><summary><b>Update (26)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `update.alexa_media_player_update` | Alexa Media Player update | off |

| `update.aqara_fp300_firmware` | Aqara FP300 Firmware | unknown |

| `update.bed_presence_bb8594_firmware` | Bed Presence Sensor Firmware | off |

| `update.bedroom_lamp_firmware` | Bedroom Lamp Firmware | unknown |

| `update.browser_mod_update` | browser_mod update | off |

| `update.card_mod_update` | card-mod update | off |

| `update.custom_icons_update` | Custom Icons update | off |

| `update.everything_presence_lite_922d28_everything_presence_lite_firmware` | Everything Presence Lite Everything Presence Lite Firmware | off |

| `update.everything_presence_zone_configurator_update` | Everything Presence Zone Configurator Update | off |

| `update.file_editor_update` | File editor Update | off |

| `update.hacs_update` | HACS update | off |

| `update.home_assistant_core_update` | Home Assistant Core Update | on |

| `update.home_assistant_matter_hub_3_0_0_alpha_76_update` | Home-Assistant-Matter-Hub (3.0.0-alpha.76) Update | off |

| `update.home_assistant_operating_system_update` | Home Assistant Operating System Update | off |

| `update.home_assistant_supervisor_update` | Home Assistant Supervisor Update | off |

| `update.living_room_lamp_firmware` | Living Room Lamp Firmware | unknown |

| `update.matter_server_update` | Matter Server Update | off |

| `update.music_assistant_update` | Music Assistant Update | off |

| `update.openthread_border_router_update` | OpenThread Border Router Update | off |

| `update.philips_rwl020_firmware` | Hue Dimmer Firmware | unknown |

| `update.shelly_device_firmware` | Shelly Device Firmware | off |

| `update.slzb_mr1_core_firmware` | SLZB-MR1 Core firmware | off |

| `update.slzb_mr1_zigbee_firmware` | SLZB-MR1 Zigbee firmware | off |

| `update.slzb_mr1_zigbee_firmware_2` | SLZB-MR1 Zigbee firmware | off |

| `update.sqlite_web_update` | SQLite Web Update | off |

| `update.terminal_ssh_update` | Terminal & SSH Update | off |

</details>




<details><summary><b>Weather (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `weather.openweathermap_2` | OpenWeatherMap | cloudy |

</details>




<details><summary><b>Zone (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `zone.home` | Home | 1 |

| `zone.work` | Work | 0 |

</details> EOF
