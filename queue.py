import time 
import packet 
import threading
import globals
import defense
import Queue
import math
# lock = threading.Lock()

queue = Queue.Queue()

def enqueuePacket(pkt):
   # print len(globals.INGRESS_CAP)
   global queue
   if ((globals.INGRESS_CAP[pkt.ingress].availableBuffSpace - pkt.packet_len) > 0):
      # lock[pkt.dst].acquire()
      globals.RECEIVE_COUNTER[pkt.ingress] +=1
      queue.put(pkt)
      globals.INGRESS_CAP[pkt.ingress].availableBuffSpace -= pkt.packet_len

      # lock[pkt.dst].release()
   else:
      dropPacket(pkt)


def processPacket():
   global queue
   for i in xrange(0,globals.INGRESS_LOC):
      pktsToDequeue = globals.INGRESS_CAP[i].numOfDequeuePkts
      if(globals.RECEIVE_COUNTER[i] > 0):
         if(globals.INGRESS_CAP[i].numOfDequeuePkts*globals.PKT_LEN > globals.INGRESS_CAP[i].cap - globals.INGRESS_CAP[i].availableBuffSpace):
            pktsToDequeue = math.floor((globals.INGRESS_CAP[i].cap - globals.INGRESS_CAP[i].availableBuffSpace)*1.0/globals.PKT_LEN)
         globals.INGRESS_CAP[i].availableBuffSpace += globals.PKT_LEN*pktsToDequeue
         for i in xrange(0,int(pktsToDequeue)):
            pkt = queue.get()
            defense.ddosMiddlebox(pkt)
         
   
   
      # globals.processCounter[pkt.dst] += INGRESS_CAP[pkt.dst].numOfDequeuePkts


def dropPacket(pkt):
   if (pkt.attack_flag == 0):
      globals.legitimateDropCounter[pkt.ingress]+=1
   else:
      globals.attackDropCounter[pkt.ingress] +=1



