# This file contains the toplogy of the ISP
# including the number of ingress locations,
# the total capacity of the ISP

import constants
import math

prevDropCount = [0] * constants.INGRESS_LOC
prevReceiveCount = [0] * constants.INGRESS_LOC

def initializeISP():

	for i in xrange(0,constants.INGRESS_LOC):
		# constants.CAPACITY.append(math.floor(constants.TOTAL_CAPACITY_ISP/constants.INGRESS_LOC))
		constants.CURR_TRAFFIC_STATS.append({})
		constants.CURR_TRAFFIC_STATS[i]["total"] = 0
		constants.CURR_TRAFFIC_STATS[i]["udp_flood"] = 0
		constants.CURR_TRAFFIC_STATS[i]["tcp_syn"] = 0

		constants.PREV_TRAFFIC_STATS.append({})
		constants.PREV_TRAFFIC_STATS[i]["total"] = 0
		constants.PREV_TRAFFIC_STATS[i]["udp_flood"] = 0
		constants.PREV_TRAFFIC_STATS[i]["tcp_syn"] = 0

		constants.PEAK_TRAFFIC.append(0)
		constants.MIN_TRAFFIC.append(float('inf'))

		# constants.BUFF_SIZE.append(buff)



# def latencyIncurred():

def countDroppedPackets():

	global prevDropCount
	for i in xrange(0,globals.INGRESS_LOC):
		print constants.legitimateDropCounter[i] - prevDropCount[i]
		prevDropCount[i] = constants.legitimateDropCounter[i] 

def wastedResources():

	for i in xrange(0,globals.INGRESS_LOC):
		receivedPktsPerWIndow =  globals.receiveCounter[i] - prevReceiveCount[i]
		prevReceiveCount[i] = globals.receiveCounter[i] 
		wastedCap = receivedPktsPerWIndow*globals.PKT_LEN - CAPACITY[i]
		print wastedCap


