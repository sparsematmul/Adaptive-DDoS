


import globals
import detection_diagnosis
import mitigation_strategy



def initializeAdaptive():

	total_num_vms = math.floor(globals.ISP_CAP*1.0/globals.VM_COMPUTE_CAP)
	for i in xrange(0, globals.INGRESS_LOC):
		globals.NUM_OF_VM[i] = math.floor(total_num_vms/globals.INGRESS_LOC)



def initialize(defenseType):
	if(defenseType == "adaptive")
		initializeAdaptive()


def ddosMiddlebox(pkt):
	if(constants.DEFENSE_TYPE == "static"):
		staticDefense(pkt)
	elif(constants.DEFENSE_TYPE == "dynamic"):
		dynamicDefense(pkt)




def staticDefense(pkt):


	detection_diagnosis.diagnoseTraffic(pkt)
	static_mitigation()




def dynamicDefense(pkt):
	detection_diagnosis.diagnoseTraffic(pkt)
	mitigation_strategy.dynamic_mitigation()
