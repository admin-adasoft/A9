"""
PLC Memory Map
MB (Memory Bit) and MI (Memory Integer) Address Definitions
Based on ObjLstOfScreenDesignWashMachine.csv
"""

# ==============================================================================
# NAVIGATION BUTTONS (MB900-MB999)
# ==============================================================================
MB_HOME = 900  # Return to Home (Screen 1)
MB_NAV_SCREEN_2 = 902  # Navigate to Screen 2 (Program Factory) - MB902
MB_NAV_SCREEN_3 = 903  # Navigate to Screen 3
MB_NAV_SCREEN_4 = 904  # Navigate to Screen 4
MB_NAV_SCREEN_5 = 905  # Navigate to Screen 5
MB_NAV_SCREEN_6 = 911  # Navigate to Screen 6 (Manual Graphic) — CSV BB0002 on Screen 5: MB911
MB_NAV_LAST_CYCLE = 906  # Navigate to Screen 26 Last Cycle Menu (CSV BB0000 on Screen 1: MB906)
MB_NAV_SCREEN_7 = 901  # Navigate to Screen 7 (Setup) - MB901
MB_NAV_SCREEN_8 = 907  # Navigate to Screen 8 / Program 1 select
MB_NAV_SCREEN_9 = 908  # Navigate to Screen 9 / Program 2 select
MB_NAV_SCREEN_10 = 909  # Navigate to Screen 10 / Program 3 select
MB_PROGRAM_4_SELECT = 910  # Program 4 select (to Screen 8)

# Screen 3 (Program Factory 2/4) Program Selection
MB_PROGRAM_1_SELECT_S3 = 997   # Screen 3: Program 1 selection -> Screen 8
MB_PROGRAM_2_SELECT_S3 = 998   # Screen 3: Program 2 selection -> Screen 8
MB_PROGRAM_3_SELECT_S3 = 1084  # Screen 3: Program 3 selection -> Screen 8
MB_PROGRAM_4_SELECT_S3 = 1085  # Screen 3: Program 4 selection -> Screen 8
MB_PROGRAM_5_SELECT_S3 = 1086  # Screen 3: Program 5 selection -> Screen 8
MB_PROGRAM_6_SELECT_S3 = 1087  # Screen 3: Program 6 selection -> Screen 8
MB_NAV_BACK_S3 = 904           # Screen 3: Back navigation (to Screen 2)

MB_CANCEL = 912  # Cancel/back to previous screen
MB_CONFIRM = 913  # Confirm action
MB_DOOR_TOGGLE = 915  # Door control toggle

MB_NAV_MANUAL_GRAPHIC = 911  # Navigate to Screen 6 (Manual Graphic) from Maintenance
MB_NOT_IMPLEMENTED = 999  # Placeholder for features not yet implemented

# Navigation addresses used by specific screens (aliases)
MB_NAV_SCREEN_21 = 1093  # Navigate to Screen 21 (Alarms)
MB_NAV_SCREEN_23 = 23  # Navigate to Screen 23 (Utility Menu) - Screen Button
MB_NAV_SCREEN_26 = 906  # Navigate to Screen 26 (Last Cycle Menu)
MB_NAV_MAINTENANCE = 905  # Navigate to Screen 4 (Maintenance Password)
MB_NAV_SCREEN_15 = 914  # Navigate to Screen 15 (Program Selection) from Setup
MB_NAV_SCREEN_18 = 970  # Navigate to Screen 18 (Basket Setting) from Setup
MB_NAV_SCREEN_35 = 971  # Navigate to Screen 35 (User Lists) from Setup

# ==============================================================================
# SCREEN 15, 27, 28, 29 - SELECT ENTER PROGRAM (Pagination)
# ==============================================================================
# Program buttons (shared across all 4 screens) -> navigate to Screen 11
MB_ENTER_PROGRAM_1 = 917   # Program 1 -> page 11
MB_ENTER_PROGRAM_2 = 935   # Program 2 -> page 11
MB_ENTER_PROGRAM_3 = 936   # Program 3 -> page 11
MB_ENTER_PROGRAM_4 = 937   # Program 4 -> page 11
MB_ENTER_PROGRAM_5 = 938   # Program 5 -> page 11
MB_ENTER_PROGRAM_6 = 939   # Program 6 -> page 11
MB_ENTER_PROGRAM_7 = 940   # Program 7 -> page 11
MB_ENTER_PROGRAM_8 = 941   # Program 8 -> page 11

# Navigation between pagination screens
MB_NAV_SCREEN_15_TO_27 = 1002  # Screen 15 NEXT -> Screen 27
MB_NAV_SCREEN_27_TO_28 = 1005  # Screen 27 NEXT -> Screen 28
MB_NAV_SCREEN_28_TO_29 = 1006  # Screen 28 NEXT -> Screen 29
MB_NAV_SCREEN_27_BACK = 914    # Screen 27 BACK -> Screen 15
MB_NAV_SCREEN_28_BACK = 1002   # Screen 28 BACK -> Screen 27
MB_NAV_SCREEN_29_BACK = 1005   # Screen 29 BACK -> Screen 28

# ==============================================================================
# DOOR CONTROL AND STATES (MB17-MB27)
# ==============================================================================
MB_DOOR_PANEL_VISIBLE = 17  # Door control panel visibility (MB17)
MB_DOOR_OPEN = 18  # Button Open Door command
MB_DOOR_CLOSE = 19  # Button Close Door command
MB_DOOR_CONTROL_2 = 20
MB_DOOR_FRONT_OPEN   = 40   # Manual: front door open   (Screen 06)
MB_DOOR_FRONT_CLOSE  = 41   # Manual: front door close  (Screen 06)
MB_DOOR_BACK_OPEN    = 42   # Manual: back door open    (Screen 06 / Sub-Screen)
MB_DOOR_BACK_CLOSE   = 44   # Manual: back door close   (Screen 06 / Sub-Screen)
MB_DOOR_BACK_STATUS  = 128  # Monitor: back door status (1=closed, 0=open) — MB128
MB_DOOR_LOADING = 245  # Loading door status
MB_DOOR_UNLOADING = 246  # Unloading door status

# ==============================================================================
# SAFETY INTERLOCKS (MB248-MB249)
# ==============================================================================
MB_SAFETY_BAR_LOADING = 248  # Safety bar loading door
MB_SAFETY_BAR_UNLOADING = 249  # Safety bar unloading door

# ==============================================================================
# SAFETY BAR ACKNOWLEDGE (MB250-MB251)
# ==============================================================================
MB_SAFETY_ACK_LOADING = 250  # Acknowledge loading door safety bar
MB_SAFETY_ACK_UNLOADING = 251  # Acknowledge unloading door safety bar

# ==============================================================================
# VISIBILITY CONTROL
# ==============================================================================
MB_VERSION_VISIBLE = 324  # Show version display (MI930)

