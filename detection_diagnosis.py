



# let's fix 90% accuracy for each attack for now


def detect_UDP_Flood(udp_pkt):
	prob = random.random(0.0,1)
	if(prob > 0.9):
		# attack packet received
		return True

	return False




def detect_TCP_SYN_Flood(tcp_pkt):
	prob = random.random(0.0,1)
	if(prob > 0.9):
		# attack packet received
		return True

	return False



def detect_NTP(udp_pkt):
	prob = random.random(0.0,1)
	if(prob > 0.9):
		# attack packet received
		return True

	return False



def detect_DNS_amp(udp_pkt):
	prob = random.random(0.0,1)
	if(prob > 0.9):
		# attack packet received
		return True

	return False



def diagnose_UDP_Flood(udp_pkt):

	UDP_Flood_traffic = 0

	if(detect_UDP_Flood(udp_pkt)):
		UDP_Flood_traffic += udp_pkt.size

	return UDP_Flood_traffic


def diagnose_TCP_SYN_Flood(tcp_pkt):

	TCP_SYN_Flood_traffic = 0

	if(detect_TCP_SYN_Flood(udp_pkt)):
		TCP_SYN_Flood_traffic += tcp_pkt.size

	return TCP_SYN_Flood_traffic






def diagnose_tarffic(pkt):

	if(isUDP(pkt)):
		attack_traffic_udp = diagnose_UDP_Flood(pkt)
		attack_traffic_dns = diagnose_DNS_amp(pkt)
		attack_traffic_ntp = diagnose_NTP(pkt)

	if(isTCP(pkt)):
		attack_traffic_tcp = diagnose_TCP_SYN_Flood(pkt)





