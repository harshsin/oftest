# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template const.py
# Do not modify

OFP_VERSION = 2

# Identifiers from group macro_definitions
OFP_MAX_TABLE_NAME_LEN = 32
OFP_MAX_PORT_NAME_LEN = 16
OFP_TCP_PORT = 6653
OFP_SSL_PORT = 6653
OFP_ETH_ALEN = 6
OFP_DEFAULT_MISS_SEND_LEN = 128
OFPFW_ICMP_TYPE = 64
OFPFW_ICMP_CODE = 128
OFP_DL_TYPE_ETH2_CUTOFF = 1536
OFP_DL_TYPE_NOT_ETH_TYPE = 1535
OFP_VLAN_NONE = 0
OFPMT_STANDARD_LENGTH = 88
OFP_FLOW_PERMANENT = 0
OFP_DEFAULT_PRIORITY = 32768
DESC_STR_LEN = 256
SERIAL_NUM_LEN = 32
OFPQ_ALL = 4294967295
OFPQ_MIN_RATE_UNCFG = 65535

# Identifiers from group of_bsn_pdu_slot_num_t
BSN_PDU_SLOT_NUM_ANY = 255

of_bsn_pdu_slot_num_t_map = {
    255: 'BSN_PDU_SLOT_NUM_ANY',
}

# Identifiers from group ofp_action_type
OFPAT_OUTPUT = 0
OFPAT_SET_VLAN_VID = 1
OFPAT_SET_VLAN_PCP = 2
OFPAT_SET_DL_SRC = 3
OFPAT_SET_DL_DST = 4
OFPAT_SET_NW_SRC = 5
OFPAT_SET_NW_DST = 6
OFPAT_SET_NW_TOS = 7
OFPAT_SET_NW_ECN = 8
OFPAT_SET_TP_SRC = 9
OFPAT_SET_TP_DST = 10
OFPAT_COPY_TTL_OUT = 11
OFPAT_COPY_TTL_IN = 12
OFPAT_SET_MPLS_LABEL = 13
OFPAT_SET_MPLS_TC = 14
OFPAT_SET_MPLS_TTL = 15
OFPAT_DEC_MPLS_TTL = 16
OFPAT_PUSH_VLAN = 17
OFPAT_POP_VLAN = 18
OFPAT_PUSH_MPLS = 19
OFPAT_POP_MPLS = 20
OFPAT_SET_QUEUE = 21
OFPAT_GROUP = 22
OFPAT_SET_NW_TTL = 23
OFPAT_DEC_NW_TTL = 24
OFPAT_EXPERIMENTER = 65535

ofp_action_type_map = {
    0: 'OFPAT_OUTPUT',
    1: 'OFPAT_SET_VLAN_VID',
    2: 'OFPAT_SET_VLAN_PCP',
    3: 'OFPAT_SET_DL_SRC',
    4: 'OFPAT_SET_DL_DST',
    5: 'OFPAT_SET_NW_SRC',
    6: 'OFPAT_SET_NW_DST',
    7: 'OFPAT_SET_NW_TOS',
    8: 'OFPAT_SET_NW_ECN',
    9: 'OFPAT_SET_TP_SRC',
    10: 'OFPAT_SET_TP_DST',
    11: 'OFPAT_COPY_TTL_OUT',
    12: 'OFPAT_COPY_TTL_IN',
    13: 'OFPAT_SET_MPLS_LABEL',
    14: 'OFPAT_SET_MPLS_TC',
    15: 'OFPAT_SET_MPLS_TTL',
    16: 'OFPAT_DEC_MPLS_TTL',
    17: 'OFPAT_PUSH_VLAN',
    18: 'OFPAT_POP_VLAN',
    19: 'OFPAT_PUSH_MPLS',
    20: 'OFPAT_POP_MPLS',
    21: 'OFPAT_SET_QUEUE',
    22: 'OFPAT_GROUP',
    23: 'OFPAT_SET_NW_TTL',
    24: 'OFPAT_DEC_NW_TTL',
    65535: 'OFPAT_EXPERIMENTER',
}

