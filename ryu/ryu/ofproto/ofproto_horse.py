import sys
from struct import calcsize
from ryu.lib import type_desc
from ryu.ofproto.ofproto_common import OFP_HEADER_SIZE

HORSE_EXPERIMENTER_ID = 0xF0A1F0A1

#Horse simulator messages
HORSE_SIM_TIME = 0

HORSE_SIM_TIME_PACK_STR = '!Q'
HORSE_SIM_TIME_SIZE = 8
assert calcsize(HORSE_SIM_TIME_PACK_STR) == HORSE_SIM_TIME_SIZE
