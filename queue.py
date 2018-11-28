import time 
import packet 
import threading
import globals
# import 

# lock = threading.Lock()



def enqueuePacket(pkt):
   # print len(globals.INGRESS_CAP)
   if ((globals.INGRESS_CAP[pkt.ingress].availableBuffSpace - pkt.packet_len) > 0):
      # lock[pkt.dst].acquire()
      globals.RECEIVE_COUNTER[pkt.ingress] +=1
      globals.INGRESS_CAP[pkt.ingress].availableBuffSpace -= pkt.packet_len
      
      # lock[pkt.dst].release()
   else:
      dropPacket(pkt)


def processPacket():
   for i in xrange(0,globals.INGRESS_LOC):
      if(globals.RECEIVE_COUNTER[i] > 0):
         globals.INGRESS_CAP[i].availableBuffSpace += globals.PKT_LEN*globals.INGRESS_CAP[i].numOfDequeuePkts
         if(globals.INGRESS_CAP[i].availableBuffSpace > globals.INGRESS_CAP[i].vmQueue):
            globals.INGRESS_CAP[i].availableBuffSpace = globals.INGRESS_CAP[i].vmQueue
      
      # constants.processCounter[pkt.dst] += INGRESS_CAP[pkt.dst].numOfDequeuePkts


def dropPacket(pkt):
   if (pkt.attack_flag == 0):
      globals.legitimateDropCounter[pkt.ingress]+=1
   else:
      globals.attackDropCounter[pkt.ingress] +=1



