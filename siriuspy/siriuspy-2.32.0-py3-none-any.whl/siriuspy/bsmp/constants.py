"""BSMP Constants."""

# --- Reserved Address IDs ---
ID_ADDR_MASTER: int = 0
ID_ADDR_BROADCAST: int = 255

# --- Reserved Group IDs ---
ID_STD_GROUP_ALL: int = 0
ID_STD_GROUP_READONLY: int = 1
ID_STD_GROUP_WRITE: int = 2

# --- Query Commands ---
CMD_CMD_QUERY_PROTOCOL_VERSION: int = 0x00
CMD_PROTOCOL_VERSION: int = 0x01
CMD_CMD_QUERY_LIST_OF_VARIABLES: int = 0x02
CMD_LIST_OF_VARIABLE: int = 0x03
CMD_QUERY_LIST_OF_GROUP_OF_VARIABLES: int = 0x04
CMD_LIST_OF_GROUP_OF_VARIABLES: int = 0x05
CMD_QUERY_GROUP_OF_VARIABLES: int = 0x06
CMD_GROUP_OF_VARIABLES: int = 0x07
CMD_QUERY_LIST_OF_CURVES: int = 0x08
CMD_LIST_OF_CURVES: int = 0x09
CMD_QUERY_CURVE_CHECKSUM: int = 0x0A
CMD_CURVE_CHECKSUM: int = 0x0B
CMD_QUERY_LIST_OF_FUNCTIONS: int = 0x0C
CMD_LIST_OF_FUNCTIONS: int = 0x0D

# --- Reading Commands ---
CMD_READ_VARIABLE: int = 0x10
CMD_VARIABLE_VALUE: int = 0x11
CMD_READ_GROUP_OF_VARIABLES: int = 0x12
CMD_GROUP_OF_VARIABLES_VALUE: int = 0x13

# --- Writing Commands ---
CMD_WRITE_VARIABLE: int = 0x20
CMD_WRITE_GROUP_OF_VARIABLES: int = 0x22
CMD_BINARY_OPERATION_IN_A_VARIABLE: int = 0x24
CMD_BINARY_OPERATION_IN_A_GROUP: int = 0x26
CMD_WRITE_AND_READ_VARIABLES: int = 0x28

# --- Group of Variables Manipulation Commnads ---
CMD_CREATE_GROUP_OF_VARIABLES: int = 0x30
CMD_REMOVE_ALL_GROUPS_OF_VARIABLES: int = 0x32

# --- Curve Transfer Commands ---
CMD_REQUEST_CURVE_BLOCK: int = 0x40
CMD_CURVE_BLOCK: int = 0x41
CMD_RECALCULATE_CURVE_CHECKSUM: int = 0x42

# --- Function Execution Commands ---
CMD_EXECUTE_FUNCTION: int = 0x50
CMD_FUNCTION_RETURN: int = 0x51
CMD_FUNCTION_ERROR: int = 0x53

# --- Error Commands ---
ACK_OK: int = 0xE0
ACK_MALFORMED_MESSAGE: int = 0xE1
ACK_OPERATION_NOT_SUPPORTED: int = 0xE2
ACK_INVALID_ID: int = 0xE3
ACK_INVALID_VALUE: int = 0xE4
ACK_INVALID_PAYLOAD_SIZE: int = 0xE5
ACK_READ_ONLY: int = 0xE6
ACK_INSUFFICIENT_MEMORY: int = 0xE7
ACK_RESOURCE_BUSY: int = 0xE8
