_Last Updated: 2026-02-11T23:10:34.017239-06:00_

## 🛠 UI Helpers
Below are the input helpers configured in Home Assistant.





### Boolean
| Entity ID | Name | State | Attributes |
|---|---|---|---|




| `input_boolean.disable_toggle` | **Disable toggle ** | off |  |




| `input_boolean.phone_active` | **Phone active** | on |  |




| `input_boolean.workday_today_toggle` | **Workday Today Toggle** | on |  |




| `input_boolean.workday_toggle_helper` | **General Toggle Helper** | off |  |




| `input_boolean.workday_tomorrow_toggle` | **Workday Tomorrow Toggle** | on |  |









### Datetime
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  


| `input_datetime.alarm` | **Alarm ** | 2025-12-25 00:00:00 | has_date=True, has_time=True |



  


| `input_datetime.home_timestamp` | **Home Timestamp** | 2026-02-11 22:41:10 | has_date=True, has_time=True |



  


| `input_datetime.last_door_open` | **Last Door Open** | 2026-02-11 22:44:31 | has_date=True, has_time=True |



  


| `input_datetime.scheduled_off` | **Scheduled Off** | 1969-12-31 | has_date=True, has_time=False |



  


| `input_datetime.working_override` | **Working Override** | 1969-12-31 | has_date=True, has_time=False |









### Select
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  


| `input_select.speakers` | **Speaker Options** | All Echo (All Alexa Devices) | options=All Echo (All Alexa Devices), Echo Spot (Bedroom), Echo Pop (Bathroom), Echo Dot (Kitchen) |






### Text
| Entity ID | Name | State | Attributes |
|---|---|---|---|




| `input_text.alarm_music` | **Alarm Music** | Ed sheeran |  |




| `input_text.alexa_music_search` | **Alexa Music Search** |  |  |






### Counter
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  


| `counter.counter_helper` | **Counter helper** | 0 | min=, max= |



  


| `counter.door_stuck` | **Door Stuck** | 11 | min=, max= |



  


| `counter.motion_anomaly` | **Motion anomaly** | 1 | min=, max= |






### Timer
| Entity ID | Name | State | Attributes |
|---|---|---|---|



  


| `timer.timer_helper` | **Timer Helper** | idle | duration=0:00:00 |








---

## 🏠 All Entities (By Domain)


<details><summary><b>Automation (15)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `automation.battery_low_automation` | Battery Low Automation | on |

| `automation.bedroom_ceiling_lights_3_set_my_room` | Bedroom Ceiling Lights (3) -> Set My Room | on |

| `automation.door_automation` | Door Automation | on |

| `automation.flic_butttons` | Flic Button | on |

| `automation.goodnight` | Goodnight | on |

| `automation.helper_automation` | Helper Automation | on |

| `automation.hue_dimmer` | Hue Dimmer | on |

| `automation.light_triggers_another_light` | Light Automations | on |

| `automation.living_room_lamp` | Living Room Lamp | on |

| `automation.nightly_github_sync` | Nightly GitHub sync | on |

| `automation.thermostat` | Thermostat | on |

| `automation.washing_machine_dryer` | Washing Machine / Dryer | on |

| `automation.work_attic_temperature_notifications` | Work Attic Temperature Alert | on |

| `automation.work_schedule_automations` | Work Schedule Automations | on |

| `automation.workday_wakeup_new` | Workday Wakeup | on |

</details>




<details><summary><b>Binary_sensor (65)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `binary_sensor.50_onn_roku_tv_headphones_connected` | Bedroom TV Headphones connected | off |

| `binary_sensor.50_onn_roku_tv_supports_airplay` | Bedroom TV Supports AirPlay | on |

| `binary_sensor.50_onn_roku_tv_supports_ethernet` | Bedroom TV Supports Ethernet | on |

| `binary_sensor.50_onn_roku_tv_supports_find_remote` | Bedroom TV Supports find remote | on |

| `binary_sensor.akamatis_presence_sensor_b24c50_moving_target` | Akamatis Presence Sensor b24c50 Moving Target | off |

| `binary_sensor.akamatis_presence_sensor_b24c50_still_target` | Akamatis Presence Sensor b24c50 Still Target | off |

| `binary_sensor.alexa_master_sensor` | Alexa Master Sensor | off |

| `binary_sensor.all_echo_connectivity` | All Echo Connectivity | on |

| `binary_sensor.apartment_presence` | Apartment Presence | on |

| `binary_sensor.bathroom_light_cloud_connection` | Bathroom Light Cloud connection | on |

| `binary_sensor.bathroom_light_overheated` | Bathroom Light Overheated | off |

| `binary_sensor.bathroom_presence` | Bathroom Presence | off |

| `binary_sensor.bed_presence_bb8594_bed_occupied_both` | Bed Pressure Sensor Bed Occupied Both | off |

