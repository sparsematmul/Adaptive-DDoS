
from threading import Thread,Timer,Event
import constants

import sys
from legitimate_traffic import *
from attack_traffic import *
import isp

class RepeatingThread(Thread):
    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        while not self.stopped.wait(1):
            print("my thread")
            startNewWindow()
            # call a function


def startNewWindow():

	for i in xrange(0,constants.INGRESS_LOC):
		constants.PREV_TRAFFIC_STATS[i]["total"] = constants.CURR_TRAFFIC_STATS[i]["total"]
		constants.CURR_TRAFFIC_STATS[i]["total"] = 0

		constants.PREV_TRAFFIC_STATS[i]["udp_flood"] = constants.CURR_TRAFFIC_STATS[i]["udp_flood"]
		constants.CURR_TRAFFIC_STATS[i]["udp_flood"] = 0

		constants.PREV_TRAFFIC_STATS[i]["tcp_syn"] = constants.CURR_TRAFFIC_STATS[i]["tcp_syn"]
		constants.CURR_TRAFFIC_STATS[i]["tcp_syn"] = 0

	
	constants.WINDOW_COUNTER += 1
	isp.countDroppedPackets()
	isp.wastedResources()


def main():
	
	attackerType = sys.argv[1]
	constants.DEFENSE_TYPE = sys.argv[2]
	constants.INGRESS_LOC = int(sys.argv[3])
	BUFF_SIZE = int(sys.argv[4])
	constants.TOTAL_CAPACITY_ISP = int(sys.argv[5])
	isp.initializeISP(BUFF_SIZE)
	# if(len(sys.argv) == 5):
	# 	numPkts = int(sys.argv[4])
	# 	threading.Thread(target=flowGen, args=[numPkts]).start()
	# elif(len(sys.argv) == 6):
	# 	mode = sys.argv[5]

	threading.Thread(target=flowGen, args=[1000,"simple"]).start()
	# else:
	# threading.Thread(target=flowGen).start()

	
	# threading.Thread(target=attackTrafficGen, args=[attackerType]).start()
	

	stopFlag = Event()
	thread = RepeatingThread(stopFlag)
	thread.start()
#	 this will stop the timer
	# stopFlag.set()


if __name__ == "__main__":
    main()


