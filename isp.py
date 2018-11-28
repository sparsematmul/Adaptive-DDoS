# This file contains the toplogy of the ISP
# including the number of ingress locations,
# the total capacity of the ISP

import globals
import math

prevDropCount = [0] * globals.INGRESS_LOC
prevReceiveCount = [0] * globals.INGRESS_LOC

def initializeISP():

	logging.debug("Function: initializeISP- Initializing TRAFFIC_STATS variables")

	for i in range(0,globals.INGRESS_LOC):
		# globals.CAPACITY.append(math.floor(globals.TOTAL_CAPACITY_ISP/globals.INGRESS_LOC))
		globals.CURR_TRAFFIC_STATS.append({})
		globals.CURR_TRAFFIC_STATS[i]["total"] = 0
		globals.CURR_TRAFFIC_STATS[i]["udp_flood"] = 0
		globals.CURR_TRAFFIC_STATS[i]["tcp_syn"] = 0

		globals.PREV_TRAFFIC_STATS.append({})
		globals.PREV_TRAFFIC_STATS[i]["total"] = 0
		globals.PREV_TRAFFIC_STATS[i]["udp_flood"] = 0
		globals.PREV_TRAFFIC_STATS[i]["tcp_syn"] = 0

		globals.PEAK_TRAFFIC.append(0)
		globals.MIN_TRAFFIC.append(float('inf'))

		# globals.BUFF_SIZE.append(buff)



# def latencyIncurred():

def countDroppedPackets():

	global prevDropCount
	for i in range(0,globals.INGRESS_LOC):
		dropped = globals.legitimateDropCounter[i] - prevDropCount[i]
		prevDropCount[i] = globals.legitimateDropCounter[i]
		logging.debug("Function: countDroppedPackets, dropped Packets at ingress %(i) are %(dropped)")
 

def wastedResources():

	for i in range(0,globals.INGRESS_LOC):
		receivedPktsPerWIndow =  globals.RECEIVE_COUNTER[i] - prevReceiveCount[i]
		prevReceiveCount[i] = globals.RECEIVE_COUNTER[i] 
		wastedCap = receivedPktsPerWIndow*globals.PKT_LEN - globals.INGRESS_CAP[i].cap
		logging.debug("Function: wastedResources, wasted resources at ingress %(i) are %(wastedCap)")
		# print wastedCap