# Identifiers from group ofp_bad_action_code
OFPBAC_BAD_TYPE = 0
OFPBAC_BAD_LEN = 1
OFPBAC_BAD_EXPERIMENTER = 2
OFPBAC_BAD_EXPERIMENTER_TYPE = 3
OFPBAC_BAD_OUT_PORT = 4
OFPBAC_BAD_ARGUMENT = 5
OFPBAC_EPERM = 6
OFPBAC_TOO_MANY = 7
OFPBAC_BAD_QUEUE = 8
OFPBAC_BAD_OUT_GROUP = 9
OFPBAC_MATCH_INCONSISTENT = 10
OFPBAC_UNSUPPORTED_ORDER = 11
OFPBAC_BAD_TAG = 12

ofp_bad_action_code_map = {
    0: 'OFPBAC_BAD_TYPE',
    1: 'OFPBAC_BAD_LEN',
    2: 'OFPBAC_BAD_EXPERIMENTER',
    3: 'OFPBAC_BAD_EXPERIMENTER_TYPE',
    4: 'OFPBAC_BAD_OUT_PORT',
    5: 'OFPBAC_BAD_ARGUMENT',
    6: 'OFPBAC_EPERM',
    7: 'OFPBAC_TOO_MANY',
    8: 'OFPBAC_BAD_QUEUE',
    9: 'OFPBAC_BAD_OUT_GROUP',
    10: 'OFPBAC_MATCH_INCONSISTENT',
    11: 'OFPBAC_UNSUPPORTED_ORDER',
    12: 'OFPBAC_BAD_TAG',
}

# Identifiers from group ofp_bad_instruction_code
OFPBIC_UNKNOWN_INST = 0
OFPBIC_UNSUP_INST = 1
OFPBIC_BAD_TABLE_ID = 2
OFPBIC_UNSUP_METADATA = 3
OFPBIC_UNSUP_METADATA_MASK = 4
OFPBIC_UNSUP_EXP_INST = 5

ofp_bad_instruction_code_map = {
    0: 'OFPBIC_UNKNOWN_INST',
    1: 'OFPBIC_UNSUP_INST',
    2: 'OFPBIC_BAD_TABLE_ID',
    3: 'OFPBIC_UNSUP_METADATA',
    4: 'OFPBIC_UNSUP_METADATA_MASK',
    5: 'OFPBIC_UNSUP_EXP_INST',
}

# Identifiers from group ofp_bad_match_code
OFPBMC_BAD_TYPE = 0
OFPBMC_BAD_LEN = 1
OFPBMC_BAD_TAG = 2
OFPBMC_BAD_DL_ADDR_MASK = 3
OFPBMC_BAD_NW_ADDR_MASK = 4
OFPBMC_BAD_WILDCARDS = 5
OFPBMC_BAD_FIELD = 6
OFPBMC_BAD_VALUE = 7

ofp_bad_match_code_map = {
    0: 'OFPBMC_BAD_TYPE',
    1: 'OFPBMC_BAD_LEN',
    2: 'OFPBMC_BAD_TAG',
    3: 'OFPBMC_BAD_DL_ADDR_MASK',
    4: 'OFPBMC_BAD_NW_ADDR_MASK',
    5: 'OFPBMC_BAD_WILDCARDS',
    6: 'OFPBMC_BAD_FIELD',
    7: 'OFPBMC_BAD_VALUE',
}

# Identifiers from group ofp_bad_request_code
OFPBRC_BAD_VERSION = 0
OFPBRC_BAD_TYPE = 1
OFPBRC_BAD_STAT = 2
OFPBRC_BAD_EXPERIMENTER = 3
OFPBRC_BAD_SUBTYPE = 4
OFPBRC_EPERM = 5
OFPBRC_BAD_LEN = 6
OFPBRC_BUFFER_EMPTY = 7
OFPBRC_BUFFER_UNKNOWN = 8
OFPBRC_BAD_TABLE_ID = 9