# ==============================================================================
# SUB-SCREEN (SECONDARY DISPLAY) ADDRESSES
# From ObjLstOfWasherHMI_SubScreen.csv
# ==============================================================================
MI_SUB_DOOR_CONTROL = 201  # W201: door open(bit0) / close(bit1) / status(bit2) / ok-finish(bit3)
MI_SUB_ALERT_WARNING_DOOR = 334  # W334: sub-screen WARNING DOOR alert block (bits 0..3)
MB_SUB_ALERT_DOOR_STUCK = 325  # B325: sub-screen discrete alert block (door stuck)
MI_SUB_SCREEN_REGISTER = 1704  # W1704: sub-screen switching register ($C0); 2 = Finish Screen_ 2

# ==============================================================================
# WARNING AND STATUS (MB180-MB200)
# ==============================================================================
MB_WARNING_PAGE = 182  # Warning page trigger
MB_ALARM_STATUS = 200  # MB200: machine alarm active (error/fault condition) — for UI flash and alarm bell

# ==============================================================================
# ALARM ADDRESSES (MB136-MB301) - 44 Alarm Blocks
# ==============================================================================
# From alarmBlocks.csv

# Critical Alarms (Level 2)
MB_ALARM_PHASE_SEQUENCE = 136  # Phase sequence alarm
MB_ALARM_AUX = 137  # AUX alarm
MB_ALARM_HIGH_TEMP_CHAMBER = 138  # High temperature chamber
MB_ALARM_HIGH_TEMP_AIR_DRY = 139  # High temperature air dry
MB_ALARM_THERMAL_SAFETY = 150  # Thermal safety

MB_ALARM_HIGH_TEMP_TANK1 = 160  # High temperature tank 1
MB_ALARM_HIGH_TEMP_TANK2 = 161  # High temperature tank 2
MB_ALARM_FAIL_FILLING_TANK1 = 162  # Fail filling tank 1
MB_ALARM_FAIL_FILLING_TANK2 = 163  # Fail filling tank 2
MB_ALARM_FAIL_FILLING_WATER3 = 164  # Fail filling water 3
MB_ALARM_FAIL_FILLING_WATER4 = 165  # Fail filling water 4
MB_ALARM_FAIL_LOADING_DOOR = 166  # Fail loading door timeout
MB_ALARM_FAIL_UNLOADING_DOOR = 167  # Fail unloading door timeout
MB_ALARM_TANK1_MAX_LEVEL = 168  # Tank 1 max level fail
MB_ALARM_TANK2_MAX_LEVEL = 169  # Tank 2 max level fail
MB_ALARM_PT1000_TANK1 = 170  # PT1000 tank 1 out of range
MB_ALARM_PT1000_TANK2 = 171  # PT1000 tank 2 out of range

MB_ALARM_WATER_LOST = 202  # Water lost
MB_ALARM_WASH_PUMP_PRESSURE = 206  # Wash pump pressure abnormal
MB_ALARM_AIR_DRY_PRESSURE_SW1 = 207  # Air dry pressure SW1
MB_ALARM_AIR_DRY_PRESSURE_SW2 = 208  # Air dry pressure SW2
MB_ALARM_CHAMBER_PROBE_FAIL = 209  # Chamber probe fail
MB_ALARM_DRY_PROBE_FAIL = 210  # Dry probe fail

MB_ALARM_CHEMICAL_FLOW_ERROR = 212  # Chemical flow error
MB_ALARM_CHAMBER_HEATING_FAIL = 213  # Chamber heating fail
MB_ALARM_AIR_DRY_HEATING_FAIL = 214  # Air dry heating fail
MB_ALARM_DRAIN_FAIL = 215  # Drain fail
MB_ALARM_HEATING_TANK1_FAIL = 216  # Heating tank 1 fail
MB_ALARM_HEATING_TANK2_FAIL = 217  # Heating tank 2 fail

MB_ALARM_TEMP_DIFF_CHAMBER = 223  # Temperature difference in chamber

MB_ALARM_CHEMICAL1_TIMEOUT = 233  # Chemical 1 fill timeout
MB_ALARM_CHEMICAL2_TIMEOUT = 234  # Chemical 2 fill timeout
MB_ALARM_CHEMICAL3_TIMEOUT = 235  # Chemical 3 fill timeout
MB_ALARM_PRINTER_SIGNAL_LOST = 236  # Printer signal lost
MB_ALARM_UNLOAD_DOOR_NOT_CLOSE = 237  # Unload door not close

# Warning Alarms (Level 1)
MB_ALARM_CHEMICAL1_LOW = 116  # Chemical 1 low level (Warning)
MB_ALARM_CHEMICAL2_LOW = 117  # Chemical 2 low level (Warning)
MB_ALARM_CHEMICAL3_LOW = 118  # Chemical 3 low level (Warning)

MB_ALARM_AIR_SUPPLY_LOW = 174  # Air supply low (Warning)
MB_ALARM_HEPA_FILTER = 175  # HEPA filter (Warning)

MB_ALARM_PRINTER_COMM_FAIL = 186  # Printer communication fail (Warning)
MB_ALARM_LOW_MEMORY = 196  # Low memory logger (Warning)

MB_ALARM_NO_BASKET = 286  # No basket (Warning)
MB_ALARM_DOOR_NOT_CLOSE = 301  # Door not close (Warning)

# ==============================================================================
# SCREEN 08 BEGIN START CYCLE (MB25, MB245-MB246, MB912-MB913, MB920)
# ==============================================================================
MB_CONFIRM_BUTTON_VISIBLE = 25  # Confirm button visibility (from program select)
MB_DIRTY_DOOR_WARNING = 245  # Dirty side door not closed message (ประตูฝั่งสกปรก)
MB_CLEAN_DOOR_WARNING = 246  # Clean side door not closed message (ประตูฝั่งสะอาด)
MB_CANCEL_SCREEN_08 = 912  # Cancel button - back to previous screen
MB_CONFIRM_SCREEN_08 = 913  # Confirm button - go to Screen 9 (Auto)
MB_FROM_LAST_CYCLE = 920  # From last cycle button (hide confirm)

# ==============================================================================
# SCREEN 26 LATEST OPERATION (MB920, MB1108, MB320, MB197)
# ==============================================================================
MB_LATEST_OPERATION = 920  # Latest operation button (to Screen 8, hides confirm)
MB_PRINT_LATEST_CYCLE = 1108  # Print latest cycle command to PLC
MB_LATEST_OP_MONITOR = 320  # Monitor for latest operation button
MB_PRINT_LATEST_MONITOR = 197  # Monitor for print latest button

# ==============================================================================
# SCREEN 37 RE-PRINT PROTOCOL
# ==============================================================================
ML_REPRINT_CYCLE_ID = 12    # INT32: cycle number to re-print (HMI → PLC, Unitronics ML12)
MB_REPRINT_TRIGGER  = 1108  # Bit: pulse to trigger print — reuses Screen 26 MB1108 (HMI → PLC)

