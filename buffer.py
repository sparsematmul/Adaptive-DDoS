import time 
import packet 
import threading
import globals
import defense
import queue
import math
import logging

# lock = threading.Lock()

Buffer = queue.Queue()

def enqueuePacket(pkt):
   # print len(globals.INGRESS_CAP)
   global Buffer
   if ((globals.INGRESS_CAP[pkt.ingress].availableBuffSpace - pkt.packet_len) > 0):
      # lock[pkt.dst].acquire()
      globals.RECEIVE_COUNTER[pkt.ingress] +=1
      Buffer.put(pkt)
      globals.INGRESS_CAP[pkt.ingress].availableBuffSpace -= pkt.packet_len

      # lock[pkt.dst].release()
   else:
      dropPacket(pkt)


def processPacket():
   global Buffer
   for i in range(0,globals.INGRESS_LOC):
      pktsToDequeue = globals.INGRESS_CAP[i].numOfDequeuePkts
      if(globals.RECEIVE_COUNTER[i] > 0):
         if(globals.INGRESS_CAP[i].numOfDequeuePkts*globals.PKT_LEN > globals.INGRESS_CAP[i].cap - globals.INGRESS_CAP[i].availableBuffSpace):
            pktsToDequeue = math.floor((globals.INGRESS_CAP[i].cap - globals.INGRESS_CAP[i].availableBuffSpace)*1.0/globals.PKT_LEN)
         globals.INGRESS_CAP[i].availableBuffSpace += globals.PKT_LEN*pktsToDequeue
         for i in range(0,int(pktsToDequeue)):
            pkt = Buffer.get()
            defense.ddosMiddlebox(pkt)
         
   
   
      # globals.processCounter[pkt.dst] += INGRESS_CAP[pkt.dst].numOfDequeuePkts


def dropPacket(pkt):
   if (pkt.attack_flag == 0):
      globals.legitimateDropCounter[pkt.ingress]+=1
   else:
      globals.attackDropCounter[pkt.ingress] +=1



