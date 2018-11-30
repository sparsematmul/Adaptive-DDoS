

import lock
import globals





def initializeIngressLocks():
	for i in range(0,globals.INGRESS_LOC):
		# globals.LOCK_PREV_TRAFFIC_STATS.append({})
		# globals.LOCK_PREV_TRAFFIC_STATS[i]["total"] = lock.Lock()
		


		globals.LOCK_CURR_TRAFFIC_STATS.append(lock.Lock())
	
	
		globals.LOCK_legitimateDropCounter.append(lock.Lock())
		globals.LOCK_RECEIVE_COUNTER.append(lock.Lock())

		# globals.LOCK_INGRESS_AVAILABLE_CAP.append(lock.Lock())
		globals.LOCK_INGRESS_CAP.append(lock.Lock())


		globals.LOCK_NUM_VM.append(lock.lock())







def initializeLocks():
	initializeIngressLocks()
	