| `binary_sensor.bed_presence_bb8594_bed_occupied_either` | Bed Pressure Sensor Bed Occupied Either | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_left` | Bed Pressure Sensor Bed Occupied Left | on |

| `binary_sensor.bed_presence_bb8594_bed_occupied_right` | Bed Pressure Sensor Bed Occupied Right | off |

| `binary_sensor.bed_presence_bb8594_status` | Bed Pressure Sensor Status | on |

| `binary_sensor.bedroom_presence` | Everything Presence Lite Occupancy | on |

| `binary_sensor.blake_s_echo_dot_connectivity` | Blake's Echo Dot Connectivity | on |

| `binary_sensor.blake_s_echo_pop_connectivity` | Blake's Echo Pop Connectivity | on |

| `binary_sensor.blake_s_echo_spot_connectivity` | Blake's Echo Spot Connectivity | on |

| `binary_sensor.blake_s_echo_spot_motion` | Motion | unavailable |

| `binary_sensor.closet_light_cloud_connection` | Closet Light Cloud connection | on |

| `binary_sensor.closet_light_overheated` | Closet Light Overheated | off |

| `binary_sensor.closet_motion` | Closet Motion | off |

| `binary_sensor.dryer` | Dryer | off |

| `binary_sensor.echo_dot_active` | Echo Dot Active | off |

| `binary_sensor.echo_pop_active` | Echo Pop Active | off |

| `binary_sensor.echo_spot_active` | Echo Spot Active | off |

| `binary_sensor.everything_presence_lite_922d28_target_1_active` | Everything Presence Lite Target 1 Active | on |

| `binary_sensor.everything_presence_lite_922d28_target_2_active` | Everything Presence Lite Target 2 Active | off |

| `binary_sensor.everything_presence_lite_922d28_target_3_active` | Everything Presence Lite Target 3 Active | off |

| `binary_sensor.everything_presence_lite_922d28_zone_1_occupancy` | Everything Presence Lite Zone 1 Occupancy | off |

| `binary_sensor.everything_presence_lite_922d28_zone_2_occupancy` | Everything Presence Lite Zone 2 Occupancy | off |

| `binary_sensor.everything_presence_lite_922d28_zone_3_occupancy` | Everything Presence Lite Zone 3 Occupancy | off |

| `binary_sensor.everything_presence_lite_922d28_zone_4_occupancy` | Everything Presence Lite Zone 4 Occupancy | off |

| `binary_sensor.everywhere_connectivity` | Connectivity | unavailable |

| `binary_sensor.fan_outlet_cloud_connection` | Fan Outlet Cloud connection | on |

| `binary_sensor.front_door` | Front door | off |

| `binary_sensor.hlk_ld2410_ff00_motion` | Motion | unavailable |

| `binary_sensor.hlk_ld2410_ff00_occupancy` | Occupancy | unavailable |

| `binary_sensor.kitchen_lights_cloud_connection` | Kitchen Lights Cloud connection | on |

| `binary_sensor.kitchen_lights_overheated` | Kitchen Lights Overheated | off |

| `binary_sensor.kitchen_presence` | Aqara FP300 Presence | off |

| `binary_sensor.living_room_ceiling_fan_cloud_connection` | Living Room Ceiling Fan Cloud connection | on |

| `binary_sensor.living_room_ceiling_fan_overheated` | Living Room Ceiling Fan Overheated | off |

| `binary_sensor.living_room_ceiling_lights_cloud_connection` | Living Room Ceiling Lights Cloud connection | on |

| `binary_sensor.living_room_ceiling_lights_overheated` | Living Room Ceiling Lights Overheated | off |

| `binary_sensor.living_room_motion` | Living Room Motion | off |

| `binary_sensor.main_lights_cloud_connection` | Main Lights Cloud connection | on |

| `binary_sensor.philips_rwl020_binary_input` | Hue Dimmer Binary input | off |

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

| `binary_sensor.washing_machine` | Washing Machine | off |

| `binary_sensor.workday_tomorrow_template_sensor` | Workday Tomorrow Template Sensor | on |

</details>




<details><summary><b>Button (22)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `button.aqara_fp300_identify` | Aqara FP300 Identify | unknown |

| `button.aqara_fp300_restart_device` | Aqara FP300 Restart device | unknown |

| `button.aqara_fp300_start_spatial_learning` | Aqara FP300 Start spatial learning | 2025-12-15T04:11:25.804002+00:00 |

| `button.aqara_fp300_start_target_distance_tracking` | Aqara FP300 Start target distance tracking | 2025-12-15T04:09:48.237866+00:00 |

| `button.bed_presence_bb8594_calibrate_left_occupied` | Bed Pressure Sensor Calibrate Left Occupied | 2026-01-26T07:40:19.720153+00:00 |

| `button.bed_presence_bb8594_calibrate_left_unoccupied` | Bed Pressure Sensor Calibrate Left Unoccupied | 2026-01-26T07:38:40.418690+00:00 |

| `button.bed_presence_bb8594_calibrate_right_occupied` | Bed Pressure Sensor Calibrate Right Occupied | 2026-01-26T07:39:46.364113+00:00 |

| `button.bed_presence_bb8594_calibrate_right_unoccupied` | Bed Pressure Sensor Calibrate Right Unoccupied | 2026-01-26T07:38:49.922190+00:00 |

| `button.bed_presence_bb8594_restart` | Bed Pressure Sensor Restart | 2026-01-26T07:21:43.748455+00:00 |

| `button.bedroom_lamp_identify` | Bedroom Lamp Identify | 2025-12-08T08:30:05.569038+00:00 |

| `button.everything_presence_lite_922d28_esp_reboot` | Everything Presence Lite ESP Reboot | unknown |

| `button.everything_presence_lite_922d28_factory_reset_mmwave_sensor` | Everything Presence Lite Factory Reset mmWave Sensor | unknown |

| `button.everything_presence_lite_922d28_reboot_mmwave_sensor` | Everything Presence Lite Reboot mmWave Sensor | unknown |

| `button.govee_to_mqtt_purge_caches` | Purge Caches | unavailable |

| `button.h6098_identify` | Bedroom Tv Backlight Identify | 2026-01-20T04:40:34.514908+00:00 |

| `button.living_room_lamp_identify` | Living Room Lamp Identify | 2025-12-12T05:16:53.886398+00:00 |

| `button.nest_thermostat_identify` | Nest Thermostat Identify | unknown |

| `button.philips_rwl020_identify` | Hue Dimmer Identify | unknown |

| `button.shelly_device_reboot` | Shelly Device Restart | unknown |

| `button.slzb_mr1_core_restart` | SLZB-MR1 Core restart | unknown |

| `button.slzb_mr1_zigbee_restart` | SLZB-MR1 Zigbee restart | unknown |

| `button.third_reality_inc_3rths0224z_identify` | Temp & Humidity Identify | unknown |

</details>




<details><summary><b>Climate (4)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `climate.a_expansion_attic` | A expansion attic | off |

| `climate.c_expansion_attic` | C Expansion attic | off |

| `climate.d_expansion_attic` | D expansion attic | off |

| `climate.nest_thermostat` | Nest Thermostat | heat |

</details>




<details><summary><b>Conversation (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `conversation.home_assistant` | Home Assistant | unknown |

</details>






<details><summary><b>Device_tracker (31)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `device_tracker.blakes_iphone` | Blakes iPhone | home |

| `device_tracker.bleperipheralapp_4840` | bleperipheralapp 4840 | unavailable |

| `device_tracker.ipad` | iPad | home |

| `device_tracker.rachels_phone` | Rachels Phone | Rachel’s Home |

| `device_tracker.rivian_phone_key_2060` | rivian phone key 2060 | unavailable |

| `device_tracker.rivian_phone_key_3a87` | rivian phone key 3a87 | unavailable |

| `device_tracker.rivian_phone_key_3d22` | rivian phone key 3d22 | unavailable |

| `device_tracker.rivian_phone_key_714f` | rivian phone key 714f | unavailable |

| `device_tracker.rivian_phone_key_7f97` | rivian phone key 7f97 | unavailable |

| `device_tracker.rivian_phone_key_9e27` | rivian phone key 9e27 | unavailable |

| `device_tracker.rivian_phone_key_c28f` | rivian phone key c28f | unavailable |

| `device_tracker.rivian_phone_key_ec7f` | rivian phone key ec7f | unavailable |

| `device_tracker.rivian_phone_key_f289` | rivian phone key f289 | unavailable |

| `device_tracker.rivian_sensor_1_d795` | rivian sensor 1 d795 | unavailable |

| `device_tracker.rivian_sensor_2_eca1` | rivian sensor 2 eca1 | unavailable |

| `device_tracker.rivian_sensor_3_aa31` | rivian sensor 3 aa31 | unavailable |

| `device_tracker.rivian_sensor_4_0a2c` | rivian sensor 4 0a2c | unavailable |

| `device_tracker.rivian_sensor_4_14f4` | rivian sensor 4 14f4 | unavailable |

| `device_tracker.s266657243954c04bc_20b2` | S266657243954c04bC 20B2 | not_home |

| `device_tracker.s2a274671f938dadcc_fde0` | S2a274671f938dadcC FDE0 | not_home |

| `device_tracker.s5763cf7cddb7eef9c_7c8d` | s5763cf7cddb7eef9c 7c8d | unavailable |

| `device_tracker.s58cdfccea0786690c_d4a2` | S58cdfccea0786690C D4A2 | not_home |

| `device_tracker.s97ba9994382d840bc_e454` | s97ba9994382d840bc e454 | unavailable |

| `device_tracker.sbc4f3bc21b66bf73c_555f` | sbc4f3bc21b66bf73c 555f | unavailable |

| `device_tracker.sc88d2596603604dcc_ffeb` | sc88d2596603604dcc ffeb | unavailable |

| `device_tracker.scd0ed4bcbf3abdf0c_652d` | scd0ed4bcbf3abdf0c 652d | unavailable |

| `device_tracker.sd78d075d9fbca645c_788d` | sd78d075d9fbca645c 788d | unavailable |

| `device_tracker.sdf631c51986d49cdc_295e` | sdf631c51986d49cdc 295e | unavailable |

| `device_tracker.sfb57741ef118e66ec_4652` | Sfb57741ef118e66eC 4652 | not_home |

| `device_tracker.telematic_575072_ced2` | telematic 575072 ced2 | unavailable |

| `device_tracker.xkglowrgb_0451` | xkglowrgb 0451 | unavailable |

</details>




<details><summary><b>Event (3)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `event.backup_automatic_backup` | Backup Automatic backup | 2026-02-11T11:30:43.881+00:00 |

| `event.bthome_sensor_3370_button` | Motion 1 - Shelly Button | 2025-10-19T05:15:17.292+00:00 |

| `event.front_door_sensor_button` | Front Door Sensor Button | 2025-12-14T04:27:51.375+00:00 |

</details>




<details><summary><b>Fan (3)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `fan.bedroom_ceiling_fan` | Bedroom Ceiling Fan | off |

| `fan.bedroom_fan` | Fan | off |

| `fan.living_room_ceiling_fan` | Living Room Ceiling Fan | off |

</details>












<details><summary><b>Light (10)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `light.bathroom_light` | Bathroom Light | off |

| `light.bedroom_ceiling_lights` | Bedroom Ceiling Lights | on |

| `light.bedroom_lamp` | Bedroom Lamp | on |

| `light.bedroom_tv_backlight` | Bedroom Tv Backlight | off |

| `light.closet_light` | Closet Light | off |

| `light.everything_presence_lite_922d28_esp32_led` | Everything Presence Lite ESP32 LED | off |

| `light.kitchen_lights` | Kitchen Lights | off |

| `light.living_room_ceiling_lights` | Living Room Ceiling Lights | off |

| `light.living_room_lamp` | Living Room Lamp | on |

| `light.main_lights` | Main Lights | off |

</details>




<details><summary><b>Media_player (6)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `media_player.all_echo` | All Echo | paused |

| `media_player.bedroom_tv` | Bedroom Tv | idle |

| `media_player.blake_s_echo_dot` | Blake's Echo Dot | paused |

| `media_player.blake_s_echo_pop` | Blake's Echo Pop | paused |

| `media_player.blake_s_echo_spot` | Blake's Echo Spot | paused |

| `media_player.living_room_tv` | Living Room TV | unavailable |

</details>




<details><summary><b>Notify (8)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `notify.all_echo_announce` | All Echo Announce | 2026-01-23T15:35:19.458008+00:00 |

| `notify.blake_s_echo_dot_announce` | Blake's Echo Dot Announce | unknown |

| `notify.blake_s_echo_dot_speak` | Blake's Echo Dot Speak | unknown |

| `notify.blake_s_echo_pop_announce` | Blake's Echo Pop Announce | unknown |

| `notify.blake_s_echo_pop_speak` | Blake's Echo Pop Speak | unknown |

| `notify.blake_s_echo_spot_announce` | Blake's Echo Spot Announce | 2026-02-04T05:23:04.417028+00:00 |

| `notify.blake_s_echo_spot_speak` | Blake's Echo Spot Speak | 2026-02-10T15:07:17.975699+00:00 |

| `notify.everywhere_announce` | Announce | unavailable |

</details>




<details><summary><b>Number (83)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `number.akamatis_presence_sensor_b24c50_g0_move_threshold` | Akamatis Presence Sensor b24c50 g0 move threshold | 50.0 |

| `number.akamatis_presence_sensor_b24c50_g0_still_threshold` | Akamatis Presence Sensor b24c50 g0 still threshold | 44.0 |

| `number.akamatis_presence_sensor_b24c50_g1_move_threshold` | Akamatis Presence Sensor b24c50 g1 move threshold | 50.0 |

| `number.akamatis_presence_sensor_b24c50_g1_still_threshold` | Akamatis Presence Sensor b24c50 g1 still threshold | 51.0 |

| `number.akamatis_presence_sensor_b24c50_g2_move_threshold` | Akamatis Presence Sensor b24c50 g2 move threshold | 51.0 |

| `number.akamatis_presence_sensor_b24c50_g2_still_threshold` | Akamatis Presence Sensor b24c50 g2 still threshold | 40.0 |

| `number.akamatis_presence_sensor_b24c50_g3_move_threshold` | Akamatis Presence Sensor b24c50 g3 move threshold | 64.0 |

| `number.akamatis_presence_sensor_b24c50_g3_still_threshold` | Akamatis Presence Sensor b24c50 g3 still threshold | 44.0 |

| `number.akamatis_presence_sensor_b24c50_g4_move_threshold` | Akamatis Presence Sensor b24c50 g4 move threshold | 66.0 |

| `number.akamatis_presence_sensor_b24c50_g4_still_threshold` | Akamatis Presence Sensor b24c50 g4 still threshold | 51.0 |

| `number.akamatis_presence_sensor_b24c50_g5_move_threshold` | Akamatis Presence Sensor b24c50 g5 move threshold | 60.0 |

| `number.akamatis_presence_sensor_b24c50_g5_still_threshold` | Akamatis Presence Sensor b24c50 g5 still threshold | 71.0 |

| `number.akamatis_presence_sensor_b24c50_g6_move_threshold` | Akamatis Presence Sensor b24c50 g6 move threshold | 63.0 |

| `number.akamatis_presence_sensor_b24c50_g6_still_threshold` | Akamatis Presence Sensor b24c50 g6 still threshold | 61.0 |

| `number.akamatis_presence_sensor_b24c50_g7_move_threshold` | Akamatis Presence Sensor b24c50 g7 move threshold | 54.0 |

| `number.akamatis_presence_sensor_b24c50_g7_still_threshold` | Akamatis Presence Sensor b24c50 g7 still threshold | 53.0 |

| `number.akamatis_presence_sensor_b24c50_g8_move_threshold` | Akamatis Presence Sensor b24c50 g8 move threshold | 57.0 |

| `number.akamatis_presence_sensor_b24c50_g8_still_threshold` | Akamatis Presence Sensor b24c50 g8 still threshold | 53.0 |

| `number.akamatis_presence_sensor_b24c50_light_threshold` | Akamatis Presence Sensor b24c50 light threshold | 128.0 |

| `number.akamatis_presence_sensor_b24c50_max_move_distance_gate` | Akamatis Presence Sensor b24c50 max move distance gate | 8.0 |

| `number.akamatis_presence_sensor_b24c50_max_still_distance_gate` | Akamatis Presence Sensor b24c50 max still distance gate | 8.0 |

| `number.akamatis_presence_sensor_b24c50_timeout` | Akamatis Presence Sensor b24c50 timeout | 5.0 |

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

| `number.bed_presence_bb8594_left_occupied_pressure` | Bed Pressure Sensor Left Occupied Pressure | 91.0 |

| `number.bed_presence_bb8594_left_trigger_pressure` | Bed Pressure Sensor Left Trigger Pressure | 87.0 |

| `number.bed_presence_bb8594_left_unoccupied_pressure` | Bed Pressure Sensor Left Unoccupied Pressure | 75.0 |

| `number.bed_presence_bb8594_right_occupied_pressure` | Bed Pressure Sensor Right Occupied Pressure | 92.0 |

| `number.bed_presence_bb8594_right_trigger_pressure` | Bed Pressure Sensor Right Trigger Pressure | 91.5 |

| `number.bed_presence_bb8594_right_unoccupied_pressure` | Bed Pressure Sensor Right Unoccupied Pressure | 90.0 |

| `number.bedroom_lamp_start_up_color_temperature` | Bedroom Lamp Start-up color temperature | 366 |

| `number.bedroom_lamp_start_up_current_level` | Bedroom Lamp Start-up current level | 255 |

| `number.closet_light_turn_off_in` | Closet Light Turn off in | 120 |

| `number.everything_presence_lite_922d28_illuminance_offset` | Everything Presence Lite Illuminance Offset | 0.0 |

| `number.everything_presence_lite_922d28_installation_angle` | Everything Presence Lite Installation Angle | -43.0 |

| `number.everything_presence_lite_922d28_max_distance` | Everything Presence Lite Max Distance | 600.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_begin_x` | Everything Presence Lite Occupancy Mask 1 Begin X | 400.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_begin_y` | Everything Presence Lite Occupancy Mask 1 Begin Y | -200.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_end_x` | Everything Presence Lite Occupancy Mask 1 End X | 700.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_1_end_y` | Everything Presence Lite Occupancy Mask 1 End Y | 200.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_begin_x` | Everything Presence Lite Occupancy Mask 2 Begin X | 0.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_begin_y` | Everything Presence Lite Occupancy Mask 2 Begin Y | 0.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_end_x` | Everything Presence Lite Occupancy Mask 2 End X | 0.0 |

