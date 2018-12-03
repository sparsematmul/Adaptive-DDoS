
package main

import (
	"math/rand"
)


func changeCapacity(i int,newCap float64) {
	NUM_VMs[i] = int(newCap*1.0/CONFIGURATION.VM_COMPUTE_CAP)
	LOCK_INGRESS_CAP[i].Lock()
	oldCap := INGRESS_CAP[i].cap
	INGRESS_CAP[i].cap = newCap
	
	INGRESS_CAP[i].numOfDequeuePkts = int(CONFIGURATION.NUM_NIC_VM*NUM_VMs[i])
	INGRESS_CAP[i].vmQueue = float64(INGRESS_CAP[i].numOfDequeuePkts)*CONFIGURATION.BUFF_SIZE
	INGRESS_CAP[i].availableBuffSpace = newCap - (oldCap - INGRESS_CAP[i].availableBuffSpace)
	_DEBUG.Printf("Function: change Capacity, capacity at ingress %d = %f",i, newCap) 
	LOCK_INGRESS_CAP[i].Unlock()

}

func dynamicMitigation() {

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		
		LOCK_CURR_TRAFFIC_STATS[i].Lock()
		if((float64(CURR_TRAFFIC_STATS[i]["total"])) * PKT_LEN > PEAK_TRAFFIC[i]) {
			PEAK_TRAFFIC[i] = float64(CURR_TRAFFIC_STATS[i]["total"]) * PKT_LEN
		}


		if(float64(CURR_TRAFFIC_STATS[i]["total"])* PKT_LEN < MIN_TRAFFIC[i]) {
			MIN_TRAFFIC[i] = float64(CURR_TRAFFIC_STATS[i]["total"]) * PKT_LEN
		}

		LOCK_CURR_TRAFFIC_STATS[i].Unlock()
		// # INGRESS_CAP[i] = random.uniform(MIN_TRAFFIC[i],PEAK_TRAFFIC[i])
		changeCapacity(i,(rand.Float64() * (PEAK_TRAFFIC[i] - MIN_TRAFFIC[i])) + MIN_TRAFFIC[i])
		

	}
}

func staticMitigation() {

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		
		LOCK_CURR_TRAFFIC_STATS[i].Lock()
		if((float64(CURR_TRAFFIC_STATS[i]["total"])) * PKT_LEN > PEAK_TRAFFIC[i]) {
			PEAK_TRAFFIC[i] = float64(CURR_TRAFFIC_STATS[i]["total"]) * PKT_LEN
		}


		if(float64(CURR_TRAFFIC_STATS[i]["total"])* PKT_LEN < MIN_TRAFFIC[i]) {
			MIN_TRAFFIC[i] = float64(CURR_TRAFFIC_STATS[i]["total"]) * PKT_LEN
		}

		LOCK_CURR_TRAFFIC_STATS[i].Unlock()
		// # INGRESS_CAP[i] = random.uniform(MIN_TRAFFIC[i],PEAK_TRAFFIC[i])
		changeCapacity(i,(rand.Float64() * (PEAK_TRAFFIC[i] - MIN_TRAFFIC[i])) + MIN_TRAFFIC[i])
		

	}
}

func adaptiveMitigation() {

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		
		LOCK_CURR_TRAFFIC_STATS[i].Lock()
		if((float64(CURR_TRAFFIC_STATS[i]["total"])) * PKT_LEN > PEAK_TRAFFIC[i]) {
			PEAK_TRAFFIC[i] = float64(CURR_TRAFFIC_STATS[i]["total"]) * PKT_LEN
		}


		if(float64(CURR_TRAFFIC_STATS[i]["total"])* PKT_LEN < MIN_TRAFFIC[i]) {
			MIN_TRAFFIC[i] = float64(CURR_TRAFFIC_STATS[i]["total"]) * PKT_LEN
		}

		LOCK_CURR_TRAFFIC_STATS[i].Unlock()
		// # INGRESS_CAP[i] = random.uniform(MIN_TRAFFIC[i],PEAK_TRAFFIC[i])
		changeCapacity(i,(rand.Float64() * (PEAK_TRAFFIC[i] - MIN_TRAFFIC[i])) + MIN_TRAFFIC[i])
		

	}
}