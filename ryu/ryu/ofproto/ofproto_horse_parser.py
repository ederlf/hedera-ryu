import struct
from ryu.base import app_manager
from ryu.lib.pack_utils import msg_pack_into
from ryu.controller import event,ofp_event
import ryu.ofproto.ofproto_v1_3_parser as ofproto_parser
import ryu.ofproto.ofproto_v1_3 as ofproto
import ryu.ofproto.ofproto_horse as horseproto
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller.handler import set_ev_cls

class HorseSimHeader(ofproto_parser.OFPExperimenter):


    def __init__(self, datapath, subtype, data = None):
        super(HorseHeader, self).__init__(datapath, HORSE_EXPERIMENTER_ID,subtype, data)

class HorseSimTime(HorseSimHeader):
    def __init__(self,datapath, sim_time):
        super(HorseSimTime,self).__init__(datapath, HORSE_SIM_TIME)
        self.sim_time = sim_time 

    @classmethod
    def parser(cls,datapath, buf, offset):
        sim_time = struct.unpack_from(HORSE_SIM_TIME_PACK_STR , buf, offset)
        return cls(datapath, sim_time)

class EventHorseEventTime(event.EventBase):
    def __init__(self,reply):
        
        self.reply = reply

class HorseEventMessageHandler(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto.OFP_VERSION]

    _EVENTS = [
        EventHorseEventTime,
        ]

    def __init__(self):
        self.name = "HorseEventMessage"
        super(HorseEventMessageHandler,self).__init__()

    @set_ev_cls(ofp_event.EventOFPExperimenter, MAIN_DISPATCHER)
    def experimenter_message_handler(self,ev):
        msg = ev.msg
        datapath = msg.datapath
        experimenter = msg.experimenter
        exp_type = msg.exp_type
        print experimenter

        if experimenter == HORSE_EXPERIMENTER_ID:
            if exp_type == HORSE_SIM_TIME:
                reply = HorseSimTime.parser(datapath, msg.data, 0)
                self.send_event_to_observers(EventHorseEventTime(reply))
            else:
                LOG.error("unknown subtype %d" %exp_type)
            

    @set_ev_cls(ofp_event.EventOFPErrorMsg, MAIN_DISPATCHER)
    def ofp_error_handler(self,ev):
        msg = ev.msg
        datapath = msg.datapath
        err_type = msg.type
        LOG.info("Error type %s from switch %016x" %(err_type,datapath.id) )