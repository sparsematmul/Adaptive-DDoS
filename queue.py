import time 
import packet 
import threading

lock = threading.Lock()


def enqueuePacket(pkt):
   if ((BUFFSIZE[pkt.dst] - pkt.packet_len) > 0):
      print_lock[pkt.dst].acquire()
      receiveCounter[pkt.dst] +=1
      BUFFSIZE[pkt.dst] -= pkt.packet_len
      print_lock[pkt.dst].release()
   else:
      dropPacket(pkt)


def processePacket(pkt,processingdelay):
   time.sleep(1/processingdelay)
   BUFFSIZE += pcket_len
   processCounter+=1


def dropPacket(pkt):
   if (pkt.attack_flag == 0):
      legitimate_dropCounter[pkt.dst]+=1
   else:
      attack_dropCounter[pkt.dst] +=1