# ==============================================================================
# SCREEN 09 AUTO - PROCESS CONTROL (MB26-MB28, MB122-MB124, MB140)
# ==============================================================================
MB_SKIP_STOP_PANEL = 26  # Skip/Stop selection panel visibility
MB_CONFIRM_CANCEL_PANEL = 27  # Confirm/Cancel panel visibility
MB_SKIP_STOP_STATE = 28  # Skip/Stop state (0=Skip, 1=Stop)
MB_CHEMICAL_1_STATUS = 122  # Chemical 1 ON/OFF status
MB_CHEMICAL_2_STATUS = 123  # Chemical 2 ON/OFF status
MB_CHEMICAL_3_STATUS = 124  # Chemical 3 ON/OFF status
MB_DOOR_STATUS = 140  # Door status (ON=Open, OFF=Close)

# Screen 09 Control Buttons (MB1088-MB1092)
MB_SELECT_BUTTON = 1088  # Select button (trigger more options popup)
MB_SKIP_PHASE = 1089  # Skip phase button
MB_CONFIRM_SKIP_STOP = 1090  # Confirm skip/stop action
MB_STOP_PROCESS = 1091  # Stop process button
MB_CANCEL_SKIP_STOP = 1092  # Cancel button

# ==============================================================================
# SCREEN 11 - ENTER PROGRAM
# ==============================================================================
# Visibility control overlays
MB_S11_CONFIRM_CLEAR_VISIBLE = 135   # Show confirm-clear overlay (MB135)
MB_S11_SAVE_SUCCESS_VISIBLE = 179    # Show save-success overlay (MB179)

# Action buttons
MB_S11_CLEAR_DATA = 1097      # BB0021 – trigger clear program data
MB_S11_CANCEL_CLEAR = 1092   # BB0023 – cancel from confirm-clear overlay
MB_S11_CONFIRM_CLEAR = 1098  # BB0024 – confirm clear program data
MB_S11_OK_SAVE = 1102        # BB0022 – OK after save success
MB_S11_NAV_PROGRAM = 1109    # BB0000 – to page 15 (select main program)
MB_S11_NAV_DRAIN = 916       # BB0001 – to page 14 (drain config screen)
MB_S11_SAVE = 934            # BB0002 – save program
MB_S11_NAV_WASH = 921        # BB0003 – to page 13 (wash config screen)

# Wash slot buttons (BB0004-BB0011) – navigate to screen 16 to pick a wash program
MB_S11_SEL_WASH_1 = 925   # BB0004 set wash slot 1
MB_S11_SEL_WASH_2 = 942   # BB0005 set wash slot 2
MB_S11_SEL_WASH_3 = 943   # BB0006 set wash slot 3
MB_S11_SEL_WASH_4 = 944   # BB0007 set wash slot 4
MB_S11_SEL_WASH_5 = 945   # BB0008 set wash slot 5
MB_S11_SEL_WASH_6 = 946   # BB0009 set wash slot 6
MB_S11_SEL_WASH_7 = 947   # BB0010 set wash slot 7
MB_S11_SEL_WASH_8 = 948   # BB0011 set wash slot 8

# Drain slot buttons (BB0012-BB0019) – navigate to screen 17 to pick a drain program
MB_S11_SEL_DRAIN_1 = 952   # BB0012 set drain slot 1
MB_S11_SEL_DRAIN_2 = 953   # BB0013 set drain slot 2
MB_S11_SEL_DRAIN_3 = 954   # BB0014 set drain slot 3
MB_S11_SEL_DRAIN_4 = 955   # BB0015 set drain slot 4
MB_S11_SEL_DRAIN_5 = 956   # BB0016 set drain slot 5
MB_S11_SEL_DRAIN_6 = 957   # BB0017 set drain slot 6
MB_S11_SEL_DRAIN_7 = 958   # BB0018 set drain slot 7
MB_S11_SEL_DRAIN_8 = 959   # BB0019 set drain slot 8

# Basket type button (BB0020) – navigate to screen 19
MB_S11_SEL_BASKET = 996   # BB0020 set basket type

# Numeric parameters
MI_S11_DRAIN_BEGIN_TIME = 471   # NE0000 start drain time (sec)
MI_S11_AIR_DRY_TEMP = 489       # NE0001 air dry temperature (°C)
MI_S11_AIR_DRY_TIME = 580       # NE0002 air dry time (sec)

# Character Entry / Display
MI_S11_PROGRAM_NAME = 490       # TE0000 program name (read/write)

# Wash program name monitors (Character Display, 10 words each)
MI_S11_WASH_1_NAME = 335   # TD0000 wash 1 name
MI_S11_WASH_2_NAME = 345   # TD0001 wash 2 name
MI_S11_WASH_3_NAME = 355   # TD0002 wash 3 name
MI_S11_WASH_4_NAME = 365   # TD0003 wash 4 name
MI_S11_WASH_5_NAME = 375   # TD0004 wash 5 name
MI_S11_WASH_6_NAME = 385   # TD0005 wash 6 name
MI_S11_WASH_7_NAME = 581   # TD0006 wash 7 name
MI_S11_WASH_8_NAME = 591   # TD0007 wash 8 name

# Drain program name monitors (Character Display, 10 words each)
MI_S11_DRAIN_1_NAME = 601   # TD0008 drain 1 name
MI_S11_DRAIN_2_NAME = 611   # TD0009 drain 2 name
MI_S11_DRAIN_3_NAME = 621   # TD0010 drain 3 name
MI_S11_DRAIN_4_NAME = 631   # TD0011 drain 4 name
MI_S11_DRAIN_5_NAME = 641   # TD0012 drain 5 name
MI_S11_DRAIN_6_NAME = 651   # TD0013 drain 6 name
MI_S11_DRAIN_7_NAME = 661   # TD0014 drain 7 name
MI_S11_DRAIN_8_NAME = 671   # TD0015 drain 8 name

# Basket name monitor
MI_S11_BASKET_NAME = 824   # TD0016 basket type name

# ==============================================================================
# SCREEN 16 - SELECT WASH PROGRAM
# ==============================================================================
# Write MB: select program slot
MB_SEL_WASH_PROG_1 = 926   # Select wash program 1 (BB0000)
MB_SEL_WASH_PROG_2 = 927   # Select wash program 2 (BB0001)
MB_SEL_WASH_PROG_3 = 928   # Select wash program 3 (BB0004)
MB_SEL_WASH_PROG_4 = 929   # Select wash program 4 (BB0002)
MB_SEL_WASH_PROG_5 = 930   # Select wash program 5 (BB0003)
MB_SEL_WASH_PROG_6 = 931   # Select wash program 6 (BB0012)
MB_SEL_WASH_PROG_7 = 932   # Select wash program 7 (BB0005)
MB_SEL_WASH_PROG_8 = 933   # Select wash program 8 (BB0011)

