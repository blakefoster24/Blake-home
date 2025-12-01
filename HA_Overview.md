_Last Updated: 2025-12-01T06:20:58.458683-06:00_

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



  

| `input_datetime.home_timestamp` | **Home Timestamp** | 2025-12-01 00:00:00 | has_date=True, has_time=True |



  

| `input_datetime.last_door_open` | **Last Door Open** | 2025-11-30 20:11:13 | has_date=True, has_time=True |



  

| `input_datetime.scheduled_off` | **Scheduled Off** | 1969-12-31 | has_date=True, has_time=False |



  

| `input_datetime.working_override` | **Working Override** | 1969-12-31 | has_date=True, has_time=False |






### Number
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  

| `input_number.phone_charging_distance` | **Phone Charging -> Distance** | 0.011 | min=0.0, max=100.0, step=0.01 |












### Counter
| Entity ID | Name | State | Attributes |
|---|---|---|---|



   

| `counter.counter_helper` | **Counter helper** | 0 | min=0, max=20 |



   

| `counter.door_stuck` | **Door Stuck** | 2 | min=0, max=1000 |






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

| `automation.hue_dimmer_switch` | Hue Dimmer Switch | on |

| `automation.light_triggers_another_light` | Light Triggers another Light | on |

| `automation.living_room_lamp` | Living Room Lamp | on |

| `automation.nightly_github_sync` | Nightly GitHub sync | on |

| `automation.test_bay` | Test Bay | on |

| `automation.thermostat` | Thermostat | on |

| `automation.work_schedule_automations` | Work Schedule Automations | on |

| `automation.workday_wake_up` | Workday Wake-up | on |

</details>




<details><summary><b>Binary_sensor (22)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `binary_sensor.50_onn_roku_tv_headphones_connected` | Bedroom TV Headphones connected | off |

| `binary_sensor.50_onn_roku_tv_supports_airplay` | Bedroom TV Supports AirPlay | on |

| `binary_sensor.50_onn_roku_tv_supports_ethernet` | Bedroom TV Supports Ethernet | on |

| `binary_sensor.50_onn_roku_tv_supports_find_remote` | Bedroom TV Supports find remote | on |

| `binary_sensor.bathroom_light_cloud_connection` | Bathroom Light Cloud connection | on |

| `binary_sensor.bathroom_light_overheated` | Bathroom Light Overheated | off |

| `binary_sensor.closet_light_cloud_connection` | Closet Light Cloud connection | on |

| `binary_sensor.closet_light_overheated` | Closet Light Overheated | off |

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

| `binary_sensor.workday_tomorrow_template_sensor` | Workday Tomorrow Template Sensor | on |

</details>