ofp_bad_request_code_map = {
    0: 'OFPBRC_BAD_VERSION',
    1: 'OFPBRC_BAD_TYPE',
    2: 'OFPBRC_BAD_STAT',
    3: 'OFPBRC_BAD_EXPERIMENTER',
    4: 'OFPBRC_BAD_SUBTYPE',
    5: 'OFPBRC_EPERM',
    6: 'OFPBRC_BAD_LEN',
    7: 'OFPBRC_BUFFER_EMPTY',
    8: 'OFPBRC_BUFFER_UNKNOWN',
    9: 'OFPBRC_BAD_TABLE_ID',
}

# Identifiers from group ofp_bsn_vport_q_in_q_untagged
OF_BSN_VPORT_Q_IN_Q_UNTAGGED = 65535

ofp_bsn_vport_q_in_q_untagged_map = {
    65535: 'OF_BSN_VPORT_Q_IN_Q_UNTAGGED',
}

# Identifiers from group ofp_bsn_vport_status
OF_BSN_VPORT_STATUS_OK = 0
OF_BSN_VPORT_STATUS_FAILED = 1

ofp_bsn_vport_status_map = {
    0: 'OF_BSN_VPORT_STATUS_OK',
    1: 'OF_BSN_VPORT_STATUS_FAILED',
}

# Identifiers from group ofp_capabilities
OFPC_FLOW_STATS = 1
OFPC_TABLE_STATS = 2
OFPC_PORT_STATS = 4
OFPC_GROUP_STATS = 8
OFPC_IP_REASM = 32
OFPC_QUEUE_STATS = 64
OFPC_ARP_MATCH_IP = 128

ofp_capabilities_map = {
    1: 'OFPC_FLOW_STATS',
    2: 'OFPC_TABLE_STATS',
    4: 'OFPC_PORT_STATS',
    8: 'OFPC_GROUP_STATS',
    32: 'OFPC_IP_REASM',
    64: 'OFPC_QUEUE_STATS',
    128: 'OFPC_ARP_MATCH_IP',
}

# Identifiers from group ofp_config_flags
OFPC_FRAG_NORMAL = 0
OFPC_FRAG_DROP = 1
OFPC_FRAG_REASM = 2
OFPC_FRAG_MASK = 3
OFPC_INVALID_TTL_TO_CONTROLLER = 4

ofp_config_flags_map = {
    0: 'OFPC_FRAG_NORMAL',
    1: 'OFPC_FRAG_DROP',
    2: 'OFPC_FRAG_REASM',
    3: 'OFPC_FRAG_MASK',
    4: 'OFPC_INVALID_TTL_TO_CONTROLLER',
}

# Identifiers from group ofp_error_type
OFPET_HELLO_FAILED = 0
OFPET_BAD_REQUEST = 1
OFPET_BAD_ACTION = 2
OFPET_BAD_INSTRUCTION = 3
OFPET_BAD_MATCH = 4
OFPET_FLOW_MOD_FAILED = 5
OFPET_GROUP_MOD_FAILED = 6
OFPET_PORT_MOD_FAILED = 7
OFPET_TABLE_MOD_FAILED = 8
OFPET_QUEUE_OP_FAILED = 9
OFPET_SWITCH_CONFIG_FAILED = 10

ofp_error_type_map = {
    0: 'OFPET_HELLO_FAILED',
    1: 'OFPET_BAD_REQUEST',
    2: 'OFPET_BAD_ACTION',
    3: 'OFPET_BAD_INSTRUCTION',
    4: 'OFPET_BAD_MATCH',
    5: 'OFPET_FLOW_MOD_FAILED',
    6: 'OFPET_GROUP_MOD_FAILED',
    7: 'OFPET_PORT_MOD_FAILED',
    8: 'OFPET_TABLE_MOD_FAILED',
    9: 'OFPET_QUEUE_OP_FAILED',
    10: 'OFPET_SWITCH_CONFIG_FAILED',
}

# Identifiers from group ofp_flow_mod_command
OFPFC_ADD = 0
OFPFC_MODIFY = 1
OFPFC_MODIFY_STRICT = 2
OFPFC_DELETE = 3
OFPFC_DELETE_STRICT = 4

ofp_flow_mod_command_map = {
    0: 'OFPFC_ADD',
    1: 'OFPFC_MODIFY',
    2: 'OFPFC_MODIFY_STRICT',
    3: 'OFPFC_DELETE',
    4: 'OFPFC_DELETE_STRICT',
}

