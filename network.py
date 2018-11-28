# Maybe add the propogation delay later 

import globals


from defense import *
from queue import *

def sendtoNetwork(pkt):
	# pause till transmission delay
	receiveonNetwork(pkt)


def receiveonNetwork(pkt):
	deliverPacket(pkt)
	#detection part
	#call receive pkt


def deliverPacket(pkt):
	
	enqueuePacket(pkt)


