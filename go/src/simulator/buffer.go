package main




func enqueuePacket(pkt packet) {

  
   LOCK_INGRESS_CAP[pkt.ingress].Lock()
	if ((INGRESS_CAP[pkt.ingress].availableBuffSpace - pkt.packet_len) > 0) {

      LOCK_RECEIVE_COUNTER[pkt.ingress].Lock()
      RECEIVE_COUNTER[pkt.ingress] +=1
      LOCK_RECEIVE_COUNTER[pkt.ingress].Unlock()
      BUFFER[pkt.ingress].Add(pkt)
      
      INGRESS_CAP[pkt.ingress].availableBuffSpace -= pkt.packet_len
      // _DEBUG.Printf("Function: enqueuePacket - Packet Added to Queue, Available Buffer space at %d = %f", pkt.ingress, INGRESS_CAP[pkt.ingress].availableBuffSpace)
      // BUFFER[pkt.ingress] <- pkt   // Send v to channel ch


   	} else {
      dropPacket(pkt)
   	}
   LOCK_INGRESS_CAP[pkt.ingress].Unlock()

}



func dropPacket(pkt packet) {
   	
   	if (pkt.attack_flag == false) {
      
		LOCK_legitimateDropCounter[pkt.ingress].Lock()
		legitimateDropCounter[pkt.ingress]+=1
		_DEBUG.Printf("Function: dropPacket - Legitimate packet dropped, legitimateDropCounter = %d",legitimateDropCounter[pkt.ingress])
		LOCK_legitimateDropCounter[pkt.ingress].Unlock()

 //  	} else {
	// 	attackDropCounter[pkt.ingress] +=1
 //      // # _DEBUG.Printf(f"Function: dropPacket - Attack packet dropped, attackDropCounter = {attackDropCounter[pkt.ingress]}")
	}
}


func processPacket() {

	for i := 0 ; i < CONFIGURATION.INGRESS_LOC ; i++ {
	  // # LOCK_RECEIVE_COUNTER[i].Lock()
	  
		if(RECEIVE_COUNTER[i] > 0) {
		 
			LOCK_INGRESS_CAP[i].Lock()
			pktsToDequeue := INGRESS_CAP[i].numOfDequeuePkts
			if(float64(pktsToDequeue)*PKT_LEN > (INGRESS_CAP[i].cap - INGRESS_CAP[i].availableBuffSpace)) {
				pktsToDequeue = int(INGRESS_CAP[i].cap - INGRESS_CAP[i].availableBuffSpace/PKT_LEN)
			}
			INGRESS_CAP[i].availableBuffSpace += (PKT_LEN*float64(pktsToDequeue))

			// _DEBUG.Printf("Function: processPacket - {pktsToDequeue} packets processed, Available Buffer space at %d = %f", i, INGRESS_CAP[i].availableBuffSpace)
			LOCK_INGRESS_CAP[i].Unlock()

			for j := 0 ; j < pktsToDequeue ; j++ { 
				// pkt := <-BUFFER[i]
				pkt,ok  := (BUFFER[i].Next()).(packet)
				if(ok) {
					enqueuePacket(pkt)
					diagnose(pkt)
				} 
			}
		}

		 // _DEBUG.Printf("Function: processPacket - after diagnose %+v ",CURR_TRAFFIC_STATS[i])

		// # LOCK_RECEIVE_COUNTER[i].Unlock()

    }
}    