# Monitor MB: current selected state (shared with screen 17 and 19)
MB_SEL_PROG_MON_1 = 152    # Monitor program 1 selected
MB_SEL_PROG_MON_2 = 153    # Monitor program 2 selected
MB_SEL_PROG_MON_3 = 154    # Monitor program 3 selected
MB_SEL_PROG_MON_4 = 155    # Monitor program 4 selected
MB_SEL_PROG_MON_5 = 156    # Monitor program 5 selected
MB_SEL_PROG_MON_6 = 157    # Monitor program 6 selected
MB_SEL_PROG_MON_7 = 158    # Monitor program 7 selected
MB_SEL_PROG_MON_8 = 159    # Monitor program 8 selected

# Range tabs (Write / Monitor)
MB_SEL_WASH_RANGE_1 = 949       # Range 1-8  write  (BB0006)
MB_SEL_WASH_RANGE_2 = 950       # Range 9-16 write  (BB0007)
MB_SEL_WASH_RANGE_3 = 951       # Range 17-24 write (BB0008)
MB_SEL_WASH_RANGE_MON_1 = 20    # Range 1-8  monitor (BB0006 monitor)
MB_SEL_WASH_RANGE_MON_2 = 21    # Range 9-16 monitor
MB_SEL_WASH_RANGE_MON_3 = 22    # Range 17-24 monitor

# Clear (ลบ) button
MB_SEL_WASH_CLEAR     = 1095  # BB0013 write – clear selection
MB_SEL_WASH_CLEAR_MON = 100   # BB0013 monitor – clear selected state

# ==============================================================================
# SCREEN 17 - SELECT DRAIN PROGRAM
# ==============================================================================
# Write MB: select drain program slot
MB_SEL_DRAIN_PROG_1 = 962   # Select drain program 1 (BB0000)
MB_SEL_DRAIN_PROG_2 = 963   # Select drain program 2 (BB0001)
MB_SEL_DRAIN_PROG_3 = 964   # Select drain program 3 (BB0004)
MB_SEL_DRAIN_PROG_4 = 965   # Select drain program 4 (BB0002)
MB_SEL_DRAIN_PROG_5 = 966   # Select drain program 5 (BB0003)
MB_SEL_DRAIN_PROG_6 = 967   # Select drain program 6 (BB0012)
MB_SEL_DRAIN_PROG_7 = 968   # Select drain program 7 (BB0005)
MB_SEL_DRAIN_PROG_8 = 969   # Select drain program 8 (BB0011)

# Range tabs (Write / Monitor) – only 2 tabs on screen 17
MB_SEL_DRAIN_RANGE_1 = 960      # Range 1-8  write  (BB0006)
MB_SEL_DRAIN_RANGE_2 = 961      # Range 9-16 write  (BB0008)
MB_SEL_DRAIN_RANGE_MON_1 = 23   # Range 1-8  monitor (BB0006 monitor)
MB_SEL_DRAIN_RANGE_MON_2 = 24   # Range 9-16 monitor (BB0008 monitor)

# Clear (CLEAR) button
MB_SEL_DRAIN_CLEAR     = 1096  # BB0007 write – clear selection
MB_SEL_DRAIN_CLEAR_MON = 119   # BB0007 monitor – clear selected state

# ==============================================================================
# SCREEN 19 - SELECT BASKET PROGRAM
# ==============================================================================
# Write MB: select basket slot
MB_SEL_BASKET_1 = 1075   # Select basket 1 (BB0002)
MB_SEL_BASKET_2 = 1076   # Select basket 2 (BB0003)
MB_SEL_BASKET_3 = 1077   # Select basket 3 (BB0006)
MB_SEL_BASKET_4 = 1078   # Select basket 4 (BB0004)
MB_SEL_BASKET_5 = 1079   # Select basket 5 (BB0005)
MB_SEL_BASKET_6 = 1080   # Select basket 6 (BB0009)
MB_SEL_BASKET_7 = 1081   # Select basket 7 (BB0007)
MB_SEL_BASKET_8 = 1082   # Select basket 8 (BB0008)

# ALL baskets button
MB_SEL_BASKET_ALL = 1101      # ALL baskets selected (BB0010 write)
MB_SEL_BASKET_ALL_MON = 172   # ALL baskets monitor (BB0010 monitor)

# ==============================================================================
# SCREEN 23 UTILITY MENU (MB1103, MB1107)
# ==============================================================================
MB_WASHING_FIND = 1103  # WASHING FIND button -> navigate to Screen 24
MB_DRAIN_FIND = 1107  # DRAIN FIND button -> navigate to Screen 24

# ==============================================================================
# SCREEN 24 WASHING FIND
# ==============================================================================
# Not Found Popup
MB_NOT_FOUND_POPUP_VISIBLE = 183  # Not found popup visibility (MB183)
MB_NOT_FOUND_MESSAGE_STATE = 184  # Message state: 0=NO DRAIN, 1=NO WASHING
MB_NOT_FOUND_OK = 1106  # OK button on not found popup (Write)

# Pagination buttons
MB_RANGE_1_8 = 185  # Show programs 1-8 (Write), Monitor: MB12
MB_RANGE_9_16 = 1104  # Show programs 9-16 (Write), Monitor: MB13
MB_RANGE_17_24 = 1105  # Show programs 17-24 (Write), Monitor: MB14

# Pagination monitor
MB_RANGE_1_8_MONITOR = 12  # Monitor for range 1-8 active
MB_RANGE_9_16_MONITOR = 13  # Monitor for range 9-16 active
MB_RANGE_17_24_MONITOR = 14  # Monitor for range 17-24 active

# Program selection buttons -> navigate to Screen 25
MB_PROGRAM_1_FIND = 926  # Program 1 wash/drain find
MB_PROGRAM_2_FIND = 927  # Program 2 wash/drain find
MB_PROGRAM_3_FIND = 928  # Program 3 wash/drain find
MB_PROGRAM_4_FIND = 929  # Program 4 wash/drain find
MB_PROGRAM_5_FIND = 930  # Program 5 wash/drain find
MB_PROGRAM_6_FIND = 931  # Program 6 wash/drain find
MB_PROGRAM_7_FIND = 932  # Program 7 wash/drain find
MB_PROGRAM_8_FIND = 933  # Program 8 wash/drain find

# Program name display addresses (Character Display)
MI_FIND_PROGRAM_1_NAME = 400  # Program 1 name
MI_FIND_PROGRAM_2_NAME = 417  # Program 2 name
MI_FIND_PROGRAM_3_NAME = 434  # Program 3 name
MI_FIND_PROGRAM_4_NAME = 451  # Program 4 name
MI_FIND_PROGRAM_5_NAME = 1111  # Program 5 name
MI_FIND_PROGRAM_6_NAME = 1128  # Program 6 name
MI_FIND_PROGRAM_7_NAME = 1145  # Program 7 name
MI_FIND_PROGRAM_8_NAME = 1162  # Program 8 name

