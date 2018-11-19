import time 
import packet 
import threading
import constants

# lock = threading.Lock()



def enqueuePacket(pkt):
   if ((constants.BUFF_SIZE[pkt.dst] - pkt.packet_len) > 0):
      # lock[pkt.dst].acquire()
      constants.receiveCounter[pkt.dst] +=1
      constants.BUFF_SIZE[pkt.dst] -= pkt.packet_len
      # lock[pkt.dst].release()
   else:
      dropPacket(pkt)


def processePacket(pkt,processingdelay):
   if(receiveCounter > 0):
      time.sleep(processingdelay)
      constants.BUFF_SIZE[pkt.dst] += pcket_len
      constants.processCounter[pkt.dst] +=1


def dropPacket(pkt):
   if (pkt.attack_flag == 0):
      constants.legitimateDropCounter[pkt.dst]+=1
   else:
      constants.attackDropCounter[pkt.dst] +=1



