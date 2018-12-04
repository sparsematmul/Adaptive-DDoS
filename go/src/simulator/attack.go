package main

import (
	"time"
	"math/rand"
)



func sendToRandIngress(n int){
	for i := 0 ; i < n ; i++ {
		// sendtoNetwork(NewPacket(PKT_LEN,"udp",0,0))
		dst := rand.Intn(CONFIGURATION.INGRESS_LOC)
		enqueuePacket(NewPacket(PKT_LEN,"udp",dst,false))
	}
}
func randIngress() {
	fixedCap := CONFIGURATION.ATTACKER_CAP //Mbps
	numPkts := int(fixedCap / PKT_LEN)
	_DEBUG.Printf("Function: flowGenSimple - Number of packets to send in 1 second %d with packet length %f and send rate %f",numPkts, PKT_LEN, fixedCap)
	for {
		go sendToRandIngress(numPkts)
		time.Sleep(1 * time.Second)
		// # network.sendtoNetwork(pkt)
	}
}

func sendPktsProtocol(n int, ingress int, protocol string) {
	for i := 0 ; i < n ; i++ {
		// sendtoNetwork(NewPacket(PKT_LEN,"udp",0,0))
		enqueuePacket(NewPacket(PKT_LEN,protocol,ingress,false))
	}
}
func randAttackMix() {
	// _DEBUG.Printf("Function: flowGenSimple - Number of packets to send in 1 second %d with packet length %f and send rate %f",numPkts, PKT_LEN, fixedCap)
	for {
		u := rand.Float64()
		t := rand.Float64()
		d := rand.Float64()
		sum := u+t+d
		u = (u/sum)*CONFIGURATION.ATTACKER_CAP
		t = (t/sum)*CONFIGURATION.ATTACKER_CAP
		d = (d/sum)*CONFIGURATION.ATTACKER_CAP
		u_numPkts := int(u / PKT_LEN)
		t_numPkts := int(t / PKT_LEN)
		d_numPkts := int(d / PKT_LEN)
		ingress :=0
		go sendPktsProtocol(u_numPkts,ingress,"udp")
		go sendPktsProtocol(t_numPkts,ingress,"tcp")
		go sendPktsProtocol(d_numPkts,ingress,"dns")
		time.Sleep(1 * time.Second)
		// # network.sendtoNetwork(pkt)
	}
}
