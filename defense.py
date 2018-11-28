


import globals
import detection_diagnosis
import mitigation_strategy
import VM
import math


def initializeAdaptive():

	total_num_vms = math.floor(globals.ISP_CAP*1.0/globals.VM_COMPUTE_CAP)
	for i in range(0, globals.INGRESS_LOC):
		globals.NUM_VMs.append(math.floor(total_num_vms*1.0//globals.INGRESS_LOC))
		queueSize = globals.NUM_PORTS_VM*globals.NUM_VMs[i]*globals.BUFF_SIZE
		dequeuePkts = globals.NUM_PORTS_VM*globals.NUM_VMs[i]
		vmCapacity = globals.NUM_VMs[i]*globals.VM_COMPUTE_CAP
		globals.INGRESS_CAP.append(VM.VM(vmCapacity,queueSize,dequeuePkts,vmCapacity))
		# globals.INGRESS_CAP[i] = math.floor(total_num_vms/globals.INGRESS_LOC)




def initialize():
	if(globals.DEFENSE_TYPE == "adaptive"):
		initializeAdaptive()


def ddosMiddlebox(pkt):
	if(globals.DEFENSE_TYPE == "static"):
		staticDefense(pkt)
	elif(globals.DEFENSE_TYPE == "dynamic"):
		dynamicDefense(pkt)
	elif(globals.DEFENSE_TYPE == "adaptive"):
		adaptiveDefense(pkt)




def staticDefense(pkt):


	detection_diagnosis.diagnoseTraffic(pkt)
	static_mitigation()




def dynamicDefense(pkt):
	detection_diagnosis.diagnoseTraffic(pkt)
	mitigation_strategy.dynamic_mitigation()

def adaptiveDefense(pkt):
	detection_diagnosis.diagnoseTraffic(pkt)
	mitigation_strategy.dynamic_mitigation()