# ==============================================================================
# SCREEN 25 FIND RESULT
# ==============================================================================
# Result display MI addresses (10 results, 2 columns x 5 rows)
# Left column (programs 1-5): MI830, MI840, MI850, MI860, MI870
# Right column (programs 6-10): MI880, MI890, MI900, MI910, MI920
MI_FIND_RESULT_1 = 830   # MI830 - program 1 (left col, row 1)
MI_FIND_RESULT_2 = 840   # MI840 - program 2 (left col, row 2)
MI_FIND_RESULT_3 = 850   # MI850 - program 3 (left col, row 3)
MI_FIND_RESULT_4 = 860   # MI860 - program 4 (left col, row 4)
MI_FIND_RESULT_5 = 870   # MI870 - program 5 (left col, row 5)
MI_FIND_RESULT_6 = 880   # MI880 - program 6 (right col, row 1)
MI_FIND_RESULT_7 = 890   # MI890 - program 7 (right col, row 2)
MI_FIND_RESULT_8 = 900   # MI900 - program 8 (right col, row 3)
MI_FIND_RESULT_9 = 910   # MI910 - program 9 (right col, row 4)
MI_FIND_RESULT_10 = 920  # MI920 - program 10 (right col, row 5)

# ==============================================================================
# SCREEN 20 FINISH AUTO (MB1083)
# ==============================================================================
MB_FINISH_AUTO_CONFIRM = 1083  # Finish Auto confirm button - return to home

# ==============================================================================
# SCREEN 18 - ENTER BASKET DATA
# ==============================================================================
# Navigation / control
MB_S18_HOME = 901         # BB0001 – home button (to Screen 7)
MB_S18_SAVE = 1051        # BB0000 – save basket data (บันทึกตะกร้า)

# Bit Button: check basket toggle (BB / TS0000) – Momentary press
MB_S18_CHECK_BASKET = 240  # Write MB240 (momentary pulse)

# Bit Lamp: check basket indicator (BL0000)
MB_S18_CHECK_BASKET_LAMP = 241  # Monitor MB241

# Basket name Character Entry (TE0000-TE0007) – Write/Monitor MI
MI_S18_NAME_1 = 681   # TE0000 Basket name 1 (10 words = 20 chars)
MI_S18_NAME_2 = 687   # TE0001 Basket name 2
MI_S18_NAME_3 = 788   # TE0002 Basket name 3
MI_S18_NAME_4 = 794   # TE0003 Basket name 4
MI_S18_NAME_5 = 800   # TE0004 Basket name 5
MI_S18_NAME_6 = 806   # TE0005 Basket name 6
MI_S18_NAME_7 = 812   # TE0006 Basket name 7
MI_S18_NAME_8 = 818   # TE0007 Basket name 8

# Position sensor Write addresses (BB0002-BB0041)
# Basket 1 (MB971-MB975 = pos1-pos5)
MB_S18_B1_POS1_W = 971
MB_S18_B1_POS2_W = 972
MB_S18_B1_POS3_W = 973
MB_S18_B1_POS4_W = 974
MB_S18_B1_POS5_W = 975
# Basket 2 (MB976-MB980)
MB_S18_B2_POS1_W = 976
MB_S18_B2_POS2_W = 977
MB_S18_B2_POS3_W = 978
MB_S18_B2_POS4_W = 979
MB_S18_B2_POS5_W = 980
# Basket 3 (MB981-MB985)
MB_S18_B3_POS1_W = 981
MB_S18_B3_POS2_W = 982
MB_S18_B3_POS3_W = 983
MB_S18_B3_POS4_W = 984
MB_S18_B3_POS5_W = 985
# Basket 4 (MB986-MB990)
MB_S18_B4_POS1_W = 986
MB_S18_B4_POS2_W = 987
MB_S18_B4_POS3_W = 988
MB_S18_B4_POS4_W = 989
MB_S18_B4_POS5_W = 990
# Basket 5 (MB991-MB995)
MB_S18_B5_POS1_W = 991
MB_S18_B5_POS2_W = 992
MB_S18_B5_POS3_W = 993
MB_S18_B5_POS4_W = 994
MB_S18_B5_POS5_W = 995
# Basket 6 (MB1052-MB1056)
MB_S18_B6_POS1_W = 1052
MB_S18_B6_POS2_W = 1053
MB_S18_B6_POS3_W = 1054
MB_S18_B6_POS4_W = 1055
MB_S18_B6_POS5_W = 1056
# Basket 7 (MB1057-MB1061)
MB_S18_B7_POS1_W = 1057
MB_S18_B7_POS2_W = 1058
MB_S18_B7_POS3_W = 1059
MB_S18_B7_POS4_W = 1060
MB_S18_B7_POS5_W = 1061
# Basket 8 (MB1062-MB1066)
MB_S18_B8_POS1_W = 1062
MB_S18_B8_POS2_W = 1063
MB_S18_B8_POS3_W = 1064
MB_S18_B8_POS4_W = 1065
MB_S18_B8_POS5_W = 1066

# Position sensor Monitor addresses (MB52-MB76 for baskets 1-5, MB101-MB115 for baskets 6-8)
# Basket 1 pos1-pos5 (MB52-MB56)
MB_S18_B1_POS1_R = 52
MB_S18_B1_POS2_R = 53
MB_S18_B1_POS3_R = 54
MB_S18_B1_POS4_R = 55
MB_S18_B1_POS5_R = 56
# Basket 2 pos1-pos5 (MB57-MB61)
MB_S18_B2_POS1_R = 57
MB_S18_B2_POS2_R = 58
MB_S18_B2_POS3_R = 59
MB_S18_B2_POS4_R = 60
MB_S18_B2_POS5_R = 61
# Basket 3 pos1-pos5 (MB62-MB66)
MB_S18_B3_POS1_R = 62
MB_S18_B3_POS2_R = 63
MB_S18_B3_POS3_R = 64
MB_S18_B3_POS4_R = 65
MB_S18_B3_POS5_R = 66
# Basket 4 pos1-pos5 (MB67-MB71)
MB_S18_B4_POS1_R = 67
MB_S18_B4_POS2_R = 68
MB_S18_B4_POS3_R = 69
MB_S18_B4_POS4_R = 70
MB_S18_B4_POS5_R = 71
# Basket 5 pos1-pos5 (MB72-MB76)
MB_S18_B5_POS1_R = 72
MB_S18_B5_POS2_R = 73
MB_S18_B5_POS3_R = 74
MB_S18_B5_POS4_R = 75
MB_S18_B5_POS5_R = 76
# Basket 6 pos1-pos5 (MB101-MB105)
MB_S18_B6_POS1_R = 101
MB_S18_B6_POS2_R = 102
MB_S18_B6_POS3_R = 103
MB_S18_B6_POS4_R = 104
MB_S18_B6_POS5_R = 105
# Basket 7 pos1-pos5 (MB106-MB110)
MB_S18_B7_POS1_R = 106
MB_S18_B7_POS2_R = 107
MB_S18_B7_POS3_R = 108
MB_S18_B7_POS4_R = 109
MB_S18_B7_POS5_R = 110
# Basket 8 pos1-pos5 (MB111-MB115)
MB_S18_B8_POS1_R = 111
MB_S18_B8_POS2_R = 112
MB_S18_B8_POS3_R = 113
MB_S18_B8_POS4_R = 114
MB_S18_B8_POS5_R = 115

