_Last Updated: 2025-12-08T02:00:00.258742-06:00_

## 🛠 UI Helpers
Below are the input helpers configured in Home Assistant.





### Boolean
| Entity ID | Name | State | Attributes |
|---|---|---|---|



| `input_boolean.disable_toggle` | **Disable toggle ** | off |  |



| `input_boolean.im_awake_toggle_helper` | **I’m Awake Toggle** | off |  |



| `input_boolean.phone_active` | **Phone active** | on |  |



| `input_boolean.workday_today_toggle` | **Workday Today Toggle** | on |  |



| `input_boolean.workday_toggle_helper` | **General Toggle Helper** | off |  |



| `input_boolean.workday_tomorrow_toggle` | **Workday Tomorrow Toggle** | on |  |









### Datetime
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  

| `input_datetime.home_timestamp` | **Home Timestamp** | 2025-12-07 17:22:48 | has_date=True, has_time=True |



  

| `input_datetime.last_door_open` | **Last Door Open** | 2025-12-07 21:13:43 | has_date=True, has_time=True |



  

| `input_datetime.scheduled_off` | **Scheduled Off** | 1969-12-31 | has_date=True, has_time=False |



  

| `input_datetime.working_override` | **Working Override** | 1969-12-31 | has_date=True, has_time=False |















### Counter
| Entity ID | Name | State | Attributes |
|---|---|---|---|



   

| `counter.counter_helper` | **Counter helper** | 0 | min=0, max=20 |



   

| `counter.door_stuck` | **Door Stuck** | 3 | min=0, max=1000 |






### Timer
| Entity ID | Name | State | Attributes |
|---|---|---|---|



   

| `timer.timer_helper` | **Timer Helper** | idle | duration=0:00:15 |








---

## 🏠 All Entities (By Domain)


<details><summary><b>Automation (13)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `automation.battery_low_automation` | Battery Low Automation | on |

| `automation.bedroom_ceiling_lights_3_set_my_room` | Bedroom Ceiling Lights (3) -> Set My Room | on |

| `automation.door_automation` | Door Automation | on |

| `automation.flic_butttons` | Flic Button | on |

| `automation.goodnight` | Goodnight | on |

| `automation.helper_automation` | Helper Automation | on |

| `automation.hue_dimmer_switch` | Hue Dimmer Switch | off |

| `automation.light_triggers_another_light` | Light Triggers another Light | on |

| `automation.living_room_lamp` | Living Room Lamp | on |

| `automation.nightly_github_sync` | Nightly GitHub sync | on |

| `automation.thermostat` | Thermostat | on |

| `automation.work_schedule_automations` | Work Schedule Automations | on |

| `automation.workday_wake_up` | Workday Wake-up | on |

</details>




<details><summary><b>Binary_sensor (35)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `binary_sensor.50_onn_roku_tv_headphones_connected` | Bedroom TV Headphones connected | off |

| `binary_sensor.50_onn_roku_tv_supports_airplay` | Bedroom TV Supports AirPlay | on |

| `binary_sensor.50_onn_roku_tv_supports_ethernet` | Bedroom TV Supports Ethernet | on |

| `binary_sensor.50_onn_roku_tv_supports_find_remote` | Bedroom TV Supports find remote | on |

| `binary_sensor.bathroom_light_cloud_connection` | Bathroom Light Cloud connection | on |

| `binary_sensor.bathroom_light_overheated` | Bathroom Light Overheated | off |

| `binary_sensor.bed_presence_bb8594_bed_occupied_both` | Bed Presence Sensor Bed Occupied Both | off |

| `binary_sensor.bed_presence_bb8594_bed_occupied_either` | Bed Presence Sensor Bed Occupied Either | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left` | Bed Presence Sensor Bed Occupied Left | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left_fast` | Bed Presence Sensor Bed Occupied Left (Fast) | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left_normal` | Bed Presence Sensor Bed Occupied Left (Normal) | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_right` | Bed Presence Sensor Bed Occupied Right | off |