# Identifiers from group ofp_flow_mod_failed_code
OFPFMFC_UNKNOWN = 0
OFPFMFC_TABLE_FULL = 1
OFPFMFC_BAD_TABLE_ID = 2
OFPFMFC_OVERLAP = 3
OFPFMFC_EPERM = 4
OFPFMFC_BAD_TIMEOUT = 5
OFPFMFC_BAD_COMMAND = 6

ofp_flow_mod_failed_code_map = {
    0: 'OFPFMFC_UNKNOWN',
    1: 'OFPFMFC_TABLE_FULL',
    2: 'OFPFMFC_BAD_TABLE_ID',
    3: 'OFPFMFC_OVERLAP',
    4: 'OFPFMFC_EPERM',
    5: 'OFPFMFC_BAD_TIMEOUT',
    6: 'OFPFMFC_BAD_COMMAND',
}

# Identifiers from group ofp_flow_mod_flags
OFPFF_SEND_FLOW_REM = 1
OFPFF_CHECK_OVERLAP = 2

ofp_flow_mod_flags_map = {
    1: 'OFPFF_SEND_FLOW_REM',
    2: 'OFPFF_CHECK_OVERLAP',
}

# Identifiers from group ofp_flow_removed_reason
OFPRR_IDLE_TIMEOUT = 0
OFPRR_HARD_TIMEOUT = 1
OFPRR_DELETE = 2
OFPRR_GROUP_DELETE = 3

ofp_flow_removed_reason_map = {
    0: 'OFPRR_IDLE_TIMEOUT',
    1: 'OFPRR_HARD_TIMEOUT',
    2: 'OFPRR_DELETE',
    3: 'OFPRR_GROUP_DELETE',
}

# Identifiers from group ofp_flow_wildcards
OFPFW_IN_PORT = 1
OFPFW_DL_VLAN = 2
OFPFW_DL_VLAN_PCP = 4
OFPFW_DL_TYPE = 8
OFPFW_NW_TOS = 16
OFPFW_NW_PROTO = 32
OFPFW_TP_SRC = 64
OFPFW_TP_DST = 128
OFPFW_MPLS_LABEL = 256
OFPFW_MPLS_TC = 512
OFPFW_ALL = 1023

ofp_flow_wildcards_map = {
    1: 'OFPFW_IN_PORT',
    2: 'OFPFW_DL_VLAN',
    4: 'OFPFW_DL_VLAN_PCP',
    8: 'OFPFW_DL_TYPE',
    16: 'OFPFW_NW_TOS',
    32: 'OFPFW_NW_PROTO',
    64: 'OFPFW_TP_SRC',
    128: 'OFPFW_TP_DST',
    256: 'OFPFW_MPLS_LABEL',
    512: 'OFPFW_MPLS_TC',
}

# Identifiers from group ofp_group
OFPG_MAX = 4294967040
OFPG_ALL = 4294967292
OFPG_ANY = 4294967295

ofp_group_map = {
    4294967040: 'OFPG_MAX',
    4294967292: 'OFPG_ALL',
    4294967295: 'OFPG_ANY',
}

# Identifiers from group ofp_group_mod_command
OFPGC_ADD = 0
OFPGC_MODIFY = 1
OFPGC_DELETE = 2

ofp_group_mod_command_map = {
    0: 'OFPGC_ADD',
    1: 'OFPGC_MODIFY',
    2: 'OFPGC_DELETE',
}

# Identifiers from group ofp_group_mod_failed_code
OFPGMFC_GROUP_EXISTS = 0
OFPGMFC_INVALID_GROUP = 1
OFPGMFC_WEIGHT_UNSUPPORTED = 2
OFPGMFC_OUT_OF_GROUPS = 3
OFPGMFC_OUT_OF_BUCKETS = 4
OFPGMFC_CHAINING_UNSUPPORTED = 5
OFPGMFC_WATCH_UNSUPPORTED = 6
OFPGMFC_LOOP = 7
OFPGMFC_UNKNOWN_GROUP = 8

