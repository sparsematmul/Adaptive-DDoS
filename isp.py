# This file contains the toplogy of the ISP
# including the number of ingress locations,
# the total capacity of the ISP

import constants
import math

prevDropCount = [0] * constants.INGRESS_LOC
prevReceiveCount = [0] * constants.INGRESS_LOC
def initializeISP(buff):

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

		constants.BUFF_SIZE.append(buff)





def countDroppedPackets():

	global prevDropCount
	for i in xrange(0,constants.INGRESS_LOC):
		print constants.legitimateDropCounter[i] - prevDropCount[i]
		prevDropCount[i] = constants.legitimateDropCounter[i] 

def wastedResources(pkt):

	for i in xrange(0,constants.INGRESS_LOC):
		receivedPktsPerWIndow =  constants.receiveCounter[i] - prevReceiveCount[i]
		prevReceiveCount[i] = constants.receiveCounter[i] 
		wastedCap = receivedPktsPerWIndow - CAPACITY[i]
		print wastedCap