| `binary_sensor.bed_presence_bb8594_status` | Bed Presence Sensor Status | on |

| `binary_sensor.blake_s_echo_dot_connectivity` | Blake's Echo Dot Connectivity | on |

| `binary_sensor.blake_s_echo_pop_connectivity` | Blake's Echo Pop Connectivity | on |

| `binary_sensor.closet_light_cloud_connection` | Closet Light Cloud connection | on |

| `binary_sensor.closet_light_overheated` | Closet Light Overheated | off |

| `binary_sensor.everywhere_connectivity` | Everywhere Connectivity | on |

| `binary_sensor.fan_outlet_cloud_connection` | Fan Outlet Cloud connection | on |

| `binary_sensor.front_door` | Front door | off |

| `binary_sensor.main_lights_cloud_connection` | Main Lights Cloud connection | on |

| `binary_sensor.motion_1_motion` | Motion 1 | off |

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

| `binary_sensor.workday_tomorrow_template_sensor` | Workday Tomorrow Template Sensor | on |

</details>




<details><summary><b>Button (9)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `button.bed_presence_bb8594_calibrate_left_occupied` | Bed Presence Sensor Calibrate Left Occupied | 2025-12-02T05:21:48.234043+00:00 |

| `button.bed_presence_bb8594_calibrate_left_unoccupied` | Bed Presence Sensor Calibrate Left Unoccupied | 2025-12-02T05:29:13.586934+00:00 |

| `button.bed_presence_bb8594_calibrate_right_occupied` | Bed Presence Sensor Calibrate Right Occupied | 2025-12-02T05:30:00.329341+00:00 |

| `button.bed_presence_bb8594_calibrate_right_unoccupied` | Bed Presence Sensor Calibrate Right Unoccupied | 2025-12-02T05:31:49.498289+00:00 |

| `button.bed_presence_bb8594_restart` | Bed Presence Sensor Restart | unknown |

| `button.nest_thermostat_identify` | Nest Thermostat Identify | unknown |

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