ofp_group_mod_failed_code_map = {
    0: 'OFPGMFC_GROUP_EXISTS',
    1: 'OFPGMFC_INVALID_GROUP',
    2: 'OFPGMFC_WEIGHT_UNSUPPORTED',
    3: 'OFPGMFC_OUT_OF_GROUPS',
    4: 'OFPGMFC_OUT_OF_BUCKETS',
    5: 'OFPGMFC_CHAINING_UNSUPPORTED',
    6: 'OFPGMFC_WATCH_UNSUPPORTED',
    7: 'OFPGMFC_LOOP',
    8: 'OFPGMFC_UNKNOWN_GROUP',
}

# Identifiers from group ofp_group_type
OFPGT_ALL = 0
OFPGT_SELECT = 1
OFPGT_INDIRECT = 2
OFPGT_FF = 3

ofp_group_type_map = {
    0: 'OFPGT_ALL',
    1: 'OFPGT_SELECT',
    2: 'OFPGT_INDIRECT',
    3: 'OFPGT_FF',
}

# Identifiers from group ofp_hello_failed_code
OFPHFC_INCOMPATIBLE = 0
OFPHFC_EPERM = 1

ofp_hello_failed_code_map = {
    0: 'OFPHFC_INCOMPATIBLE',
    1: 'OFPHFC_EPERM',
}

# Identifiers from group ofp_instruction_type
OFPIT_GOTO_TABLE = 1
OFPIT_WRITE_METADATA = 2
OFPIT_WRITE_ACTIONS = 3
OFPIT_APPLY_ACTIONS = 4
OFPIT_CLEAR_ACTIONS = 5
OFPIT_EXPERIMENTER = 65535

ofp_instruction_type_map = {
    1: 'OFPIT_GOTO_TABLE',
    2: 'OFPIT_WRITE_METADATA',
    3: 'OFPIT_WRITE_ACTIONS',
    4: 'OFPIT_APPLY_ACTIONS',
    5: 'OFPIT_CLEAR_ACTIONS',
    65535: 'OFPIT_EXPERIMENTER',
}

# Identifiers from group ofp_match_type
OFPMT_STANDARD = 0

ofp_match_type_map = {
    0: 'OFPMT_STANDARD',
}

# Identifiers from group ofp_packet_in_reason
OFPR_NO_MATCH = 0
OFPR_ACTION = 1

ofp_packet_in_reason_map = {
    0: 'OFPR_NO_MATCH',
    1: 'OFPR_ACTION',
}

# Identifiers from group ofp_port
OFPP_MAX = 4294967040
OFPP_IN_PORT = 4294967288
OFPP_TABLE = 4294967289
OFPP_NORMAL = 4294967290
OFPP_FLOOD = 4294967291
OFPP_ALL = 4294967292
OFPP_CONTROLLER = 4294967293
OFPP_LOCAL = 4294967294
OFPP_ANY = 4294967295

ofp_port_map = {
    4294967040: 'OFPP_MAX',
    4294967288: 'OFPP_IN_PORT',
    4294967289: 'OFPP_TABLE',
    4294967290: 'OFPP_NORMAL',
    4294967291: 'OFPP_FLOOD',
    4294967292: 'OFPP_ALL',
    4294967293: 'OFPP_CONTROLLER',
    4294967294: 'OFPP_LOCAL',
    4294967295: 'OFPP_ANY',
}

# Identifiers from group ofp_port_config
OFPPC_PORT_DOWN = 1
OFPPC_NO_RECV = 4
OFPPC_NO_FWD = 32
OFPPC_NO_PACKET_IN = 64
OFPPC_BSN_MIRROR_DEST = 2147483648

ofp_port_config_map = {
    1: 'OFPPC_PORT_DOWN',
    4: 'OFPPC_NO_RECV',
    32: 'OFPPC_NO_FWD',
    64: 'OFPPC_NO_PACKET_IN',
    2147483648: 'OFPPC_BSN_MIRROR_DEST',
}

