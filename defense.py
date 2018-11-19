


import constants
import detection_diagnosis
import mitigation_strategy

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
