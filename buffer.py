import time 
import packet 
import threading
import globals
import defense
import queue
import math
# import logging

# lock = threading.Lock()

Buffer = queue.Queue()

def enqueuePacket(pkt):

   global Buffer
   globals.LOCK_INGRESS_CAP[pkt.ingress].acquire()
   if ((globals.INGRESS_CAP[pkt.ingress].availableBuffSpace - pkt.packet_len) > 0):

      globals.LOCK_RECEIVE_COUNTER[pkt.ingress].acquire()
      globals.RECEIVE_COUNTER[pkt.ingress] +=1
      globals.LOCK_RECEIVE_COUNTER[pkt.ingress].release()
      Buffer.put(pkt)
      globals.INGRESS_CAP[pkt.ingress].availableBuffSpace -= pkt.packet_len
      globals.DEBUG_LOGGER.debug("Function: enqueuePacket - Packet Added to Queue, Available Buffer space at %(pkt.ingress) = %(globals.INGRESS_CAP[pkt.ingress].availableBuffSpace)" )

   else:
      dropPacket(pkt)
   globals.LOCK_INGRESS_CAP[pkt.ingress].release()


def processPacket():
   global Buffer
   for i in range(0,globals.INGRESS_LOC):
      globals.LOCK_INGRESS_CAP[i].acquire()
      pktsToDequeue = globals.INGRESS_CAP[i].numOfDequeuePkts
      globals.LOCK_RECEIVE_COUNTER[i].acquire()
      if(globals.RECEIVE_COUNTER[i] > 0):
         if(pktsToDequeue*globals.PKT_LEN > globals.INGRESS_CAP[i].cap - globals.INGRESS_CAP[i].availableBuffSpace):
            pktsToDequeue = math.floor((globals.INGRESS_CAP[i].cap - globals.INGRESS_CAP[i].availableBuffSpace)*1.0/globals.PKT_LEN)
         globals.INGRESS_CAP[i].availableBuffSpace += globals.PKT_LEN*pktsToDequeue
         globals.DEBUG_LOGGER.debug("Function: processPacket - %(str(pktsToDequeue)) packets processed, Available Buffer space at %(pkt.ingress) = %(globals.INGRESS_CAP[pkt.ingress].availableBuffSpace)")
         for i in range(0,int(pktsToDequeue)):
            pkt = Buffer.get()
            defense.ddosMiddlebox(pkt)
      globals.LOCK_RECEIVE_COUNTER[i].release()
      globals.LOCK_INGRESS_CAP[i].release()

         
   
   
      # globals.processCounter[pkt.dst] += INGRESS_CAP[pkt.dst].numOfDequeuePkts


def dropPacket(pkt):
   if (pkt.attack_flag == 0):
      
      globals.LOCK_legitimateDropCounter[pkt.ingress].acquire()
      globals.legitimateDropCounter[pkt.ingress]+=1
      globals.DEBUG_LOGGER.debug("Function: dropPacket - Legitimate packet dropped, legitimateDropCounter = %(globals.legitimateDropCounter)")
      globals.LOCK_legitimateDropCounter[pkt.ingress].release()

   else:
      globals.attackDropCounter[pkt.ingress] +=1
      globals.DEBUG_LOGGER.debug("Function: dropPacket - Attack packet dropped, attackDropCounter = %(globals.attackDropCounter)")




