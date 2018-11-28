
import constants
import random

# this file contains the three various mitigation techniques
# that can be used by the defense layer, all traffic from the 
# diagnosis layer comes into the mitigation layer which 
# mitigates and creates flow rules etc.

# def load

# def static_mitigation():

	# add rules to controller to drop the attack traffic
	# tags traffic as attack or legitimate


# 1


def dynamic_mitigation():

	for i in xrange(0,constants.INGRESS_LOC):
		
		if(constants.CURR_TRAFFIC_STATS[i]["total"] > constants.PEAK_TRAFFIC[i]):
			constants.PEAK_TRAFFIC[i] = constants.CURR_TRAFFIC_STATUS[i]["total"]


		if(constants.CURR_TRAFFIC_STATS[i]["total"] < constants.MIN_TRAFFIC[i]):
			constants.MIN_TRAFFIC[i] = constants.CURR_TRAFFIC_STATS[i]["total"]


		constants.CAPACITY[i] = random.uniform(constants.MIN_TRAFFIC[i],constants.PEAK_TRAFFIC[i])


def adaptive_mitigation():

	for i in xrange(0,constants.INGRESS_LOC):
		
		if(constants.CURR_TRAFFIC_STATS[i]["total"] > constants.PEAK_TRAFFIC[i]):
			constants.PEAK_TRAFFIC[i] = constants.CURR_TRAFFIC_STATUS[i]["total"]


		if(constants.CURR_TRAFFIC_STATS[i]["total"] < constants.MIN_TRAFFIC[i]):
			constants.MIN_TRAFFIC[i] = constants.CURR_TRAFFIC_STATS[i]["total"]


		constants.CAPACITY[i] = random.uniform(constants.MIN_TRAFFIC[i],constants.PEAK_TRAFFIC[i])

	# set flow rules for new capacity in the controller
	# create packet rules for attack packers which is essentially the static mitigation


# def adaptive_mitigation(traffic_stats):


	