# Identifiers from group ofp_port_features
OFPPF_10MB_HD = 1
OFPPF_10MB_FD = 2
OFPPF_100MB_HD = 4
OFPPF_100MB_FD = 8
OFPPF_1GB_HD = 16
OFPPF_1GB_FD = 32
OFPPF_10GB_FD = 64
OFPPF_40GB_FD = 128
OFPPF_100GB_FD = 256
OFPPF_1TB_FD = 512
OFPPF_OTHER = 1024
OFPPF_COPPER = 2048
OFPPF_FIBER = 4096
OFPPF_AUTONEG = 8192
OFPPF_PAUSE = 16384
OFPPF_PAUSE_ASYM = 32768

ofp_port_features_map = {
    1: 'OFPPF_10MB_HD',
    2: 'OFPPF_10MB_FD',
    4: 'OFPPF_100MB_HD',
    8: 'OFPPF_100MB_FD',
    16: 'OFPPF_1GB_HD',
    32: 'OFPPF_1GB_FD',
    64: 'OFPPF_10GB_FD',
    128: 'OFPPF_40GB_FD',
    256: 'OFPPF_100GB_FD',
    512: 'OFPPF_1TB_FD',
    1024: 'OFPPF_OTHER',
    2048: 'OFPPF_COPPER',
    4096: 'OFPPF_FIBER',
    8192: 'OFPPF_AUTONEG',
    16384: 'OFPPF_PAUSE',
    32768: 'OFPPF_PAUSE_ASYM',
}

# Identifiers from group ofp_port_mod_failed_code
OFPPMFC_BAD_PORT = 0
OFPPMFC_BAD_HW_ADDR = 1
OFPPMFC_BAD_CONFIG = 2
OFPPMFC_BAD_ADVERTISE = 3

ofp_port_mod_failed_code_map = {
    0: 'OFPPMFC_BAD_PORT',
    1: 'OFPPMFC_BAD_HW_ADDR',
    2: 'OFPPMFC_BAD_CONFIG',
    3: 'OFPPMFC_BAD_ADVERTISE',
}

# Identifiers from group ofp_port_reason
OFPPR_ADD = 0
OFPPR_DELETE = 1
OFPPR_MODIFY = 2

ofp_port_reason_map = {
    0: 'OFPPR_ADD',
    1: 'OFPPR_DELETE',
    2: 'OFPPR_MODIFY',
}

# Identifiers from group ofp_port_state
OFPPS_LINK_DOWN = 1
OFPPS_BLOCKED = 2
OFPPS_LIVE = 4

ofp_port_state_map = {
    1: 'OFPPS_LINK_DOWN',
    2: 'OFPPS_BLOCKED',
    4: 'OFPPS_LIVE',
}

# Identifiers from group ofp_queue_op_failed_code
OFPQOFC_BAD_PORT = 0
OFPQOFC_BAD_QUEUE = 1
OFPQOFC_EPERM = 2

ofp_queue_op_failed_code_map = {
    0: 'OFPQOFC_BAD_PORT',
    1: 'OFPQOFC_BAD_QUEUE',
    2: 'OFPQOFC_EPERM',
}

# Identifiers from group ofp_queue_properties
OFPQT_NONE = 0
OFPQT_MIN_RATE = 1

ofp_queue_properties_map = {
    0: 'OFPQT_NONE',
    1: 'OFPQT_MIN_RATE',
}

# Identifiers from group ofp_stats_reply_flags
OFPSF_REPLY_MORE = 1

ofp_stats_reply_flags_map = {
    1: 'OFPSF_REPLY_MORE',
}

# Identifiers from group ofp_stats_request_flags

ofp_stats_request_flags_map = {
}

# Identifiers from group ofp_stats_type
OFPST_DESC = 0
OFPST_FLOW = 1
OFPST_AGGREGATE = 2
OFPST_TABLE = 3
OFPST_PORT = 4
OFPST_QUEUE = 5
OFPST_GROUP = 6
OFPST_GROUP_DESC = 7
OFPST_EXPERIMENTER = 65535

ofp_stats_type_map = {
    0: 'OFPST_DESC',
    1: 'OFPST_FLOW',
    2: 'OFPST_AGGREGATE',
    3: 'OFPST_TABLE',
    4: 'OFPST_PORT',
    5: 'OFPST_QUEUE',
    6: 'OFPST_GROUP',
    7: 'OFPST_GROUP_DESC',
    65535: 'OFPST_EXPERIMENTER',
}