# ==============================================================================
# SCREEN 22 WARNING RUNTIME (MI188)
# ==============================================================================
MI_WARNING_RUNTIME_TYPE = 188  # Warning type: 0 = Machine Cycle RUNTIME, 1 = HEPA FILTER RUNTIME

# ==============================================================================
# EQUIPMENT STATUS (MB81-MB99)
# ==============================================================================
MB_PUMP_WASH = 81  # Wash pump running
MB_PUMP_DRAIN = 82  # Drain pump running
MB_HEATER_CHAMBER = 85  # Chamber heater on
MB_HEATER_AIR_DRY = 86  # Air dry heater on
MB_VALVE_WATER_COLD = 87  # Cold water valve open
MB_VALVE_WATER_HOT = 88  # Hot water valve open
MB_VALVE_CHEMICAL_1 = 89  # Chemical 1 valve open
MB_VALVE_CHEMICAL_2 = 90  # Chemical 2 valve open
MB_VALVE_CHEMICAL_3 = 91  # Chemical 3 valve open

# ==============================================================================
# PROCESS STATUS (MB200+)
# ==============================================================================
# NOTE: MB200 = alarm flag (machine fault/error), NOT a cycle-running indicator.
# Cycle active state is determined by MI1700 being in {9, 10, 12}, not MB200.
# MB_CYCLE_RUNNING is kept as an alias of MB_ALARM_STATUS for legacy references
# in data_mapper — do NOT use it to detect whether a wash cycle is running.
MB_CYCLE_RUNNING = 200   # alias of MB_ALARM_STATUS (MB200 = alarm, not cycle state)
MB_CYCLE_PAUSED = 201    # Cycle is paused
MB_CYCLE_COMPLETE = 202  # Cycle completed

# ==============================================================================
# PROCESS DATA (MI Addresses)
# ==============================================================================

# Data Logging (Screen 10 - Trend)
MI_DATA_LOG_START = 25  # MI25 - Start of 4-word data logging buffer
MI_DATA_LOG_CHAMBER_TEMP = 25  # Chamber temperature
MI_DATA_LOG_DRY_TEMP = 26  # Drying temperature
MI_DATA_LOG_TANK1_LEVEL = 27  # Tank 1 level
MI_DATA_LOG_TANK2_LEVEL = 28  # Tank 2 level

# Screen Control
MI_CURRENT_SCREEN = 1700  # Current screen number (PLC controlled)

# Program and Basket Information
MI_ACTIVE_BASKET_NAME = 79  # Active basket name
MI_ACTIVE_PROGRAM_NAME = 314  # Active program name

# User Information
MI_USER_ID = 85  # User ID for login

# Program Parameters (MI471-MI580)
MI_PROGRAM_PARAMS_START = 471
MI_PROGRAM_NAME = 490  # Program name (character data)

# Program Names (10 words each)
MI_PROGRAM_1_NAME = 1051
MI_PROGRAM_2_NAME = 1061
MI_PROGRAM_3_NAME = 1071
MI_PROGRAM_4_NAME = 1081
MI_PROGRAM_5_NAME = 1091
MI_PROGRAM_6_NAME = 1101

# Program Names for Select Enter Program screens (MI500-MI570, 10 words each)
MI_ENTER_PROGRAM_1_NAME = 500   # Program name slot 1
MI_ENTER_PROGRAM_2_NAME = 510   # Program name slot 2
MI_ENTER_PROGRAM_3_NAME = 520   # Program name slot 3
MI_ENTER_PROGRAM_4_NAME = 530   # Program name slot 4
MI_ENTER_PROGRAM_5_NAME = 540   # Program name slot 5
MI_ENTER_PROGRAM_6_NAME = 550   # Program name slot 6
MI_ENTER_PROGRAM_7_NAME = 560   # Program name slot 7
MI_ENTER_PROGRAM_8_NAME = 570   # Program name slot 8

# Cycle Information
MI_STEP_NUMBER = 10  # Current step number
MI_TIME_ELAPSED = 65  # Time elapsed in seconds
MI_TIME_REMAINING = 66  # Time remaining in seconds
MI_CYCLE_TIME_TOTAL = 69  # Total cycle time
MI_STEP_NAME = 77  # Current step name

# ==============================================================================
# SCREEN 09 AUTO - PROCESS DATA (MI addresses)
# ==============================================================================
# Temperature readings for Screen 09
MI_CHAMBER_TEMP_1_CURRENT = 25  # Current Chamber Temp 1
MI_CHAMBER_TEMP_1_SET = 26  # Set Chamber Temp 1
MI_DRYING_TEMP_CURRENT = 27  # Current Drying Temp
MI_DRYING_TEMP_SET = 28  # Set Drying Temp
MI_CHAMBER_TEMP_2_CURRENT = 71  # Current Chamber Temp 2

# Water tank states (0=Empty, 1=Low, 2=Medium, 3=Full)
MI_WATER_TANK_1_STATE = 61  # Water Tank 1 state (4 states)
MI_WATER_TANK_2_STATE = 62  # Water Tank 2 state (4 states)

# Time display for Screen 09
MI_PV_TIME_MINUTES = 65  # PV Time (Minutes)
MI_SV_TIME_MINUTES = 66  # SV Time (Minutes)
MI_PV_TIME_SECONDS = 69  # PV Time (Seconds)
MI_SV_TIME_SECONDS = 77  # SV Time 2 (Seconds)

# Remaining time display for Screen 09
MI_REMAIN_TIME_HOURS = 209    # Remaining time (Hours)
MI_REMAIN_TIME_MINUTES = 210  # Remaining time (Minutes)

# Character display addresses
MI_ACTIVE_STEP_NAME = 324  # Step name (10 registers for 20 chars)

# Counters
MI_CYCLE_COUNTER = 1005  # Total cycle count
MI_VERSION = 930  # Version display

# Temperature Readings
MI_CHAMBER_TEMP = 25
MI_DRY_TEMP = 27
MI_TANK1_TEMP = 28
MI_TANK2_TEMP = 29

# ==============================================================================
# HELPER FUNCTIONS
# ==============================================================================