<details><summary><b>Device_tracker (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `device_tracker.blakes_iphone` | Blakes iPhone | home |

| `device_tracker.ipad` | iPad | home |

</details>




<details><summary><b>Event (7)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `event.backup_automatic_backup` | Backup Automatic backup | 2025-12-07T11:04:15.729+00:00 |

| `event.bthome_sensor_3370_button` | Motion 1 Button | 2025-10-19T05:15:17.292+00:00 |

| `event.front_door_sensor_button` | Front Door Sensor Button | 2025-10-19T05:12:22.248+00:00 |

| `event.hue_dimmer_switch_button_1` | Hue Dimmer Switch Button 1 | 2025-12-08T07:42:51.118+00:00 |

| `event.hue_dimmer_switch_button_2` | Hue Dimmer Switch Button 2 | 2025-12-07T03:18:34.363+00:00 |

| `event.hue_dimmer_switch_button_3` | Hue Dimmer Switch Button 3 | 2025-12-08T07:39:53.570+00:00 |

| `event.hue_dimmer_switch_button_4` | Hue Dimmer Switch Button 4 | 2025-12-08T07:59:55.089+00:00 |

</details>




<details><summary><b>Fan (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `fan.bedroom_ceiling_fan` | Bedroom Ceiling Fan | off |

| `fan.bedroom_fan` | Fan | off |

</details>








<details><summary><b>Light (7)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `light.bathroom_light` | Bathroom Light | off |

| `light.bedroom_ceiling_lights` | Bedroom Ceiling Lights | off |

| `light.bedroom_lamp` | Bedroom Lamp | on |

| `light.closet_light` | Closet Light | off |

| `light.home` | Home | on |

| `light.living_room_lamp` | Living Room Lamp | on |

| `light.main_lights` | Main Lights | off |

</details>




<details><summary><b>Media_player (5)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `media_player.bedroom_tv` | Bedroom Tv | idle |

| `media_player.blake_s_echo_dot` | Blake's Echo Dot | paused |

| `media_player.blake_s_echo_pop` | Blake's Echo Pop | paused |

| `media_player.everywhere` | Everywhere | paused |

| `media_player.living_room_tv` | Living Room TV | off |

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




<details><summary><b>Number (9)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `number.bathroom_light_turn_off_in` | Bathroom Light Turn off in | 120 |

| `number.bed_presence_bb8594_left_occupied_pressure` | Bed Presence Sensor Left Occupied Pressure | 95.96 |

| `number.bed_presence_bb8594_left_trigger_pressure` | Bed Presence Sensor Left Trigger Pressure | 91.6 |

| `number.bed_presence_bb8594_left_unoccupied_pressure` | Bed Presence Sensor Left Unoccupied Pressure | 78.5 |

| `number.bed_presence_bb8594_right_occupied_pressure` | Bed Presence Sensor Right Occupied Pressure | 97.65 |

| `number.bed_presence_bb8594_right_trigger_pressure` | Bed Presence Sensor Right Trigger Pressure | 94.78 |

| `number.bed_presence_bb8594_right_unoccupied_pressure` | Bed Presence Sensor Right Unoccupied Pressure | 86.16 |

| `number.closet_light_turn_off_in` | Closet Light Turn off in | 120 |

| `number.main_lights_turn_off_in` | Main Lights Turn off in | 120 |

</details>




<details><summary><b>Person (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `person.blake_foster` | Blake Foster | home |

</details>




<details><summary><b>Remote (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `remote.bedroom_tv` | Bedroom Tv Remote | on |

</details>




<details><summary><b>Scene (12)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `scene.all_lights` | All Lights | 2025-12-07T23:40:13.533365+00:00 |

| `scene.all_lights_off` | All Lights Off | 2025-12-08T07:42:47.295296+00:00 |

| `scene.all_off` | All Off | 2025-12-05T01:45:41.567623+00:00 |

| `scene.bedroom_lights_off` | Bedroom Lights Off | 2025-12-01T04:20:08.903975+00:00 |

| `scene.dimmed` | Dimmed | 2025-12-01T04:20:32.143898+00:00 |

| `scene.full_lamp` | Full Lamp | 2025-12-07T17:16:35.801575+00:00 |

| `scene.goodnight_scene` | Goodnight | 2025-12-08T03:13:41.162632+00:00 |

| `scene.im_awake` | I’m Awake | 2025-12-02T12:31:03.745110+00:00 |

| `scene.night_light` | Night Light | 2025-09-26T00:17:04.739409+00:00 |

| `scene.set_my_room` | Set My Room | 2025-12-08T07:42:51.123919+00:00 |

| `scene.thermostat_away` | Thermostat Away | 2025-12-05T15:03:36.163527+00:00 |

| `scene.thermostat_ideal_evening` | Thermostat 68/70 | 2025-11-28T11:14:37.942932+00:00 |

</details>




<details><summary><b>Script (4)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `script.alarm_music_script` | Alarm Music Script | off |

| `script.create_push_ha_info_to_github_gemini_zip` | Create & Push HA Info to GitHub & Gemini Zip | on |

| `script.find_remote` | Find Remote | off |

| `script.set_date_to_today` | Scheduled Off & Working Override dashboard script | off |

</details>




<details><summary><b>Select (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `select.bed_presence_bb8594_bluetooth_scanner_mode` | Bed Presence Sensor Bluetooth Scanner Mode | Active |

| `select.bed_presence_bb8594_response_speed` | Bed Presence Sensor Response Speed | Slow |

</details>




<details><summary><b>Sensor (93)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `sensor.50_onn_roku_tv_active_app` | Bedroom TV Active app | YouTube |

| `sensor.50_onn_roku_tv_active_app_id` | Bedroom TV Active app ID | 837 |

| `sensor.backup_backup_manager_state` | Backup Backup Manager state | idle |

| `sensor.backup_last_attempted_automatic_backup` | Backup Last attempted automatic backup | 2025-12-07T11:03:24+00:00 |

| `sensor.backup_last_successful_automatic_backup` | Backup Last successful automatic backup | 2025-12-07T11:04:15+00:00 |

| `sensor.backup_next_scheduled_automatic_backup` | Backup Next scheduled automatic backup | 2025-12-08T10:56:49+00:00 |

| `sensor.bathroom_light_auto_off_at` | Bathroom Light Auto-off at | unknown |

| `sensor.bathroom_light_signal_level` | Bathroom Light Signal level | 3 |

| `sensor.bed_presence_bb8594_left_pressure` | Bed Presence Sensor Left Pressure | 96.0495910644531 |

| `sensor.bed_presence_bb8594_right_pressure` | Bed Presence Sensor Right Pressure | 85.6639785766602 |

| `sensor.bed_presence_bb8594_uptime` | Bed Presence Sensor Uptime | 534977.5 |

| `sensor.bed_presence_bb8594_wifi_signal_db` | Bed Presence Sensor WiFi Signal dB | -45.0 |

| `sensor.bed_presence_bb8594_wifi_signal_percent` | Bed Presence Sensor WiFi Signal Percent | 100.0 |

| `sensor.bedroom_ceiling_fan_energy_consumed` | Bedroom Ceiling Fan Energy consumed | 5.720009 |

| `sensor.blake_foster30_gmail_com_vacation_end_date` | blake.foster30@gmail.com Vacation end date | unknown |

| `sensor.blake_s_echo_dot_illuminance` | Blake's Echo Dot Illuminance | 0.0 |

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

| `sensor.blakes_iphone_app_version` | Blakes iPhone App Version | 2025.12.1 |

| `sensor.blakes_iphone_battery_level` | Blakes iPhone Battery Level | 80 |

| `sensor.blakes_iphone_battery_state` | Blakes iPhone Battery State | Charging |

| `sensor.blakes_iphone_geocoded_location` | Blakes iPhone Geocoded Location | 1104 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.blakes_iphone_ssid` | Blakes iPhone SSID | ATTEPISyDS |

| `sensor.bthome_sensor_3370_battery` | Motion 1 Battery | 100 |

| `sensor.bthome_sensor_3370_illuminance` | Motion 1 Illuminance | 0.0 |

| `sensor.bthome_sensor_3370_packet_id` | Motion 1 Packet Id | 199 |

| `sensor.bthome_sensor_3370_signal_strength` | Motion 1 Signal Strength | -65 |

| `sensor.closet_light_auto_off_at` | Closet Light Auto-off at | unknown |

| `sensor.closet_light_signal_level` | Closet Light Signal level | 3 |

| `sensor.everywhere_next_alarm` | Everywhere Next alarm | unavailable |

| `sensor.everywhere_next_reminder` | Everywhere Next reminder | unavailable |

| `sensor.everywhere_next_timer` | Everywhere Next timer | unavailable |

| `sensor.front_door_sensor_battery` | Front Door Sensor Battery | 91 |

| `sensor.front_door_sensor_illuminance` | Front Door Sensor Illuminance | 0.0 |

| `sensor.front_door_sensor_rotation` | Front Door Sensor Rotation | 0.0 |

| `sensor.hue_dimmer_switch_1_battery` | Hue Dimmer Switch Battery | 100 |

| `sensor.ipad_app_version` | iPad App Version | 2025.10.0 |

| `sensor.ipad_battery_level` | iPad Battery Level | 100 |

| `sensor.ipad_battery_state` | iPad Battery State | Charging |

| `sensor.ipad_geocoded_location` | iPad Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.ipad_ssid` | iPad SSID | ATTEPISyDS |

| `sensor.main_lights_auto_off_at` | Main Lights Auto-off at | unknown |

| `sensor.main_lights_current` | Main Lights Current | 0.01 |

| `sensor.main_lights_current_consumption` | Main Lights Current consumption | 0.0 |

| `sensor.main_lights_signal_level` | Main Lights Signal level | 3 |

| `sensor.main_lights_this_month_s_consumption` | Main Lights This month's consumption | 1.018 |

| `sensor.main_lights_today_s_consumption` | Main Lights Today's consumption | 0.0 |

| `sensor.main_lights_voltage` | Main Lights Voltage | 123.4 |

| `sensor.nest_thermostat_temperature` | Nest Thermostat Temperature | 68.432 |

| `sensor.openweathermap_cloud_coverage_2` | OpenWeatherMap Cloud coverage | 100 |

| `sensor.openweathermap_condition_2` | OpenWeatherMap Condition | cloudy |

| `sensor.openweathermap_dew_point_2` | OpenWeatherMap Dew point temperature | 20.138 |

| `sensor.openweathermap_feels_like_temperature_2` | OpenWeatherMap Apparent temperature | 16.394 |

| `sensor.openweathermap_humidity_2` | OpenWeatherMap Humidity | 79 |

| `sensor.openweathermap_precipitation_kind_2` | OpenWeatherMap Precipitation kind | None |

| `sensor.openweathermap_pressure_2` | OpenWeatherMap Pressure | 14.895376298251 |

| `sensor.openweathermap_rain_2` | OpenWeatherMap Rain intensity | 0.0 |

| `sensor.openweathermap_snow_2` | OpenWeatherMap Snow intensity | 0.0 |

| `sensor.openweathermap_temperature_2` | OpenWeatherMap Temperature | 25.088 |

| `sensor.openweathermap_uv_index_2` | OpenWeatherMap UV index | 0 |

| `sensor.openweathermap_visibility_2` | OpenWeatherMap Visibility | 32808.3989501312 |

| `sensor.openweathermap_weather_2` | OpenWeatherMap Weather | overcast clouds |

| `sensor.openweathermap_weather_code_2` | OpenWeatherMap Weather code | 804 |

| `sensor.openweathermap_wind_bearing_2` | OpenWeatherMap Wind direction | 360 |

| `sensor.openweathermap_wind_gust_2` | OpenWeatherMap Wind gust speed | unknown |

| `sensor.openweathermap_wind_speed_2` | OpenWeatherMap Wind speed | 8.05297065139585 |

| `sensor.shelly_ceiling_fan_energy` | Bedroom Ceiling Fan Energy | 5.720009 |

| `sensor.shelly_ceiling_fan_power` | Bedroom Ceiling Fan Power | 0 |

| `sensor.shelly_ceiling_lights_energy` | Bedroom Ceiling Lights Energy | 4.829384 |

| `sensor.shelly_ceiling_lights_power` | Bedroom Ceiling Lights Power | 0 |

| `sensor.slzb_mr1_connection_mode` | SLZB-MR1 Connection mode | wifi |

| `sensor.slzb_mr1_core_chip_temp` | SLZB-MR1 Core chip temp | 132.008 |

| `sensor.slzb_mr1_firmware_channel` | SLZB-MR1 Firmware channel | release |

| `sensor.slzb_mr1_zigbee_chip_temp` | SLZB-MR1 Zigbee chip temp | 129.794 |

| `sensor.slzb_mr1_zigbee_chip_temp_2` | SLZB-MR1 Zigbee chip temp | 126.14 |

| `sensor.slzb_mr1_zigbee_type` | SLZB-MR1 Zigbee type | thread |

| `sensor.slzb_mr1_zigbee_type_2` | SLZB-MR1 Zigbee type | coordinator |

| `sensor.sun_next_dawn` | Sun Next dawn | 2025-12-08T12:38:37+00:00 |

| `sensor.sun_next_dusk` | Sun Next dusk | 2025-12-08T23:11:05+00:00 |

| `sensor.sun_next_midnight` | Sun Next midnight | 2025-12-09T05:55:23+00:00 |

| `sensor.sun_next_noon` | Sun Next noon | 2025-12-08T17:54:36+00:00 |

| `sensor.sun_next_rising` | Sun Next rising | 2025-12-08T13:08:52+00:00 |

| `sensor.sun_next_setting` | Sun Next setting | 2025-12-08T22:40:50+00:00 |

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




<details><summary><b>Switch (36)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `switch.alexa_media_player_pre_release` | Alexa Media Player Pre-release | off |

| `switch.bathroom_light` | Bathroom Light | off |

| `switch.bathroom_light_auto_off_enabled` | Bathroom Light Auto-off enabled | off |

| `switch.bathroom_light_auto_update_enabled` | Bathroom Light Auto-update enabled | on |

| `switch.bathroom_light_led` | Bathroom Light LED | off |

| `switch.bed_presence_bb8594_full_range` | Bed Presence Sensor Full Range | off |

| `switch.bedroom_ceiling_fan` | Bedroom ceiling fan | off |

| `switch.bedroom_ceiling_lights` | Bedroom Ceiling Lights | off |

| `switch.bedroom_fan` | Fan | off |

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

| `switch.everywhere_do_not_disturb_switch` | Everywhere do not disturb switch | off |

| `switch.everywhere_repeat_switch` | Everywhere repeat switch | off |

| `switch.everywhere_shuffle_switch` | Everywhere shuffle switch | off |

| `switch.fan_outlet_led` | Fan Outlet LED | off |

| `switch.file_editor` | File editor | on |

| `switch.hacs_pre_release` | HACS Pre-release | off |

| `switch.main_lights` | Main Lights | off |

| `switch.main_lights_auto_off_enabled` | Main Lights Auto-off enabled | off |

| `switch.main_lights_auto_update_enabled` | Main Lights Auto-update enabled | on |

| `switch.main_lights_led` | Main Lights LED | off |

| `switch.nest_thermostat` | Nest Thermostat | on |

| `switch.shelly_device_aioshelly_ble_integration` | Shelly Device aioshelly_ble_integration | on |

| `switch.slzb_mr1_disable_leds` | SLZB-MR1 Disable LEDs | off |

| `switch.slzb_mr1_led_night_mode` | SLZB-MR1 LED night mode | off |

</details>






<details><summary><b>Tts (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `tts.home_assistant_cloud` | Home Assistant Cloud | unknown |

</details>




<details><summary><b>Update (18)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `update.alexa_media_player_update` | Alexa Media Player update | off |

| `update.bed_presence_bb8594_firmware` | Bed Presence Sensor Firmware | off |

| `update.card_mod_update` | card-mod update | off |

| `update.custom_icons_update` | Custom Icons update | off |

| `update.file_editor_update` | File editor Update | off |

| `update.hacs_update` | HACS update | off |

| `update.home_assistant_core_update` | Home Assistant Core Update | on |

| `update.home_assistant_matter_hub_3_0_0_alpha_76_update` | Home-Assistant-Matter-Hub (3.0.0-alpha.76) Update | off |

| `update.home_assistant_operating_system_update` | Home Assistant Operating System Update | off |

| `update.home_assistant_supervisor_update` | Home Assistant Supervisor Update | off |

| `update.matter_server_update` | Matter Server Update | off |

| `update.music_assistant_update` | Music Assistant Update | off |

| `update.openthread_border_router_update` | OpenThread Border Router Update | off |

| `update.shelly_device_firmware` | Shelly Device Firmware | off |

| `update.slzb_mr1_core_firmware` | SLZB-MR1 Core firmware | off |

| `update.slzb_mr1_zigbee_firmware` | SLZB-MR1 Zigbee firmware | off |

| `update.slzb_mr1_zigbee_firmware_2` | SLZB-MR1 Zigbee firmware | off |

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
