package main

import "github.com/golang-collections/go-datastructures/fifo"


var (
	prevDropCount []int 
	prevReceiveCount []int
)


func initializeISP() {

	_DEBUG.Printf("Function: initializeISP- Initializing TRAFFIC_STATS variables")
	m := make(map[string]int)
	m["total"] = 0
	m["udp_flood"] = 0
	m["tcp_syn"] = 0
	m["dns_amp"] = 0

	PEAK_TRAFFIC = make([]float64,CONFIGURATION.INGRESS_LOC)
	MIN_TRAFFIC = make([]float64,CONFIGURATION.INGRESS_LOC)
	RECEIVE_COUNTER = make([]int,CONFIGURATION.INGRESS_LOC)
	legitimateDropCounter = make([]int,CONFIGURATION.INGRESS_LOC)
	
	prevDropCount = make([]int,CONFIGURATION.INGRESS_LOC)
	prevReceiveCount = make([]int,CONFIGURATION.INGRESS_LOC)

	processCounter = make([]int,CONFIGURATION.INGRESS_LOC)
	// BUFFER = make ([]fifo.Queue, CONFIGURATION.INGRESS_LOC)
	BUFFER = make([]*fifo.Queue, CONFIGURATION.INGRESS_LOC)

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		CURR_TRAFFIC_STATS = append(CURR_TRAFFIC_STATS,m) 
		PREV_TRAFFIC_STATS = append(PREV_TRAFFIC_STATS,m)
		BUFFER[i] = fifo.NewQueue()
		
	}


}


func countDroppedPackets() {

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		
		LOCK_legitimateDropCounter[i].Lock()
		dropped := legitimateDropCounter[i] - prevDropCount[i]
		prevDropCount[i] = legitimateDropCounter[i]
		
		
		_DEBUG.Printf("Function: countDroppedPackets, dropped Packets at ingress %d = %d",i, dropped)
		_INFO.Printf("Dropped Packets at ingress %d = %d",i, dropped)
		LOCK_legitimateDropCounter[i].Unlock()
		// fmt.Printf("%d",dropped)
	}
	// # loggings.error('This should go to both console and file')
}

func wastedResources() {

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		
		LOCK_RECEIVE_COUNTER[i].Lock()
		receivedPktsPerWIndow :=  RECEIVE_COUNTER[i] - prevReceiveCount[i]
		prevReceiveCount[i] = RECEIVE_COUNTER[i] 
		LOCK_RECEIVE_COUNTER[i].Unlock()

		LOCK_INGRESS_CAP[i].Lock()
		wastedCap := INGRESS_CAP[i].cap - (float64(receivedPktsPerWIndow)*PKT_LEN)
		LOCK_INGRESS_CAP[i].Unlock()
		// fmt.Printf("%f",wastedCap)
		

		_DEBUG.Printf("Function: wastedResources, wasted resources at ingress %d = %v Mbps",i, wastedCap)
		_INFO.Printf("Wasted resources at ingress at ingress %d = %v Mbps",i, wastedCap)

		// # 

		// # print wastedCap
	}
}


func collectStats() {

	// mitigate()
	_INFO.Printf("STATS FOR WINDOW %d - START", WINDOW_COUNTER)

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
		
		LOCK_CURR_TRAFFIC_STATS[i].Lock()
		PREV_TRAFFIC_STATS[i]["total"] = CURR_TRAFFIC_STATS[i]["total"]
		_INFO.Printf("Total Traffic at Ingress %d = %d", i,CURR_TRAFFIC_STATS[i]["total"])
		CURR_TRAFFIC_STATS[i]["total"] = 0
		
		PREV_TRAFFIC_STATS[i]["udp_flood"] = CURR_TRAFFIC_STATS[i]["udp_flood"]
		_INFO.Printf("Total UDP Flood at Ingress %d = %d", i,CURR_TRAFFIC_STATS[i]["udp_flood"])
		CURR_TRAFFIC_STATS[i]["udp_flood"] = 0

		PREV_TRAFFIC_STATS[i]["tcp_syn"] = CURR_TRAFFIC_STATS[i]["tcp_syn"]
		_INFO.Printf("Total TCP Syn at Ingress %d = %d", i,CURR_TRAFFIC_STATS[i]["tcp_syn"])
		CURR_TRAFFIC_STATS[i]["tcp_syn"] = 0
		LOCK_CURR_TRAFFIC_STATS[i].Unlock()

	}
	WINDOW_COUNTER += 1
	countDroppedPackets()
	wastedResources()
	
	_INFO.Printf("STATS FOR WINDOW %d - END \n\n", WINDOW_COUNTER)
}


