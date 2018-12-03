package main

import "time"



type packet struct {
	packet_len float64
	protocol string
	ingress int
	attack_flag bool
	dest string
	detection string

}

func NewPacket(l float64, protocol string, ingress int, af bool) packet {
	var p packet
	p.packet_len = l
	p.protocol = protocol
	p.ingress = ingress
	p.attack_flag = af
	p.dest = "dummy"
	p.detection = "benign"
	return p
}
func flowGenBenign(model string) {
	// # _DEBUG.Printf("Function: flowGen")
	if(model == "simple") {
		flowGenSimple()
	}
}

func sendPkts(n int) {
	for i := 0 ; i < n ; i++ {
		// sendtoNetwork(NewPacket(PKT_LEN,"udp",0,0))
		enqueuePacket(NewPacket(PKT_LEN,"udp",0,false))
	}
}

func flowGenSimple() {
	fixedRate := 1.0 // Mbps
	numPkts := int(fixedRate / PKT_LEN)
	_DEBUG.Printf("Function: flowGenSimple - Number of packets to send in 1 second %d with packet length %f and send rate %f",numPkts, PKT_LEN, fixedRate)
	for {
		sendPkts(numPkts)
		time.Sleep(1 * time.Second)
		// # network.sendtoNetwork(pkt)
	}
}