# Identifiers from group ofp_switch_config_failed_code
OFPSCFC_BAD_FLAGS = 0
OFPSCFC_BAD_LEN = 1

ofp_switch_config_failed_code_map = {
    0: 'OFPSCFC_BAD_FLAGS',
    1: 'OFPSCFC_BAD_LEN',
}

# Identifiers from group ofp_table_config
OFPTC_TABLE_MISS_CONTROLLER = 0
OFPTC_TABLE_MISS_CONTINUE = 1
OFPTC_TABLE_MISS_DROP = 2
OFPTC_TABLE_MISS_MASK = 3

ofp_table_config_map = {
    0: 'OFPTC_TABLE_MISS_CONTROLLER',
    1: 'OFPTC_TABLE_MISS_CONTINUE',
    2: 'OFPTC_TABLE_MISS_DROP',
    3: 'OFPTC_TABLE_MISS_MASK',
}

# Identifiers from group ofp_table_mod_failed_code
OFPTMFC_BAD_TABLE = 0
OFPTMFC_BAD_CONFIG = 1

ofp_table_mod_failed_code_map = {
    0: 'OFPTMFC_BAD_TABLE',
    1: 'OFPTMFC_BAD_CONFIG',
}

# Identifiers from group ofp_type
OFPT_HELLO = 0
OFPT_ERROR = 1
OFPT_ECHO_REQUEST = 2
OFPT_ECHO_REPLY = 3
OFPT_EXPERIMENTER = 4
OFPT_FEATURES_REQUEST = 5
OFPT_FEATURES_REPLY = 6
OFPT_GET_CONFIG_REQUEST = 7
OFPT_GET_CONFIG_REPLY = 8
OFPT_SET_CONFIG = 9
OFPT_PACKET_IN = 10
OFPT_FLOW_REMOVED = 11
OFPT_PORT_STATUS = 12
OFPT_PACKET_OUT = 13
OFPT_FLOW_MOD = 14
OFPT_GROUP_MOD = 15
OFPT_PORT_MOD = 16
OFPT_TABLE_MOD = 17
OFPT_STATS_REQUEST = 18
OFPT_STATS_REPLY = 19
OFPT_BARRIER_REQUEST = 20
OFPT_BARRIER_REPLY = 21
OFPT_QUEUE_GET_CONFIG_REQUEST = 22
OFPT_QUEUE_GET_CONFIG_REPLY = 23

ofp_type_map = {
    0: 'OFPT_HELLO',
    1: 'OFPT_ERROR',
    2: 'OFPT_ECHO_REQUEST',
    3: 'OFPT_ECHO_REPLY',
    4: 'OFPT_EXPERIMENTER',
    5: 'OFPT_FEATURES_REQUEST',
    6: 'OFPT_FEATURES_REPLY',
    7: 'OFPT_GET_CONFIG_REQUEST',
    8: 'OFPT_GET_CONFIG_REPLY',
    9: 'OFPT_SET_CONFIG',
    10: 'OFPT_PACKET_IN',
    11: 'OFPT_FLOW_REMOVED',
    12: 'OFPT_PORT_STATUS',
    13: 'OFPT_PACKET_OUT',
    14: 'OFPT_FLOW_MOD',
    15: 'OFPT_GROUP_MOD',
    16: 'OFPT_PORT_MOD',
    17: 'OFPT_TABLE_MOD',
    18: 'OFPT_STATS_REQUEST',
    19: 'OFPT_STATS_REPLY',
    20: 'OFPT_BARRIER_REQUEST',
    21: 'OFPT_BARRIER_REPLY',
    22: 'OFPT_QUEUE_GET_CONFIG_REQUEST',
    23: 'OFPT_QUEUE_GET_CONFIG_REPLY',
}

# Identifiers from group ofp_vlan_id
OFPVID_ANY = 65534
OFPVID_NONE = 65535

ofp_vlan_id_map = {
    65534: 'OFPVID_ANY',
    65535: 'OFPVID_NONE',
}