| `number.everything_presence_lite_922d28_occupancy_mask_2_end_y` | Everything Presence Lite Occupancy Mask 2 End Y | 0.0 |

| `number.everything_presence_lite_922d28_occupancy_off_delay` | Everything Presence Lite Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_stale_target_reset_timeout` | Everything Presence Lite Stale Target Reset Timeout | 60.0 |

| `number.everything_presence_lite_922d28_zone_1_begin_x` | Everything Presence Lite Zone 1 Begin X | 1700.0 |

| `number.everything_presence_lite_922d28_zone_1_begin_y` | Everything Presence Lite Zone 1 Begin Y | 600.0 |

| `number.everything_presence_lite_922d28_zone_1_end_x` | Everything Presence Lite Zone 1 End X | 3200.0 |

| `number.everything_presence_lite_922d28_zone_1_end_y` | Everything Presence Lite Zone 1 End Y | 2500.0 |

| `number.everything_presence_lite_922d28_zone_1_occupancy_off_delay` | Everything Presence Lite Zone 1 Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_zone_2_begin_x` | Everything Presence Lite Zone 2 Begin X | 0.0 |

| `number.everything_presence_lite_922d28_zone_2_begin_y` | Everything Presence Lite Zone 2 Begin Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_2_end_x` | Everything Presence Lite Zone 2 End X | 0.0 |

| `number.everything_presence_lite_922d28_zone_2_end_y` | Everything Presence Lite Zone 2 End Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_2_occupancy_off_delay` | Everything Presence Lite Zone 2 Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_zone_3_begin_x` | Everything Presence Lite Zone 3 Begin X | 0.0 |

| `number.everything_presence_lite_922d28_zone_3_begin_y` | Everything Presence Lite Zone 3 Begin Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_3_end_x` | Everything Presence Lite Zone 3 End X | 0.0 |

