# Maybe add the propogation delay later 

import constants


from defense import *
from queue import *

def sendtoNetwork(pkt):
	# pause till transmission delay
	receiveonNetwork(pkt)


def receiveonNetwork(pkt):
	ddosMiddlebox(pkt)
	deliverPacket(pkt)
	#detection part
	#call receive pkt


def deliverPacket(pkt):
	enqueuePacket(pkt)


