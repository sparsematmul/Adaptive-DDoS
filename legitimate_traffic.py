


# this file will be used to have a notion of legitimate traffic
# how much legtimate traffic is received at any given time
# what is the latency observed and all those things will be modeled here
import packet
import globals

import network


def flowGen():
	if(globals.LEG_TRAFFIC_MODEL == "simple"):
		flowGenSimple()


def flowGenSimple():

	for i in range(1,100000):
		pkt = packet.Packet(20,"udp",2,0)
		sendtoNetwork(pkt)





# def randFlowGen():
  
