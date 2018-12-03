// package main






// func initializeISP() {

// 	// globals._DEBUG.Printf("Function: initializeISP- Initializing TRAFFIC_STATS variables")

// 	for i = 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
// 		CURR_TRAFFIC_STATS = append(CURR_TRAFFIC_STATS)
// 		globals.CURR_TRAFFIC_STATS[i]["total"] = 0
// 		globals.CURR_TRAFFIC_STATS[i]["udp_flood"] = 0
// 		globals.CURR_TRAFFIC_STATS[i]["tcp_syn"] = 0

// 		globals.PREV_TRAFFIC_STATS.append({})
// 		globals.PREV_TRAFFIC_STATS[i]["total"] = 0
// 		globals.PREV_TRAFFIC_STATS[i]["udp_flood"] = 0
// 		globals.PREV_TRAFFIC_STATS[i]["tcp_syn"] = 0

// 		globals.PEAK_TRAFFIC.append(0)
// 		globals.MIN_TRAFFIC.append(float('inf'))
// 		globals.RECEIVE_COUNTER.append(0)
// 		globals.legitimateDropCounter.append(0)
// 		globals.processCounter.append(0)


// 		globals.BUFFER.append(queue.Queue())
// 	}

// }