def get_alarm_mb_addresses():
    """
    Get list of all alarm MB addresses

    Returns:
        list: List of alarm MB addresses
    """
    return [
        # Critical Alarms (Level 2)
        MB_ALARM_PHASE_SEQUENCE, MB_ALARM_AUX,
        MB_ALARM_HIGH_TEMP_CHAMBER, MB_ALARM_HIGH_TEMP_AIR_DRY,
        MB_ALARM_THERMAL_SAFETY,
        MB_ALARM_HIGH_TEMP_TANK1, MB_ALARM_HIGH_TEMP_TANK2,
        MB_ALARM_FAIL_FILLING_TANK1, MB_ALARM_FAIL_FILLING_TANK2,
        MB_ALARM_FAIL_FILLING_WATER3, MB_ALARM_FAIL_FILLING_WATER4,
        MB_ALARM_FAIL_LOADING_DOOR, MB_ALARM_FAIL_UNLOADING_DOOR,
        MB_ALARM_TANK1_MAX_LEVEL, MB_ALARM_TANK2_MAX_LEVEL,
        MB_ALARM_PT1000_TANK1, MB_ALARM_PT1000_TANK2,
        MB_ALARM_WATER_LOST,
        MB_ALARM_WASH_PUMP_PRESSURE,
        MB_ALARM_AIR_DRY_PRESSURE_SW1, MB_ALARM_AIR_DRY_PRESSURE_SW2,
        MB_ALARM_CHAMBER_PROBE_FAIL, MB_ALARM_DRY_PROBE_FAIL,
        MB_ALARM_CHEMICAL_FLOW_ERROR,
        MB_ALARM_CHAMBER_HEATING_FAIL, MB_ALARM_AIR_DRY_HEATING_FAIL,
        MB_ALARM_DRAIN_FAIL,
        MB_ALARM_HEATING_TANK1_FAIL, MB_ALARM_HEATING_TANK2_FAIL,
        MB_ALARM_TEMP_DIFF_CHAMBER,
        MB_ALARM_CHEMICAL1_TIMEOUT, MB_ALARM_CHEMICAL2_TIMEOUT,
        MB_ALARM_CHEMICAL3_TIMEOUT,
        MB_ALARM_PRINTER_SIGNAL_LOST,
        MB_ALARM_UNLOAD_DOOR_NOT_CLOSE,
        # Warning Alarms (Level 1)
        MB_ALARM_CHEMICAL1_LOW, MB_ALARM_CHEMICAL2_LOW, MB_ALARM_CHEMICAL3_LOW,
        MB_ALARM_AIR_SUPPLY_LOW, MB_ALARM_HEPA_FILTER,
        MB_ALARM_PRINTER_COMM_FAIL, MB_ALARM_LOW_MEMORY,
        MB_ALARM_NO_BASKET, MB_ALARM_DOOR_NOT_CLOSE,
    ]

def get_navigation_mb_addresses():
    """
    Get dictionary of navigation MB addresses

    Returns:
        dict: Navigation MB addresses mapped to screen numbers
    """
    return {
        MB_HOME: 1,
        MB_NAV_SCREEN_2: 2,
        MB_NAV_SCREEN_3: 3,
        MB_NAV_SCREEN_4: 4,
        MB_NAV_SCREEN_5: 5,
        MB_NAV_SCREEN_6: 6,
        MB_NAV_SCREEN_7: 7,
        MB_NAV_SCREEN_8: 8,
        MB_NAV_SCREEN_9: 9,
        MB_NAV_SCREEN_10: 10,
    }

def get_process_data_mi_addresses():
    """
    Get list of process data MI addresses for monitoring

    Returns:
        list: List of MI addresses for process monitoring
    """
    return [
        MI_CURRENT_SCREEN,
        MI_CHAMBER_TEMP, MI_DRY_TEMP,
        MI_TANK1_TEMP, MI_TANK2_TEMP,
        MI_STEP_NUMBER, MI_TIME_ELAPSED, MI_TIME_REMAINING,
        MI_CYCLE_TIME_TOTAL,
        MI_ACTIVE_PROGRAM_NAME, MI_ACTIVE_BASKET_NAME,
        MI_USER_ID,
        MI_CYCLE_COUNTER,
    ]

# ==============================================================================
# SCREEN 21 - ALARMS
# ==============================================================================
# Navigation
MB_POINT_OF_ALARM_NAV = 43    # Navigate to Screen 30 (Point of Alarm) from Screen 21
MB_HOME_SCREEN21      = 1094  # Home button on Screen 21 -> Screen 1
MB_SCROLL_UP_ALARM    = 1099  # Scroll up in alarm data log
MB_SCROLL_DOWN_ALARM  = 1100  # Scroll down in alarm data log

# Slide switch (data log scroll position, from PLC MI24 dynamic range block)
MI_ALARM_SLIDE_POSITION = 86  # MI86 - SW0000 scroll position

# Alarm data rows MI addresses: each row = 8 words (DD, MM, YYYY, HH, MIN, SS, Cycle, AlarmCode)
# Row 1 (newest displayed)
MI_ALARM_R1_DD    = 149
MI_ALARM_R1_MM    = 150
MI_ALARM_R1_YYYY  = 151
MI_ALARM_R1_HH    = 152
MI_ALARM_R1_MIN   = 153
MI_ALARM_R1_SS    = 154
MI_ALARM_R1_CYCLE = 155
MI_ALARM_R1_CODE  = 156

# Row 2
MI_ALARM_R2_DD    = 141
MI_ALARM_R2_MM    = 142
MI_ALARM_R2_YYYY  = 143
MI_ALARM_R2_HH    = 144
MI_ALARM_R2_MIN   = 145
MI_ALARM_R2_SS    = 146
MI_ALARM_R2_CYCLE = 147
MI_ALARM_R2_CODE  = 148

# Row 3
MI_ALARM_R3_DD    = 133
MI_ALARM_R3_MM    = 134
MI_ALARM_R3_YYYY  = 135
MI_ALARM_R3_HH    = 136
MI_ALARM_R3_MIN   = 137
MI_ALARM_R3_SS    = 138
MI_ALARM_R3_CYCLE = 139
MI_ALARM_R3_CODE  = 140

# Row 4
MI_ALARM_R4_DD    = 125
MI_ALARM_R4_MM    = 126
MI_ALARM_R4_YYYY  = 127
MI_ALARM_R4_HH    = 128
MI_ALARM_R4_MIN   = 129
MI_ALARM_R4_SS    = 130
MI_ALARM_R4_CYCLE = 131
MI_ALARM_R4_CODE  = 132

# Row 5
MI_ALARM_R5_DD    = 97
MI_ALARM_R5_MM    = 98
MI_ALARM_R5_YYYY  = 99
MI_ALARM_R5_HH    = 100
MI_ALARM_R5_MIN   = 121
MI_ALARM_R5_SS    = 122
MI_ALARM_R5_CYCLE = 123
MI_ALARM_R5_CODE  = 124

# Row 6 (oldest displayed)
MI_ALARM_R6_DD    = 89
MI_ALARM_R6_MM    = 90
MI_ALARM_R6_YYYY  = 91
MI_ALARM_R6_HH    = 92
MI_ALARM_R6_MIN   = 93
MI_ALARM_R6_SS    = 94
MI_ALARM_R6_CYCLE = 95
MI_ALARM_R6_CODE  = 96

