
from threading import Thread,Timer,Event, Lock
import globals

import sys
from legitimate_traffic import *
from attack_traffic import *
import isp
import queue
import json

class RepeatingThread(Thread):
    def __init__(self, event, t, name, m):
        Thread.__init__(self)
        self.stopped = event
        self.waitiingTime = t
        self.threadName = name
        self.method = m

    def run(self):
        while not self.stopped.wait(t):
            self.method()
            print self.threadName
            # call a function


def startNewWindow():

	for i in xrange(0,constants.INGRESS_LOC):
		
		globals.PREV_TRAFFIC_STATS[i]["total"] = constants.CURR_TRAFFIC_STATS[i]["total"]
		globals.CURR_TRAFFIC_STATS[i]["total"] = 0

		globals.PREV_TRAFFIC_STATS[i]["udp_flood"] = constants.CURR_TRAFFIC_STATS[i]["udp_flood"]
		globals.CURR_TRAFFIC_STATS[i]["udp_flood"] = 0

		globals.PREV_TRAFFIC_STATS[i]["tcp_syn"] = constants.CURR_TRAFFIC_STATS[i]["tcp_syn"]
		globals.CURR_TRAFFIC_STATS[i]["tcp_syn"] = 0

	
	constants.WINDOW_COUNTER += 1
	isp.countDroppedPackets()
	isp.wastedResources()




def readConfigureFile(file):
	data = ""
	with open(file, encoding='utf-8') as data_file:
    	data = json.loads(data_file.read())

    globals.ATTACK_TYPE = data.attackerType
    globals.DEFENSE_TYPE = data.defenseType
    globals.INGRESS_LOC = data.ingreeLoc
    globals.BUFF_SIZE = data.buffSize
    globals.VM_COMPUTE_CAP = data.VMCapacity
    globals.ISP_CAP = data.ISPCapacity
    globals.NUM_PORTS_VM = data.numPortsVM
    globals.ATTACKER_CAP = data.attackerCapacity
    globals.LEG_TRAFFIC_MODEL = data.legitimateTraffic
    globals.EPOCH_TIME = data.epochTime
    globals.PROCESSING_DELAY = data.processingDelay




def main():
	

	configurationFile = sys.argv[1]
	readConfigureFile(configurationFile)
	isp.initializeISP()

	# start legitimate traffic thread
	threading.Thread(target=flowGen).start()

	# start attack traffic thread
	# threading.Thread(target=attackTrafficGen, args=[attackerType]).start()
	


	# start per epoch stat collection for next epoch prediction
	stopStats = Event()
	statsThread = RepeatingThread(stopStats,globals.EPOCH_TIME,"stats per epoch collection thread",startNewWindow)
	statsThread.start()


	#start dequeuing pkts after delay equivalent to processing delay
	stopProcess = Event()
	processingThread = RepeatingThread(stopProcess,globals.PROCESSING_DELAY,"packet processingThread",queue.processPacket)
	processingThread.start()

#	 this will stop the timer
	# stopFlag.set()


if __name__ == "__main__":
    main()


