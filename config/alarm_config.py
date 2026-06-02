"""
Alarm Configuration
44 Alarm Blocks from alarmBlocks.csv
"""
from config.memory_map import *

# Alarm configuration dictionary
ALARM_BLOCKS = {
    # ==============================================================================
    # CRITICAL ALARMS (Level 2)
    # ==============================================================================
    MB_ALARM_PHASE_SEQUENCE: {
        'block_id': 0,
        'block_name': 'PHASE SEQUENCE',
        'alarm_level': 2,
        'message_key': 'alarms.phase_sequence',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_AUX: {
        'block_id': 7,
        'block_name': 'AUX',
        'alarm_level': 2,
        'message_key': 'alarms.aux',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HIGH_TEMP_CHAMBER: {
        'block_id': 14,
        'block_name': 'HIGH TEMP CHAMBER',
        'alarm_level': 2,
        'message_key': 'alarms.high_temp_chamber',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HIGH_TEMP_AIR_DRY: {
        'block_id': 15,
        'block_name': 'HIGH TEMP AIR DRY',
        'alarm_level': 2,
        'message_key': 'alarms.high_temp_air_dry',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_THERMAL_SAFETY: {
        'block_id': 23,
        'block_name': 'THERMAL SAFETY',
        'alarm_level': 2,
        'message_key': 'alarms.thermal_safety',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_WATER_LOST: {
        'block_id': 1,
        'block_name': 'WATER LOST',
        'alarm_level': 2,
        'message_key': 'alarms.water_lost',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_WASH_PUMP_PRESSURE: {
        'block_id': 2,
        'block_name': 'WASH PUMP PRESSURE',
        'alarm_level': 2,
        'message_key': 'alarms.wash_pump_pressure',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_AIR_DRY_PRESSURE_SW1: {
        'block_id': 3,
        'block_name': 'AIR DRY PRESSURE SW1',
        'alarm_level': 2,
        'message_key': 'alarms.air_dry_pressure_sw1',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_AIR_DRY_PRESSURE_SW2: {
        'block_id': 4,
        'block_name': 'AIR DRY PRESSURE SW2',
        'alarm_level': 2,
        'message_key': 'alarms.air_dry_pressure_sw2',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHAMBER_PROBE_FAIL: {
        'block_id': 5,
        'block_name': 'CHAMBER PROBE FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.chamber_probe_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_DRY_PROBE_FAIL: {
        'block_id': 6,
        'block_name': 'DRY PROBE FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.dry_probe_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHEMICAL_FLOW_ERROR: {
        'block_id': 8,
        'block_name': 'CHEMICAL FLOW ERROR',
        'alarm_level': 2,
        'message_key': 'alarms.chemical_flow_error',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHAMBER_HEATING_FAIL: {
        'block_id': 9,
        'block_name': 'CHAMBER HEATING FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.chamber_heating_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_AIR_DRY_HEATING_FAIL: {
        'block_id': 10,
        'block_name': 'AIR DRY HEATING FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.air_dry_heating_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_DRAIN_FAIL: {
        'block_id': 11,
        'block_name': 'DRAIN FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.drain_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HEATING_TANK1_FAIL: {
        'block_id': 12,
        'block_name': 'HEATING TANK 1 FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.heating_tank1_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HEATING_TANK2_FAIL: {
        'block_id': 13,
        'block_name': 'HEATING TANK 2 FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.heating_tank2_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HIGH_TEMP_TANK1: {
        'block_id': 16,
        'block_name': 'HIGH TEMP TANK 1',
        'alarm_level': 2,
        'message_key': 'alarms.high_temp_tank1',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HIGH_TEMP_TANK2: {
        'block_id': 17,
        'block_name': 'HIGH TEMP TANK 2',
        'alarm_level': 2,
        'message_key': 'alarms.high_temp_tank2',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_TEMP_DIFF_CHAMBER: {
        'block_id': 43,
        'block_name': 'TEMP DIFF IN CHAMBER',
        'alarm_level': 2,
        'message_key': 'alarms.temp_diff_chamber',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_FAIL_FILLING_TANK1: {
        'block_id': 24,
        'block_name': 'FAIL FILLING TANK 1',
        'alarm_level': 2,
        'message_key': 'alarms.fail_filling_tank1',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_FAIL_FILLING_TANK2: {
        'block_id': 25,
        'block_name': 'FAIL FILLING TANK 2',
        'alarm_level': 2,
        'message_key': 'alarms.fail_filling_tank2',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_FAIL_FILLING_WATER3: {
        'block_id': 26,
        'block_name': 'FAIL FILLING WATER 3 (COLD)',
        'alarm_level': 2,
        'message_key': 'alarms.fail_filling_water3',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_FAIL_FILLING_WATER4: {
        'block_id': 27,
        'block_name': 'FAIL FILLING WATER 4 (DEMIN)',
        'alarm_level': 2,
        'message_key': 'alarms.fail_filling_water4',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_FAIL_LOADING_DOOR: {
        'block_id': 28,
        'block_name': 'FAIL LOADING DOOR TIMEOUT',
        'alarm_level': 2,
        'message_key': 'alarms.fail_loading_door',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_FAIL_UNLOADING_DOOR: {
        'block_id': 29,
        'block_name': 'FAIL UNLOADING DOOR TIMEOUT',
        'alarm_level': 2,
        'message_key': 'alarms.fail_unloading_door',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_TANK1_MAX_LEVEL: {
        'block_id': 30,
        'block_name': 'TANK 1 MAX LEVEL FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.tank1_max_level',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_TANK2_MAX_LEVEL: {
        'block_id': 31,
        'block_name': 'TANK 2 MAX LEVEL FAIL',
        'alarm_level': 2,
        'message_key': 'alarms.tank2_max_level',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_PT1000_TANK1: {
        'block_id': 32,
        'block_name': 'PT1000 TANK 1 OUT OF RANGE',
        'alarm_level': 2,
        'message_key': 'alarms.pt1000_tank1_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_PT1000_TANK2: {
        'block_id': 33,
        'block_name': 'PT1000 TANK 2 OUT OF RANGE',
        'alarm_level': 2,
        'message_key': 'alarms.pt1000_tank2_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHEMICAL1_TIMEOUT: {
        'block_id': 36,
        'block_name': 'CHEMICAL 1 FILL TIMEOUT',
        'alarm_level': 2,
        'message_key': 'alarms.chemical1_timeout',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHEMICAL2_TIMEOUT: {
        'block_id': 37,
        'block_name': 'CHEMICAL 2 FILL TIMEOUT',
        'alarm_level': 2,
        'message_key': 'alarms.chemical2_timeout',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHEMICAL3_TIMEOUT: {
        'block_id': 38,
        'block_name': 'CHEMICAL 3 FILL TIMEOUT',
        'alarm_level': 2,
        'message_key': 'alarms.chemical3_timeout',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_PRINTER_SIGNAL_LOST: {
        'block_id': 40,
        'block_name': 'PRINTER SIGNAL LOST',
        'alarm_level': 2,
        'message_key': 'alarms.printer_signal_lost',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_UNLOAD_DOOR_NOT_CLOSE: {
        'block_id': 41,
        'block_name': 'UNLOAD DOOR NOT CLOSE',
        'alarm_level': 2,
        'message_key': 'alarms.unload_door_not_close',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },

    # ==============================================================================
    # WARNING ALARMS (Level 1)
    # ==============================================================================
    MB_ALARM_CHEMICAL1_LOW: {
        'block_id': 20,
        'block_name': 'CHEMICAL 1 LOW',
        'alarm_level': 1,
        'message_key': 'alarms.chemical1_low',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHEMICAL2_LOW: {
        'block_id': 21,
        'block_name': 'CHEMICAL 2 LOW',
        'alarm_level': 1,
        'message_key': 'alarms.chemical2_low',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_CHEMICAL3_LOW: {
        'block_id': 22,
        'block_name': 'CHEMICAL 3 LOW',
        'alarm_level': 1,
        'message_key': 'alarms.chemical3_low',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_AIR_SUPPLY_LOW: {
        'block_id': 34,
        'block_name': 'AIR SUPPLY LOW',
        'alarm_level': 1,
        'message_key': 'alarms.air_supply_low',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_HEPA_FILTER: {
        'block_id': 19,
        'block_name': 'HEPA FILTER',
        'alarm_level': 1,
        'message_key': 'alarms.hepa_filter',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_PRINTER_COMM_FAIL: {
        'block_id': 35,
        'block_name': 'PRINTER COMM FAIL',
        'alarm_level': 1,
        'message_key': 'alarms.printer_comm_fail',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_LOW_MEMORY: {
        'block_id': 39,
        'block_name': 'LOW MEMORY LOGGER',
        'alarm_level': 1,
        'message_key': 'alarms.low_memory_logger',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_NO_BASKET: {
        'block_id': 42,
        'block_name': 'NO BASKET',
        'alarm_level': 1,
        'message_key': 'alarms.no_basket',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
    MB_ALARM_DOOR_NOT_CLOSE: {
        'block_id': 18,
        'block_name': 'DOOR NOT CLOSE',
        'alarm_level': 1,
        'message_key': 'alarms.door_not_close',
        'require_acknowledgement': False,
        'display_message': True,
        'record_alarm': False,
    },
}

# Alarm polling configuration
ALARM_POLL_INTERVAL = 0.5  # 500ms
ALARM_BATCH_SIZE = 44  # Read all 44 alarms at once

# Alarm UI configuration
ALARM_CRITICAL_COLOR = "#FF0000"  # Red
ALARM_WARNING_COLOR = "#FFFF00"  # Yellow
ALARM_AUTO_DISMISS_TIME = 10  # seconds for warning level

def get_alarm_by_mb(mb_address: int) -> dict:
    """
    Get alarm configuration by MB address

    Args:
        mb_address: MB address

    Returns:
        dict: Alarm configuration or None
    """
    return ALARM_BLOCKS.get(mb_address)

def get_critical_alarms() -> dict:
    """
    Get all critical (Level 2) alarms

    Returns:
        dict: Critical alarm configurations
    """
    return {k: v for k, v in ALARM_BLOCKS.items() if v['alarm_level'] == 2}

def get_warning_alarms() -> dict:
    """
    Get all warning (Level 1) alarms

    Returns:
        dict: Warning alarm configurations
    """
    return {k: v for k, v in ALARM_BLOCKS.items() if v['alarm_level'] == 1}