<details><summary><b>Button (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `button.nest_thermostat_identify` | Nest Thermostat Identify | unknown |

| `button.shelly_device_reboot` | Shelly Device Restart | unknown |

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

| `event.backup_automatic_backup` | Backup Automatic backup | 2025-12-01T11:39:38.638+00:00 |

| `event.bthome_sensor_3370_button` | Motion 1 Button | 2025-10-19T05:15:17.292+00:00 |

| `event.front_door_sensor_button` | Front Door Sensor Button | 2025-10-19T05:12:22.248+00:00 |

| `event.hue_dimmer_switch_button_1` | Hue Dimmer Switch Button 1 | 2025-12-01T09:22:43.003+00:00 |

| `event.hue_dimmer_switch_button_2` | Hue Dimmer Switch Button 2 | 2025-11-27T01:36:36.755+00:00 |

| `event.hue_dimmer_switch_button_3` | Hue Dimmer Switch Button 3 | 2025-11-30T00:01:56.136+00:00 |

| `event.hue_dimmer_switch_button_4` | Hue Dimmer Switch Button 4 | 2025-11-30T18:37:16.819+00:00 |

</details>




<details><summary><b>Fan (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `fan.bedroom_ceiling_fan` | Bedroom Ceiling Fan | on |

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




<details><summary><b>Media_player (6)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `media_player.bedroom_tv` | Bedroom Tv | idle |

| `media_player.blake_s_echo_dot` | Blake's Echo Dot | idle |

| `media_player.blake_s_echo_pop` | Blake's Echo Pop | idle |

| `media_player.everywhere` | Everywhere | idle |

| `media_player.living_room_tv` | Living Room TV | off |

| `media_player.this_device` | This Device | idle |

</details>




<details><summary><b>Number (3)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `number.bathroom_light_turn_off_in` | Bathroom Light Turn off in | 120 |

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

| `scene.all_lights` | All Lights | 2025-11-30T23:58:31.241650+00:00 |

| `scene.all_lights_off` | All Lights Off | 2025-11-30T18:35:29.589418+00:00 |

| `scene.all_off` | All Off | 2025-12-01T02:11:13.318491+00:00 |

| `scene.bedroom_lights_off` | Bedroom Lights Off | 2025-12-01T04:20:08.903975+00:00 |

| `scene.dimmed` | Dimmed | 2025-12-01T04:20:32.143898+00:00 |

| `scene.full_lamp` | Full Lamp | 2025-12-01T04:20:10.831584+00:00 |

| `scene.goodnight_scene` | Goodnight | 2025-12-01T06:48:39.761238+00:00 |

| `scene.im_awake` | I’m Awake | 2025-11-19T14:48:00.759367+00:00 |

| `scene.night_light` | Night Light | 2025-09-26T00:17:04.739409+00:00 |

| `scene.set_my_room` | Set My Room | 2025-12-01T09:22:43.013957+00:00 |

| `scene.thermostat_away` | Thermostat Away | 2025-11-28T11:16:07.638935+00:00 |

| `scene.thermostat_ideal_evening` | Thermostat 68/70 | 2025-11-28T11:14:37.942932+00:00 |

</details>




<details><summary><b>Script (4)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `script.alarm_script` | Alarm Script | off |

| `script.create_push_ha_info_to_github` | Create & Push HA Info to Github | on |

| `script.find_remote` | Find Remote | off |

| `script.set_date_to_today` | Set Date to Today | off |

</details>




<details><summary><b>Sensor (89)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `sensor.50_onn_roku_tv_active_app` | Bedroom TV Active app | Home |

| `sensor.50_onn_roku_tv_active_app_id` | Bedroom TV Active app ID | 562859 |

| `sensor.backup_backup_manager_state` | Backup Backup Manager state | idle |

| `sensor.backup_last_attempted_automatic_backup` | Backup Last attempted automatic backup | 2025-12-01T11:38:54+00:00 |

| `sensor.backup_last_successful_automatic_backup` | Backup Last successful automatic backup | 2025-12-01T11:39:38+00:00 |

| `sensor.backup_next_scheduled_automatic_backup` | Backup Next scheduled automatic backup | 2025-12-02T10:46:06+00:00 |

| `sensor.bathroom_light_auto_off_at` | Bathroom Light Auto-off at | unknown |

| `sensor.bathroom_light_signal_level` | Bathroom Light Signal level | 3 |

| `sensor.bedroom_ceiling_fan_energy_consumed` | Bedroom Ceiling Fan Energy consumed | 5.293935 |

| `sensor.blake_foster30_gmail_com_vacation_end_date` | blake.foster30@gmail.com Vacation end date | unknown |

| `sensor.blake_s_echo_dot_next_alarm` | Blake's Echo Dot next Alarm | unknown |

| `sensor.blake_s_echo_dot_next_reminder` | Blake's Echo Dot next Reminder | unknown |

| `sensor.blake_s_echo_dot_next_timer` | Blake's Echo Dot next Timer | unknown |

| `sensor.blake_s_echo_pop_next_alarm` | Blake's Echo Pop next Alarm | unknown |

| `sensor.blake_s_echo_pop_next_reminder` | Blake's Echo Pop next Reminder | unknown |

| `sensor.blake_s_echo_pop_next_timer` | Blake's Echo Pop next Timer | unknown |

| `sensor.blakes_iphone_app_version` | Blakes iPhone App Version | 2025.10.0 |

| `sensor.blakes_iphone_audio_output` | Blakes iPhone Audio Output | Built-in Speaker |

| `sensor.blakes_iphone_battery_level` | Blakes iPhone Battery Level | 80 |

| `sensor.blakes_iphone_battery_state` | Blakes iPhone Battery State | Charging |

| `sensor.blakes_iphone_bssid` | Blakes iPhone BSSID | e6:f7:5b:a5:be:b3 |

| `sensor.blakes_iphone_connection_type` | Blakes iPhone Connection Type | Wi-Fi |

| `sensor.blakes_iphone_geocoded_location` | Blakes iPhone Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.blakes_iphone_last_update_trigger` | Blakes iPhone Last Update Trigger | Periodic |

| `sensor.blakes_iphone_location_permission` | Blakes iPhone Location permission | Authorized Always |

| `sensor.blakes_iphone_sim_1` | Blakes iPhone SIM 1 | -- |

| `sensor.blakes_iphone_sim_2` | Blakes iPhone SIM 2 | -- |

| `sensor.blakes_iphone_ssid` | Blakes iPhone SSID | ATTEPISyDS |

| `sensor.blakes_iphone_storage` | Blakes iPhone Storage | 58.28 |

| `sensor.bthome_sensor_3370_battery` | Motion 1 Battery | 100 |

| `sensor.bthome_sensor_3370_illuminance` | Motion 1 Illuminance | 0.0 |

| `sensor.bthome_sensor_3370_packet_id` | Motion 1 Packet Id | 220 |

| `sensor.bthome_sensor_3370_signal_strength` | Motion 1 Signal Strength | -66 |

| `sensor.closet_light_auto_off_at` | Closet Light Auto-off at | unknown |

| `sensor.closet_light_signal_level` | Closet Light Signal level | 3 |

| `sensor.front_door_sensor_battery` | Front Door Sensor Battery | 89 |

| `sensor.front_door_sensor_illuminance` | Front Door Sensor Illuminance | 0.0 |

| `sensor.front_door_sensor_rotation` | Front Door Sensor Rotation | 0.0 |

| `sensor.hue_dimmer_switch_1_battery` | Hue Dimmer Switch Battery | 100 |

| `sensor.ipad_app_version` | iPad App Version | 2025.10.0 |

| `sensor.ipad_audio_output` | iPad Audio Output | unavailable |

| `sensor.ipad_battery_level` | iPad Battery Level | 100 |

| `sensor.ipad_battery_state` | iPad Battery State | Charging |

| `sensor.ipad_bssid` | iPad BSSID | e6:f7:5b:a5:be:b3 |

| `sensor.ipad_connection_type` | iPad Connection Type | unavailable |

| `sensor.ipad_geocoded_location` | iPad Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.ipad_last_update_trigger` | iPad Last Update Trigger | unavailable |

| `sensor.ipad_location_permission` | iPad Location permission | Authorized Always |

| `sensor.ipad_sim_1` | iPad SIM 1 | unavailable |

| `sensor.ipad_ssid` | iPad SSID | ATTEPISyDS |

| `sensor.ipad_storage` | iPad Storage | unavailable |

| `sensor.main_lights_auto_off_at` | Main Lights Auto-off at | unknown |

| `sensor.main_lights_current` | Main Lights Current | 0.0 |

| `sensor.main_lights_current_consumption` | Main Lights Current consumption | 0.0 |

| `sensor.main_lights_signal_level` | Main Lights Signal level | 3 |

| `sensor.main_lights_this_month_s_consumption` | Main Lights This month's consumption | 0.0 |

| `sensor.main_lights_today_s_consumption` | Main Lights Today's consumption | 0.0 |

| `sensor.main_lights_voltage` | Main Lights Voltage | 121.9 |

| `sensor.nest_thermostat_temperature` | Nest Thermostat Temperature | 68.504 |

| `sensor.openweathermap_cloud_coverage_2` | OpenWeatherMap Cloud coverage | 100 |

| `sensor.openweathermap_condition_2` | OpenWeatherMap Condition | cloudy |

| `sensor.openweathermap_dew_point_2` | OpenWeatherMap Dew point temperature | 18.734 |

| `sensor.openweathermap_feels_like_temperature_2` | OpenWeatherMap Apparent temperature | 18.14 |

| `sensor.openweathermap_humidity_2` | OpenWeatherMap Humidity | 80 |

| `sensor.openweathermap_precipitation_kind_2` | OpenWeatherMap Precipitation kind | None |

| `sensor.openweathermap_pressure_2` | OpenWeatherMap Pressure | 14.9388876214202 |

| `sensor.openweathermap_rain_2` | OpenWeatherMap Rain intensity | 0.0 |

| `sensor.openweathermap_snow_2` | OpenWeatherMap Snow intensity | 0.0 |

| `sensor.openweathermap_temperature_2` | OpenWeatherMap Temperature | 23.396 |

| `sensor.openweathermap_uv_index_2` | OpenWeatherMap UV index | 0 |

| `sensor.openweathermap_visibility_2` | OpenWeatherMap Visibility | 32808.3989501312 |

| `sensor.openweathermap_weather_2` | OpenWeatherMap Weather | overcast clouds |

| `sensor.openweathermap_weather_code_2` | OpenWeatherMap Weather code | 804 |

| `sensor.openweathermap_wind_bearing_2` | OpenWeatherMap Wind direction | 169 |

| `sensor.openweathermap_wind_gust_2` | OpenWeatherMap Wind gust speed | 5.9949892627058 |

| `sensor.openweathermap_wind_speed_2` | OpenWeatherMap Wind speed | 4.00411596277738 |

| `sensor.shelly_ceiling_fan_energy` | Bedroom Ceiling Fan Energy | 5.293935 |

| `sensor.shelly_ceiling_fan_power` | Bedroom Ceiling Fan Power | 13.8 |

| `sensor.shelly_ceiling_lights_energy` | Bedroom Ceiling Lights Energy | 3.910706 |

| `sensor.shelly_ceiling_lights_power` | Bedroom Ceiling Lights Power | 0 |

| `sensor.sun_next_dawn` | Sun Next dawn | 2025-12-01T12:32:34+00:00 |

| `sensor.sun_next_dusk` | Sun Next dusk | 2025-12-01T23:11:15+00:00 |

| `sensor.sun_next_midnight` | Sun Next midnight | 2025-12-02T05:52:25+00:00 |

| `sensor.sun_next_noon` | Sun Next noon | 2025-12-01T17:51:45+00:00 |

| `sensor.sun_next_rising` | Sun Next rising | 2025-12-01T13:02:31+00:00 |

| `sensor.sun_next_setting` | Sun Next setting | 2025-12-01T22:41:18+00:00 |

| `sensor.this_device_next_alarm` | This Device next Alarm | unknown |

| `sensor.this_device_next_reminder` | This Device next Reminder | unknown |

| `sensor.this_device_next_timer` | This Device next Timer | unknown |

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




<details><summary><b>Switch (32)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `switch.alexa_media_player_pre_release` | Alexa Media Player Pre-release | off |

| `switch.bathroom_light` | Bathroom Light | off |

| `switch.bathroom_light_auto_off_enabled` | Bathroom Light Auto-off enabled | off |

| `switch.bathroom_light_auto_update_enabled` | Bathroom Light Auto-update enabled | on |

| `switch.bathroom_light_led` | Bathroom Light LED | off |

| `switch.bedroom_ceiling_fan` | Bedroom ceiling fan | on |

| `switch.bedroom_ceiling_lights` | Bedroom Ceiling Lights | off |

| `switch.bedroom_fan` | Fan | off |

| `switch.blake_s_echo_dot_do_not_disturb_switch` | Blake's Echo Dot do not disturb switch | on |

| `switch.blake_s_echo_dot_repeat_switch` | Blake's Echo Dot repeat switch | unavailable |

| `switch.blake_s_echo_dot_shuffle_switch` | Blake's Echo Dot shuffle switch | unavailable |

| `switch.blake_s_echo_pop_do_not_disturb_switch` | Blake's Echo Pop do not disturb switch | on |

| `switch.blake_s_echo_pop_repeat_switch` | Blake's Echo Pop repeat switch | unavailable |

| `switch.blake_s_echo_pop_shuffle_switch` | Blake's Echo Pop shuffle switch | unavailable |

| `switch.closet_light` | Closet Light | off |

| `switch.closet_light_auto_off_enabled` | Closet Light Auto-off enabled | off |

| `switch.closet_light_auto_update_enabled` | Closet Light Auto-update enabled | on |

| `switch.closet_light_led` | Closet Light LED | off |

| `switch.custom_icons_pre_release` | Custom Icons Pre-release | off |

| `switch.everywhere_do_not_disturb_switch` | Everywhere do not disturb switch | off |

| `switch.everywhere_repeat_switch` | Everywhere repeat switch | unavailable |

| `switch.everywhere_shuffle_switch` | Everywhere shuffle switch | unavailable |

| `switch.fan_outlet_led` | Fan Outlet LED | off |

| `switch.file_editor` | File editor | on |

| `switch.hacs_pre_release` | HACS Pre-release | off |

| `switch.main_lights` | Main Lights | off |

| `switch.main_lights_auto_off_enabled` | Main Lights Auto-off enabled | off |

| `switch.main_lights_auto_update_enabled` | Main Lights Auto-update enabled | on |

| `switch.main_lights_led` | Main Lights LED | off |

| `switch.nest_thermostat` | Nest Thermostat | on |

| `switch.shelly_device_aioshelly_ble_integration` | Shelly Device aioshelly_ble_integration | on |

| `switch.this_device_do_not_disturb_switch` | This Device do not disturb switch | off |

</details>






<details><summary><b>Tts (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `tts.home_assistant_cloud` | Home Assistant Cloud | unknown |

</details>




<details><summary><b>Update (12)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `update.alexa_media_player_update` | Alexa Media Player update | off |

| `update.card_mod_update` | card-mod update | off |

| `update.custom_icons_update` | Custom Icons update | off |

| `update.file_editor_update` | File editor Update | off |

| `update.hacs_update` | HACS update | off |

| `update.home_assistant_core_update` | Home Assistant Core Update | on |

| `update.home_assistant_matter_hub_3_0_0_alpha_76_update` | Home-Assistant-Matter-Hub (3.0.0-alpha.76) Update | off |

| `update.home_assistant_operating_system_update` | Home Assistant Operating System Update | off |

| `update.home_assistant_supervisor_update` | Home Assistant Supervisor Update | off |

| `update.matter_server_update` | Matter Server Update | off |

| `update.shelly_device_firmware` | Shelly Device Firmware | off |

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
