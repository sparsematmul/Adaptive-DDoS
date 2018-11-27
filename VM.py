import globals 
import queue

class VM ():
	def __init__(cap,vm_queue, vm_ports):
		self.cap = globals.VM_COMPUTE_CAP
		self.vm_queuue = globals.BUFFSIZE
		self.vm_ports = globals.VMPORTS