| `number.everything_presence_lite_922d28_zone_3_end_y` | Everything Presence Lite Zone 3 End Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_3_occupancy_off_delay` | Everything Presence Lite Zone 3 Occupancy Off Delay | 15.0 |

| `number.everything_presence_lite_922d28_zone_4_begin_x` | Everything Presence Lite Zone 4 Begin X | 0.0 |

| `number.everything_presence_lite_922d28_zone_4_begin_y` | Everything Presence Lite Zone 4 Begin Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_4_end_x` | Everything Presence Lite Zone 4 End X | 0.0 |

| `number.everything_presence_lite_922d28_zone_4_end_y` | Everything Presence Lite Zone 4 End Y | 0.0 |

| `number.everything_presence_lite_922d28_zone_4_occupancy_off_delay` | Everything Presence Lite Zone 4 Occupancy Off Delay | 15.0 |

| `number.kitchen_lights_turn_off_in` | Kitchen Lights Turn off in | 120 |

| `number.living_room_ceiling_fan_turn_off_in` | Living Room Ceiling Fan Turn off in | 120 |

| `number.living_room_ceiling_lights_turn_off_in` | Living Room Ceiling Lights Turn off in | 120 |

| `number.living_room_lamp_start_up_current_level` | Living Room Lamp Start-up current level | 254 |

| `number.main_lights_turn_off_in` | Main Lights Turn off in | 120 |

| `number.motion_2_detection_interval` | Motion 2 - Third Reality Detection interval | 30 |

| `number.third_reality_inc_3rths0224z_humidity_offset` | Temp & Humidity Humidity offset | unknown |

| `number.third_reality_inc_3rths0224z_temperature_offset` | Temp & Humidity Temperature offset | unknown |

</details>




<details><summary><b>Person (2)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `person.blake_foster` | Blake Foster | home |

| `person.rachel` | Rachel | Rachel’s Home |

</details>




