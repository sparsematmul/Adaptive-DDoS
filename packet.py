# Packet definition
import constants

class Packet(object):
# Packet class contains the following:
#	1.length of the packet 

	def __init__(self, packet_len,protocol,ingress_loc, attack_flag):
		self.packet_len = packet_len
		self.protocol = protocol
		self.dst = ingress_loc
		self.attack_flag = attack_flag
		
