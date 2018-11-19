


# this file will be used to have a notion of legitimate traffic
# how much legtimate traffic is received at any given time
# what is the latency observed and all those things will be modeled here
import packet
import constants

from network import *


def flowGen(numPkts, mode):
	if(mode == "simple"):
		flowGenSimple(numPkts)


def flowGenSimple(pkt_no):

	for i in range(1,pkt_no):
		pkt = packet.Packet(20,"udp",2,0)
		sendtoNetwork(pkt)





# def randFlowGen():
  