<details><summary><b>Remote (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `remote.bedroom_tv` | Bedroom Tv Remote | on |

</details>




<details><summary><b>Scene (13)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `scene.all_lights` | All Lights | 2026-02-12T04:44:31.077092+00:00 |

| `scene.all_lights_off` | All Lights Off | 2025-12-27T04:11:14.019092+00:00 |

| `scene.all_off` | All Off | 2026-02-12T04:11:00.338482+00:00 |

| `scene.bedroom_lights_off` | Bedroom Lights Off | 2026-02-12T01:34:14.759721+00:00 |

| `scene.dimmed` | Dimmed | 2026-01-31T12:43:31.087739+00:00 |

| `scene.full_lamp` | Full Lamp | 2026-02-12T04:44:31.285831+00:00 |

| `scene.goodnight_scene` | Goodnight | 2026-02-12T03:39:24.970207+00:00 |

| `scene.im_awake` | I’m Awake | 2025-12-02T12:31:03.745110+00:00 |

| `scene.lights_off_except_bedroom` | Lights off except bedroom | 2026-02-12T04:57:14.920988+00:00 |

| `scene.night_light` | Night Light | 2025-09-26T00:17:04.739409+00:00 |

| `scene.set_my_room` | Set My Room | 2026-02-12T03:43:02.302455+00:00 |

| `scene.thermostat_away` | Thermostat Away | 2026-02-11T14:59:19.400032+00:00 |

| `scene.thermostat_ideal_evening` | Thermostat 68/70 | 2025-11-28T11:14:37.942932+00:00 |

</details>




<details><summary><b>Script (8)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `script.alexa_music` | Alexa Music | off |

| `script.find_my_phone` | Find My Phone | off |

| `script.find_remote` | Find Remote | off |

| `script.push_ha_info_to_github_create_ai_zip_file_now` | Push Ha Info to GitHub & Create AI Zip File | on |

| `script.roku_backlight` | Roku Backlight | off |

| `script.set_date_to_today` | Scheduled Off & Working Override dashboard script | off |

| `script.set_room_2` | Set Room | off |

| `script.temporary_thermostat_adjustment` | Temporary Thermostat Adjustment | off |

</details>




<details><summary><b>Select (18)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `select.akamatis_presence_sensor_b24c50_baud_rate` | Akamatis Presence Sensor b24c50 baud rate | 256000 |

| `select.akamatis_presence_sensor_b24c50_distance_resolution` | Akamatis Presence Sensor b24c50 distance resolution | 0.2m |

| `select.akamatis_presence_sensor_b24c50_light_function` | Akamatis Presence Sensor b24c50 light function | off |

| `select.akamatis_presence_sensor_b24c50_out_pin_level` | Akamatis Presence Sensor b24c50 out pin level | low |

| `select.aqara_fp300_humidity_reporting_mode` | Aqara FP300 Humidity reporting mode | THRESHOLD AND INTERVAL |

| `select.aqara_fp300_light_reporting_mode` | Aqara FP300 Light reporting mode | THRESHOLD AND INTERVAL |

| `select.aqara_fp300_light_sampling` | Aqara FP300 Light sampling | CUSTOM |

| `select.aqara_fp300_motion_sensitivity` | Aqara FP300 Motion sensitivity | HIGH |

| `select.aqara_fp300_presence_detection_options` | Aqara FP300 Presence detection options | BOTH |

| `select.aqara_fp300_temp_humidity_sampling` | Aqara FP300 Temp & humidity sampling | OFF |

| `select.aqara_fp300_temperature_reporting_mode` | Aqara FP300 Temperature reporting mode | THRESHOLD AND INTERVAL |

| `select.bed_presence_bb8594_bluetooth_scanner_mode` | Bed Pressure Sensor Bluetooth Scanner Mode | Passive |

| `select.bed_presence_bb8594_response_speed` | Bed Pressure Sensor Response Speed | Slow |

| `select.bedroom_lamp_start_up_behavior` | Bedroom Lamp Start-up behavior | PreviousValue |

| `select.everything_presence_lite_922d28_extra_entities_update` | Everything Presence Lite Extra entities update | Every update |

| `select.everything_presence_lite_922d28_tracking_behaviour` | Everything Presence Lite Tracking Behaviour | Above + Speed and Resolution |

| `select.everything_presence_lite_922d28_update_speed` | Everything Presence Lite Update speed | Normal (0.3s) |

| `select.living_room_lamp_start_up_behavior` | Living Room Lamp Start-up behavior | PreviousValue |

</details>




<details><summary><b>Sensor (244)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `sensor.50_onn_roku_tv_active_app` | Bedroom TV Active app | YouTube |

| `sensor.50_onn_roku_tv_active_app_id` | Bedroom TV Active app ID | 837 |

| `sensor.a_expansion_attic_humidity` | A expansion attic Humidity | 19 |

| `sensor.a_expansion_attic_temperature` | A expansion attic Temperature | 85.46 |

| `sensor.akamatis_presence_sensor_b24c50_detection_distance` | Akamatis Presence Sensor b24c50 Detection Distance | 59.4488188976378 |

| `sensor.akamatis_presence_sensor_b24c50_g0_move_energy` | Akamatis Presence Sensor b24c50 g0 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g0_still_energy` | Akamatis Presence Sensor b24c50 g0 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g1_move_energy` | Akamatis Presence Sensor b24c50 g1 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g1_still_energy` | Akamatis Presence Sensor b24c50 g1 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g2_move_energy` | Akamatis Presence Sensor b24c50 g2 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g2_still_energy` | Akamatis Presence Sensor b24c50 g2 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g3_move_energy` | Akamatis Presence Sensor b24c50 g3 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g3_still_energy` | Akamatis Presence Sensor b24c50 g3 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g4_move_energy` | Akamatis Presence Sensor b24c50 g4 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g4_still_energy` | Akamatis Presence Sensor b24c50 g4 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g5_move_energy` | Akamatis Presence Sensor b24c50 g5 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g5_still_energy` | Akamatis Presence Sensor b24c50 g5 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g6_move_energy` | Akamatis Presence Sensor b24c50 g6 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g6_still_energy` | Akamatis Presence Sensor b24c50 g6 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g7_move_energy` | Akamatis Presence Sensor b24c50 g7 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g7_still_energy` | Akamatis Presence Sensor b24c50 g7 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g8_move_energy` | Akamatis Presence Sensor b24c50 g8 move energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_g8_still_energy` | Akamatis Presence Sensor b24c50 g8 still energy | unknown |

| `sensor.akamatis_presence_sensor_b24c50_light` | Akamatis Presence Sensor b24c50 light | unknown |

| `sensor.akamatis_presence_sensor_b24c50_move_energy` | Akamatis Presence Sensor b24c50 Move Energy | 0.0 |

| `sensor.akamatis_presence_sensor_b24c50_moving_distance` | Akamatis Presence Sensor b24c50 Moving Distance | 62.5984251968504 |

| `sensor.akamatis_presence_sensor_b24c50_presence_sensor_mac_address` | Akamatis Presence Sensor b24c50 presence sensor mac address | BC:AC:90:8F:FF:00 |

| `sensor.akamatis_presence_sensor_b24c50_presence_sensor_version` | Akamatis Presence Sensor b24c50 presence sensor version | 2.44.25070917 |

| `sensor.akamatis_presence_sensor_b24c50_still_distance` | Akamatis Presence Sensor b24c50 Still Distance | 62.5984251968504 |

| `sensor.akamatis_presence_sensor_b24c50_still_energy` | Akamatis Presence Sensor b24c50 Still Energy | 100.0 |

| `sensor.all_echo_next_alarm` | Next alarm | unavailable |

| `sensor.all_echo_next_reminder` | Next reminder | unavailable |

| `sensor.all_echo_next_timer` | Next timer | unavailable |

| `sensor.apartment_humidity` | Apartment Humidity | 34 |

| `sensor.apartment_temperature` | Apartment Temperature | 69.62 |

| `sensor.aqara_fp300_battery` | Aqara FP300 Battery | 100.0 |

| `sensor.aqara_fp300_humidity` | Aqara FP300 Humidity | 30.0 |

| `sensor.aqara_fp300_illuminance` | Aqara FP300 Illuminance | 0 |

| `sensor.aqara_fp300_target_distance` | Aqara FP300 Target distance | unknown |

| `sensor.aqara_fp300_temperature` | Aqara FP300 Temperature | 71.438 |

| `sensor.backup_backup_manager_state` | Backup Backup Manager state | idle |

| `sensor.backup_last_attempted_automatic_backup` | Backup Last attempted automatic backup | 2026-02-11T11:26:35+00:00 |

| `sensor.backup_last_successful_automatic_backup` | Backup Last successful automatic backup | 2026-02-11T11:30:43+00:00 |

| `sensor.backup_next_scheduled_automatic_backup` | Backup Next scheduled automatic backup | 2026-02-12T11:19:15+00:00 |

| `sensor.bathroom_humidity` | Bathroom Humidity | 31.89 |

| `sensor.bathroom_humidity_derivative` | Bathroom Humidity Derivative | -0.0 |

| `sensor.bathroom_light_auto_off_at` | Bathroom Light Auto-off at | unknown |

| `sensor.bathroom_light_signal_level` | Bathroom Light Signal level | 3 |

| `sensor.bathroom_temperature` | Bathroom Temperature | 70.826 |

| `sensor.bed_presence_bb8594_calibrated_left_pressure` | Bed Pressure Sensor Calibrated Left Pressure | 100.0 |

| `sensor.bed_presence_bb8594_calibrated_right_pressure` | Bed Pressure Sensor Calibrated Right Pressure | 0.0 |

| `sensor.bed_presence_bb8594_left_pressure` | Bed Pressure Sensor Left Pressure | 94.4695892333984 |

| `sensor.bed_presence_bb8594_right_pressure` | Bed Pressure Sensor Right Pressure | 83.2924194335938 |

| `sensor.bed_presence_bb8594_uptime` | Bed Pressure Sensor Uptime | 1225076.25 |

| `sensor.bed_presence_bb8594_wifi_signal_db` | Bed Pressure Sensor WiFi Signal dB | -45.0 |

| `sensor.bed_presence_bb8594_wifi_signal_percent` | Bed Pressure Sensor WiFi Signal Percent | 100.0 |

| `sensor.bedroom_ceiling_fan_energy_consumed` | Bedroom Ceiling Fan Energy consumed | 12.430551 |

| `sensor.blake_foster30_gmail_com_total_available_storage` | blake.foster30@gmail.com Total available storage | 2048.0 |

| `sensor.blake_foster30_gmail_com_used_storage` | blake.foster30@gmail.com Used storage | 265.378271625377 |

| `sensor.blake_foster30_gmail_com_vacation_end_date` | blake.foster30@gmail.com Vacation end date | unknown |

| `sensor.blake_s_echo_dot_illuminance` | Blake's Echo Dot Illuminance | 0.0 |

| `sensor.blake_s_echo_dot_next_alarm` | Blake's Echo Dot next Alarm | unavailable |

| `sensor.blake_s_echo_dot_next_alarm_2` | Blake's Echo Dot Next alarm | unavailable |

| `sensor.blake_s_echo_dot_next_alarm_3` | Blake's Echo Dot Next alarm | unknown |

| `sensor.blake_s_echo_dot_next_reminder` | Blake's Echo Dot next Reminder | unavailable |

| `sensor.blake_s_echo_dot_next_reminder_2` | Blake's Echo Dot Next reminder | unavailable |

| `sensor.blake_s_echo_dot_next_reminder_3` | Blake's Echo Dot Next reminder | unknown |

| `sensor.blake_s_echo_dot_next_timer` | Blake's Echo Dot next Timer | unavailable |

| `sensor.blake_s_echo_dot_next_timer_2` | Blake's Echo Dot Next timer | unavailable |

| `sensor.blake_s_echo_dot_next_timer_3` | Blake's Echo Dot Next timer | unknown |

| `sensor.blake_s_echo_pop_next_alarm` | Blake's Echo Pop next Alarm | unavailable |

| `sensor.blake_s_echo_pop_next_alarm_2` | Blake's Echo Pop Next alarm | unavailable |

| `sensor.blake_s_echo_pop_next_alarm_3` | Blake's Echo Pop Next alarm | unknown |

| `sensor.blake_s_echo_pop_next_reminder` | Blake's Echo Pop next Reminder | unavailable |

| `sensor.blake_s_echo_pop_next_reminder_2` | Blake's Echo Pop Next reminder | unavailable |

| `sensor.blake_s_echo_pop_next_reminder_3` | Blake's Echo Pop Next reminder | unknown |

| `sensor.blake_s_echo_pop_next_timer` | Blake's Echo Pop next Timer | unavailable |

| `sensor.blake_s_echo_pop_next_timer_2` | Blake's Echo Pop Next timer | unavailable |

| `sensor.blake_s_echo_pop_next_timer_3` | Blake's Echo Pop Next timer | unknown |

| `sensor.blake_s_echo_spot_illuminance` | Blake's Echo Spot Illuminance | 2.0 |

| `sensor.blake_s_echo_spot_next_alarm` | Blake's Echo Spot Next alarm | unavailable |

| `sensor.blake_s_echo_spot_next_alarm_2` | Blake's Echo Spot next Alarm | unavailable |

| `sensor.blake_s_echo_spot_next_alarm_3` | Blake's Echo Spot Next alarm | unknown |

| `sensor.blake_s_echo_spot_next_reminder` | Blake's Echo Spot Next reminder | unavailable |

| `sensor.blake_s_echo_spot_next_reminder_2` | Blake's Echo Spot next Reminder | unavailable |

| `sensor.blake_s_echo_spot_next_reminder_3` | Blake's Echo Spot Next reminder | unknown |

| `sensor.blake_s_echo_spot_next_timer` | Blake's Echo Spot Next timer | unavailable |

| `sensor.blake_s_echo_spot_next_timer_2` | Blake's Echo Spot next Timer | unavailable |

| `sensor.blake_s_echo_spot_next_timer_3` | Blake's Echo Spot Next timer | unknown |

| `sensor.blakes_iphone_app_version` | Blakes iPhone App Version | 2026.1.1 |

| `sensor.blakes_iphone_battery_level` | Blakes iPhone Battery Level | 95 |

| `sensor.blakes_iphone_battery_state` | Blakes iPhone Battery State | Charging |

| `sensor.blakes_iphone_geocoded_location` | Blakes iPhone Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.blakes_iphone_ssid` | Blakes iPhone SSID | ATTEPISyDS |

| `sensor.bleperipheralapp_4840_estimated_distance` | Estimated distance | unavailable |

| `sensor.bthome_sensor_3370_battery` | Motion 1 - Shelly Battery | 100 |

| `sensor.bthome_sensor_3370_illuminance` | Motion 1 - Shelly Illuminance | 51.0 |

| `sensor.bthome_sensor_3370_packet_id` | Motion 1 - Shelly Packet Id | 13 |

| `sensor.bthome_sensor_3370_signal_strength` | Motion 1 - Shelly Signal Strength | -55 |

| `sensor.c_expansion_attic_humidity` | C Expansion attic Humidity | 23 |

| `sensor.c_expansion_attic_temperature` | C Expansion attic Temperature | 79.88 |

| `sensor.closet_light_auto_off_at` | Closet Light Auto-off at | unknown |

| `sensor.closet_light_signal_level` | Closet Light Signal level | 3 |

| `sensor.d_expansion_attic_humidity` | D expansion attic Humidity | 15 |

| `sensor.d_expansion_attic_temperature` | D expansion attic Temperature | 94.1 |

| `sensor.everything_presence_lite_922d28_illuminance` | Everything Presence Lite Illuminance | 26.2598400115967 |

| `sensor.everything_presence_lite_922d28_mmwave_firmware` | Everything Presence Lite mmWave Firmware | V2.04 |

| `sensor.everything_presence_lite_922d28_occupancy_mask_1_target_count` | Everything Presence Lite Occupancy Mask 1 Target Count | 0.0 |

| `sensor.everything_presence_lite_922d28_occupancy_mask_2_target_count` | Everything Presence Lite Occupancy Mask 2 Target Count | 0.0 |

| `sensor.everything_presence_lite_922d28_target_1_angle` | Everything Presence Lite Target 1 Angle | 1.49319899082184 |

| `sensor.everything_presence_lite_922d28_target_1_distance` | Everything Presence Lite Target 1 Distance | 120.867814191683 |

| `sensor.everything_presence_lite_922d28_target_1_resolution` | Everything Presence Lite Target 1 Resolution | 14.1732283464567 |

| `sensor.everything_presence_lite_922d28_target_1_speed` | Everything Presence Lite Target 1 Speed | 0.0 |

| `sensor.everything_presence_lite_922d28_target_1_x` | Everything Presence Lite Target 1 X | -84.6850393700787 |

| `sensor.everything_presence_lite_922d28_target_1_y` | Everything Presence Lite Target 1 Y | 86.1811023622047 |

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

| `sensor.everything_presence_lite_zone_1_target_count` | Everything Presence Lite Zone 1 Target Count | 0.0 |

| `sensor.everywhere_next_alarm` | Next alarm | unavailable |

| `sensor.everywhere_next_reminder` | Next reminder | unavailable |

| `sensor.everywhere_next_timer` | Next timer | unavailable |

| `sensor.front_door_sensor_battery` | Front Door Sensor Battery | 91 |

| `sensor.front_door_sensor_illuminance` | Front Door Sensor Illuminance | 21.0 |

| `sensor.front_door_sensor_rotation` | Front Door Sensor Rotation | 0.0 |

| `sensor.govee_to_mqtt_version` | Version | unavailable |

| `sensor.h6098_current_switch_position` | Bedroom Tv Backlight Current switch position | 0 |

| `sensor.ipad_app_version` | iPad App Version | 2026.1.1 |

| `sensor.ipad_battery_level` | iPad Battery Level | 100 |

| `sensor.ipad_battery_state` | iPad Battery State | Full |

| `sensor.ipad_geocoded_location` | iPad Geocoded Location | 1109 Watermark Dr
O'Fallon MO 63368
United States |

| `sensor.ipad_ssid` | iPad SSID | Not Connected |

| `sensor.kitchen_lights_auto_off_at` | Kitchen Lights Auto-off at | unknown |

| `sensor.kitchen_lights_signal_level` | Kitchen Lights Signal level | 3 |

| `sensor.living_room_ceiling_fan_auto_off_at` | Living Room Ceiling Fan Auto-off at | unknown |

| `sensor.living_room_ceiling_fan_signal_level` | Living Room Ceiling Fan Signal level | 3 |

| `sensor.living_room_ceiling_lights_auto_off_at` | Living Room Ceiling Lights Auto-off at | unknown |

| `sensor.living_room_ceiling_lights_signal_level` | Living Room Ceiling Lights Signal level | 3 |

| `sensor.main_lights_auto_off_at` | Main Lights Auto-off at | unknown |

| `sensor.main_lights_current` | Main Lights Current | 0.01 |

| `sensor.main_lights_current_consumption` | Main Lights Current consumption | 0.0 |

| `sensor.main_lights_signal_level` | Main Lights Signal level | 3 |

| `sensor.main_lights_this_month_s_consumption` | Main Lights This month's consumption | 0.784 |

| `sensor.main_lights_today_s_consumption` | Main Lights Today's consumption | 0.04 |

| `sensor.main_lights_voltage` | Main Lights Voltage | 122.9 |

| `sensor.motion_2_battery` | Motion 2 - Third Reality Battery | 100.0 |

| `sensor.nest_temperature_sensor_a_expansion_attic_sensor_battery_level` | Nest Temperature Sensor (A expansion attic sensor) Battery Level | unavailable |

| `sensor.nest_temperature_sensor_a_expansion_attic_sensor_temperature` | Nest Temperature Sensor (A expansion attic sensor) Temperature | unavailable |

| `sensor.nest_temperature_sensor_d_expansion_attic_sensor_battery_level` | Nest Temperature Sensor (D expansion attic sensor) Battery Level | unavailable |

| `sensor.nest_temperature_sensor_d_expansion_attic_sensor_temperature` | Nest Temperature Sensor (D expansion attic sensor) Temperature | unavailable |

| `sensor.nest_temperature_sensor_stairwell_g_battery_level` | Nest Temperature Sensor (Stairwell G) Battery Level | unavailable |

| `sensor.nest_temperature_sensor_stairwell_g_temperature` | Nest Temperature Sensor (Stairwell G) Temperature | unavailable |

| `sensor.nest_thermostat_temperature` | Nest Thermostat Temperature | 69.602 |

| `sensor.openweathermap_cloud_coverage_2` | OpenWeatherMap Cloud coverage | 99 |

| `sensor.openweathermap_condition_2` | OpenWeatherMap Condition | cloudy |

| `sensor.openweathermap_dew_point_2` | OpenWeatherMap Dew point temperature | 25.232 |

| `sensor.openweathermap_feels_like_temperature_2` | OpenWeatherMap Apparent temperature | 33.188 |

| `sensor.openweathermap_humidity_2` | OpenWeatherMap Humidity | 63 |

| `sensor.openweathermap_precipitation_kind_2` | OpenWeatherMap Precipitation kind | None |

| `sensor.openweathermap_pressure_2` | OpenWeatherMap Pressure | 14.8808725238612 |

| `sensor.openweathermap_rain_2` | OpenWeatherMap Rain intensity | 0.0 |

| `sensor.openweathermap_snow_2` | OpenWeatherMap Snow intensity | 0.0 |

| `sensor.openweathermap_temperature_2` | OpenWeatherMap Temperature | 35.69 |

| `sensor.openweathermap_uv_index_2` | OpenWeatherMap UV index | 0 |

| `sensor.openweathermap_visibility_2` | OpenWeatherMap Visibility | 32808.3989501312 |

| `sensor.openweathermap_weather_2` | OpenWeatherMap Weather | overcast clouds |

| `sensor.openweathermap_weather_code_2` | OpenWeatherMap Weather code | 804 |

| `sensor.openweathermap_wind_bearing_2` | OpenWeatherMap Wind direction | 103 |

| `sensor.openweathermap_wind_gust_2` | OpenWeatherMap Wind gust speed | 3.17644953471725 |

| `sensor.openweathermap_wind_speed_2` | OpenWeatherMap Wind speed | 3.24355762347888 |

| `sensor.philips_rwl020_battery` | Hue Dimmer Battery | 100.0 |

| `sensor.rachels_phone_app_version` | Rachels Phone App Version | 2026.1.1 |

| `sensor.rachels_phone_audio_output` | Rachels Phone Audio Output | unavailable |

| `sensor.rachels_phone_battery_level` | Rachels Phone Battery Level | 40 |

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

| `sensor.rivian_phone_key_2060_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_3a87_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_3d22_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_714f_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_7f97_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_9e27_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_c28f_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_ec7f_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_phone_key_f289_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_sensor_1_d795_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_sensor_2_eca1_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_sensor_3_aa31_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_sensor_4_0a2c_estimated_distance` | Estimated distance | unavailable |

| `sensor.rivian_sensor_4_14f4_estimated_distance` | Estimated distance | unavailable |

| `sensor.s266657243954c04bc_20b2_estimated_distance` | S266657243954c04bC 20B2 Estimated distance | unavailable |

| `sensor.s2a274671f938dadcc_fde0_estimated_distance` | S2a274671f938dadcC FDE0 Estimated distance | unavailable |

| `sensor.s5763cf7cddb7eef9c_7c8d_estimated_distance` | Estimated distance | unavailable |

| `sensor.s58cdfccea0786690c_d4a2_estimated_distance` | S58cdfccea0786690C D4A2 Estimated distance | unavailable |

| `sensor.s97ba9994382d840bc_e454_estimated_distance` | Estimated distance | unavailable |

| `sensor.sbc4f3bc21b66bf73c_555f_estimated_distance` | Estimated distance | unavailable |

| `sensor.sc88d2596603604dcc_ffeb_estimated_distance` | Estimated distance | unavailable |

| `sensor.scd0ed4bcbf3abdf0c_652d_estimated_distance` | Estimated distance | unavailable |

| `sensor.sd78d075d9fbca645c_788d_estimated_distance` | Estimated distance | unavailable |

| `sensor.sdf631c51986d49cdc_295e_estimated_distance` | Estimated distance | unavailable |

| `sensor.sfb57741ef118e66ec_4652_estimated_distance` | Sfb57741ef118e66eC 4652 Estimated distance | unavailable |

| `sensor.shelly_ceiling_fan_energy` | Bedroom Ceiling Fan Energy | 12.430551 |

| `sensor.shelly_ceiling_fan_power` | Bedroom Ceiling Fan Power | 0 |

| `sensor.shelly_ceiling_lights_energy` | Bedroom Ceiling Lights Energy | 12.705878 |

| `sensor.shelly_ceiling_lights_power` | Bedroom Ceiling Lights Power | 31.8 |

| `sensor.slzb_mr1_connection_mode` | SLZB-MR1 Connection mode | wifi |

| `sensor.slzb_mr1_core_chip_temp` | SLZB-MR1 Core chip temp | 113.0 |

| `sensor.slzb_mr1_firmware_channel` | SLZB-MR1 Firmware channel | release |

| `sensor.slzb_mr1_zigbee_chip_temp` | SLZB-MR1 Zigbee chip temp | 109.976 |

| `sensor.slzb_mr1_zigbee_chip_temp_2` | SLZB-MR1 Zigbee chip temp | 108.752 |

| `sensor.slzb_mr1_zigbee_type` | SLZB-MR1 Zigbee type | thread |

| `sensor.slzb_mr1_zigbee_type_2` | SLZB-MR1 Zigbee type | coordinator |

| `sensor.sun_next_dawn` | Sun Next dawn | 2026-02-12T12:29:34+00:00 |

| `sensor.sun_next_dusk` | Sun Next dusk | 2026-02-13T00:05:01+00:00 |

| `sensor.sun_next_midnight` | Sun Next midnight | 2026-02-12T06:17:02+00:00 |

| `sensor.sun_next_noon` | Sun Next noon | 2026-02-12T18:17:02+00:00 |

| `sensor.sun_next_rising` | Sun Next rising | 2026-02-12T12:57:27+00:00 |

| `sensor.sun_next_setting` | Sun Next setting | 2026-02-12T23:37:06+00:00 |

| `sensor.telematic_575072_ced2_estimated_distance` | Estimated distance | unavailable |

| `sensor.third_reality_inc_3rths0224z_battery` | Temp & Humidity Battery | 100.0 |

| `sensor.third_reality_inc_3rvs01031z_battery` | Vibration Sensor 1 Battery | 100.0 |

| `sensor.uptime` | Uptime | 2026-02-10T09:31:12+00:00 |

| `sensor.vibration_2_third_reality_battery` | Vibration Sensor 2 Battery | 100.0 |

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




<details><summary><b>Switch (65)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `switch.akamatis_presence_sensor_b24c50_control_bluetooth` | Akamatis Presence Sensor b24c50 control Bluetooth | on |

| `switch.akamatis_presence_sensor_b24c50_engineering_mode` | Akamatis Presence Sensor b24c50 engineering mode | off |

| `switch.alexa_media_player_pre_release` | Alexa Media Player Pre-release | off |

| `switch.all_echo_do_not_disturb_switch` | All Echo Do not disturb | off |

| `switch.all_echo_repeat_switch` | All Echo Repeat | off |

| `switch.all_echo_shuffle_switch` | All Echo Shuffle | off |

| `switch.aqara_fp300_ai_adaptive_sensitivity` | Aqara FP300 AI adaptive sensitivity | off |

| `switch.aqara_fp300_ai_interference_source_self_identification` | Aqara FP300 AI interference source self-identification | off |

| `switch.aqara_fp300_detection_range_0_1_m` | Aqara FP300 Detection range 0–1 m | off |

| `switch.aqara_fp300_detection_range_1_2_m` | Aqara FP300 Detection range 1–2 m | off |

| `switch.aqara_fp300_detection_range_2_3_m` | Aqara FP300 Detection range 2–3 m | off |

| `switch.aqara_fp300_detection_range_3_4_m` | Aqara FP300 Detection range 3–4 m | off |

| `switch.aqara_fp300_detection_range_4_5_m` | Aqara FP300 Detection range 4–5 m | off |

| `switch.aqara_fp300_detection_range_5_6_m` | Aqara FP300 Detection range 5–6 m | off |

| `switch.bathroom_light` | Bathroom Light | off |

| `switch.bathroom_light_auto_off_enabled` | Bathroom Light Auto-off enabled | off |

| `switch.bathroom_light_auto_update_enabled` | Bathroom Light Auto-update enabled | on |

| `switch.bathroom_light_led` | Bathroom Light LED | off |

| `switch.bed_presence_bb8594_full_range` | Bed Pressure Sensor Full Range | off |

| `switch.bedroom_ceiling_fan` | Bedroom ceiling fan | off |

| `switch.bedroom_ceiling_lights` | Bedroom Ceiling Lights | on |

| `switch.bedroom_fan` | Fan | off |

| `switch.blake_s_echo_dot_do_not_disturb` | Blake's Echo Dot Do not disturb | on |

| `switch.blake_s_echo_dot_do_not_disturb_switch` | Blake's Echo Dot Do not disturb | on |

| `switch.blake_s_echo_dot_repeat_switch` | Blake's Echo Dot Repeat | unavailable |

| `switch.blake_s_echo_dot_shuffle_switch` | Blake's Echo Dot Shuffle | unavailable |

| `switch.blake_s_echo_pop_do_not_disturb` | Blake's Echo Pop Do not disturb | on |

| `switch.blake_s_echo_pop_do_not_disturb_switch` | Blake's Echo Pop Do not disturb | on |

| `switch.blake_s_echo_pop_repeat_switch` | Blake's Echo Pop Repeat | unavailable |

| `switch.blake_s_echo_pop_shuffle_switch` | Blake's Echo Pop Shuffle | unavailable |

| `switch.blake_s_echo_spot_do_not_disturb` | Blake's Echo Spot Do not disturb | on |

| `switch.blake_s_echo_spot_do_not_disturb_switch` | Blake's Echo Spot Do not disturb | on |

| `switch.blake_s_echo_spot_repeat_switch` | Blake's Echo Spot Repeat | unavailable |

| `switch.blake_s_echo_spot_shuffle_switch` | Blake's Echo Spot Shuffle | unavailable |

| `switch.closet_light` | Closet Light | off |

| `switch.closet_light_auto_off_enabled` | Closet Light Auto-off enabled | off |

| `switch.closet_light_auto_update_enabled` | Closet Light Auto-update enabled | on |

| `switch.closet_light_led` | Closet Light LED | off |

| `switch.custom_icons_pre_release` | Custom Icons Pre-release | off |

| `switch.everything_presence_lite_922d28_mmwave_bluetooth` | Everything Presence Lite mmWave Bluetooth | off |

| `switch.everything_presence_lite_922d28_stale_target_reset` | Everything Presence Lite Stale Target Reset | off |

| `switch.everything_presence_lite_922d28_upside_down_mounting` | Everything Presence Lite Upside Down Mounting | off |

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

</details>






<details><summary><b>Tts (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `tts.home_assistant_cloud` | Home Assistant Cloud | 2026-01-21T12:12:40.845214+00:00 |

</details>




<details><summary><b>Update (39)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `update.alexa_media_player_update` | Alexa Media Player update | on |

| `update.aqara_fp300_firmware` | Aqara FP300 Firmware | unknown |

| `update.badge_horizontal_container_card_update` | Badge horizontal container card update | off |

| `update.bed_presence_bb8594_firmware` | Bed Pressure Sensor Firmware | off |

| `update.bedroom_lamp_firmware` | Bedroom Lamp Firmware | unknown |

| `update.browser_mod_update` | browser_mod update | off |

| `update.button_card_update` | button-card update | off |

| `update.card_mod_update` | card-mod update | off |

| `update.custom_features_for_home_assistant_cards_update` | Custom Features for Home Assistant Cards update | on |

| `update.custom_icons_update` | Custom Icons update | off |

| `update.everything_presence_lite_922d28_everything_presence_lite_firmware` | Everything Presence Lite Everything Presence Lite Firmware | off |

| `update.everything_presence_zone_configurator_update` | Everything Presence Zone Configurator Update | off |

| `update.file_editor_update` | File editor Update | off |

| `update.hacs_update` | HACS update | off |

| `update.home_assistant_core_update` | Home Assistant Core Update | off |

| `update.home_assistant_matter_hub_3_0_0_alpha_76_update` | Home-Assistant-Matter-Hub (3.0.0-alpha.76) Update | off |

| `update.home_assistant_operating_system_update` | Home Assistant Operating System Update | off |

| `update.home_assistant_supervisor_update` | Home Assistant Supervisor Update | off |

| `update.living_room_lamp_firmware` | Living Room Lamp Firmware | unknown |

| `update.matter_server_update` | Matter Server Update | off |

| `update.mosquitto_broker_update` | Mosquitto broker Update | off |

| `update.motion_2_firmware` | Motion 2 - Third Reality Firmware | unknown |

| `update.mushroom_update` | Mushroom update | off |

| `update.music_assistant_update` | Music Assistant Update | off |

| `update.nest_protect_update` | Nest Protect update | off |

| `update.openthread_border_router_update` | OpenThread Border Router Update | on |

| `update.philips_rwl020_firmware` | Hue Dimmer Firmware | unknown |

| `update.shelly_device_firmware` | Shelly Device Firmware | off |

| `update.slzb_mr1_core_firmware` | SLZB-MR1 Core firmware | on |

| `update.slzb_mr1_zigbee_firmware` | SLZB-MR1 Zigbee firmware | off |

| `update.slzb_mr1_zigbee_firmware_2` | SLZB-MR1 Zigbee firmware | off |

| `update.sqlite_web_update` | SQLite Web Update | off |

| `update.studio_code_server_update` | Studio Code Server Update | off |

| `update.terminal_ssh_update` | Terminal & SSH Update | on |

| `update.third_reality_inc_3rths0224z_firmware` | Temp & Humidity Firmware | unknown |

| `update.third_reality_inc_3rvs01031z_firmware` | Vibration Sensor 1 Firmware | off |

| `update.ultra_card_update` | Ultra Card update | off |

| `update.vertical_stack_in_card_update` | Vertical Stack In Card update | off |

| `update.vibration_2_third_reality_firmware` | Vibration Sensor 2 Firmware | off |

</details>




<details><summary><b>Weather (1)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `weather.openweathermap_2` | OpenWeatherMap | cloudy |

</details>




<details><summary><b>Zone (4)</b></summary>

| Entity ID | Name | State |
|---|---|---|

| `zone.home` | Home | 1 |

| `zone.rachels_home` | Rachel’s Home | 1 |

| `zone.rachels_work` | Rachel’s Work | 0 |

| `zone.work` | Work | 0 |

</details> EOF