# Alarm scroll dynamic max (Screen 21)
MI_ALARM_SLIDE_MAX = 24   # MI24 — dynamic max for scrollbar range block

# ==============================================================================
# SCREEN 06 / 12 / 30 - MANUAL GRAPHIC / AUTO DIAGRAM / POINT OF ALARM
# Shared batch ranges for equipment status and process data
# ==============================================================================

# Equipment monitor bits (contiguous batch)
MB_EQUIP_BATCH_START  = 81   # MB81 — first address of MB81-MB99 (19 bits)
MB_EQUIP_BATCH_COUNT  = 19   # count: MB81-MB99

# Tank / door / overflow bits (contiguous batch)
MB_TANK_DOOR_BATCH_START  = 120  # MB120 — first address of MB120-MB128 (9 bits)
MB_TANK_DOOR_BATCH_COUNT  =   9  # count: MB120-MB128

# Stop-All monitor bit
MB_STOP_ALL = 6   # MB6 — stop-all machine bit

# Chemical current levels (MI1-MI3)
MI_CHEM_LEVEL_BATCH_START = 1   # MI1 — first address
MI_CHEM_LEVEL_BATCH_COUNT = 3   # count: MI1-MI3

# Water level + set point registers (MI34-MI37)
# [0]=MI34 water3_cur  [1]=MI35 water4_cur  [2]=MI36 unused  [3]=MI37 water34_set
MI_WATER_34_BATCH_START = 34   # MI34
MI_WATER_34_BATCH_COUNT =  4   # count: MI34-MI37

# Heater set temperatures (MI63-MI64)
MI_HEATER_SET_BATCH_START = 63   # MI63
MI_HEATER_SET_BATCH_COUNT =  2   # count: MI63-MI64

# Tank current temperatures (individual, non-contiguous)
MI_TANK1_TEMP_CUR = 15   # MI15 — Tank 1 current temperature
MI_TANK2_TEMP_CUR = 18   # MI18 — Tank 2 current temperature
MI_CHAMBER_TEMP_SET = 71  # MI71 — Chamber temperature set point

# Chemical set levels (MI193-MI195)
MI_CHEM_SET_BATCH_START = 193   # MI193
MI_CHEM_SET_BATCH_COUNT =   3   # count: MI193-MI195

# ==============================================================================
# SCREEN 13 - ENTER WASH
# ==============================================================================

# Wash step data — 17 words per row
MI_S13_ROWS_1_4_START = 400   # MI400 — rows 1-4 (17 words × 4 = 68 words)
MI_S13_ROWS_1_4_COUNT =  68
MI_S13_ROWS_5_8_START = 1111  # MI1111 — rows 5-8 (17 words × 4 = 68 words)
MI_S13_ROWS_5_8_COUNT =  68

MI_S13_STEP_ROW1 = 78   # MI78 — step number for row 1

# Step numbers for rows 2-8 (MI167-MI173)
MI_S13_STEPS_2_8_START = 167   # MI167
MI_S13_STEPS_2_8_COUNT =   7   # count: MI167-MI173

# Save success overlay
MB_S13_SAVE_VISIBLE = 180   # MB180 — save success popup visibility

# Range tab monitor bits (MB12-MB14) — shared with Screen 24 write side
# (MB_RANGE_1_8_MONITOR=12, MB_RANGE_9_16_MONITOR=13, MB_RANGE_17_24_MONITOR=14 already defined)
MB_S13_RANGE_TAB_START = 12   # MB12 — first range tab monitor
MB_S13_RANGE_TAB_COUNT =  3   # count: MB12-MB14

# ==============================================================================
# SCREEN 14 - ENTER DRAIN
# ==============================================================================

# Drain step data — 11 words per row × 8 rows (MI700-MI787)
MI_S14_ROWS_START = 700   # MI700
MI_S14_ROWS_COUNT =  88   # 11 × 8

# Drain step numbers (MI180-MI187)
MI_S14_STEPS_START = 180   # MI180
MI_S14_STEPS_COUNT =   8   # count: MI180-MI187

# Drain type flags (MB700-MB707)
MB_S14_DRAIN_TYPE_START = 700   # MB700
MB_S14_DRAIN_TYPE_COUNT =   8   # count: MB700-MB707

# Range tab monitor bits (MB15-MB16)
MB_S14_RANGE_TAB_START = 15   # MB15
MB_S14_RANGE_TAB_COUNT =  2   # count: MB15-MB16

# Save success overlay
MB_S14_SAVE_VISIBLE = 181   # MB181 — save success popup visibility

# ==============================================================================
# SCREEN 16 - SELECT WASH PROGRAM (batch constants)
# ==============================================================================

# Program selection monitor bits (MB152-MB159) — also used by screens 17 and 19
MB_SEL_PROG_MON_BATCH_START = 152   # MB152
MB_SEL_PROG_MON_BATCH_COUNT =   8   # count: MB152-MB159

# Range tab monitor bits (MB20-MB22)
MB_SEL_WASH_RANGE_MON_BATCH_START = 20   # MB20
MB_SEL_WASH_RANGE_MON_BATCH_COUNT =  3   # count: MB20-MB22

# ==============================================================================
# SCREEN 17 - SELECT DRAIN PROGRAM (batch constants)
# ==============================================================================

# Range tab monitor bits (MB23-MB24)
MB_SEL_DRAIN_RANGE_MON_BATCH_START = 23   # MB23
MB_SEL_DRAIN_RANGE_MON_BATCH_COUNT =  2   # count: MB23-MB24

# ==============================================================================
# SCREEN 21 - ALARMS (batch start constants)
# ==============================================================================

# Alarm row batch start addresses (8 words per row)
MI_ALARM_R1_BATCH_START = 149   # MI149-MI156 (row 0 — newest)
MI_ALARM_R2_BATCH_START = 141   # MI141-MI148 (row 1)
MI_ALARM_R3_BATCH_START = 133   # MI133-MI140 (row 2)
MI_ALARM_R4_BATCH_START = 125   # MI125-MI132 (row 3)
MI_ALARM_ROW_BATCH_COUNT = 8    # words per row

# Row 5 (non-contiguous): addresses listed individually via MI_ALARM_R5_* constants

# ==============================================================================
# SCREEN 30 - POINT OF ALARM (specific additions)
# ==============================================================================

# Point-of-alarm time-stamp batch (MI174-MI177)
MI_S30_TIMESTAMP_START = 174   # MI174
MI_S30_TIMESTAMP_COUNT =   4   # count: MI174-MI177

# Alarm flag batch (MB136-MB137)
MB_S30_ALARM_FLAG_START = 136   # MB136 = MB_ALARM_PHASE_SEQUENCE
MB_S30_ALARM_FLAG_COUNT =   2   # count: MB136-MB137
