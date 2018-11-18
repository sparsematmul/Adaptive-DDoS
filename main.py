
import threading

import sys
from legitimate_traffic import *
from attack_traffic import *

def main():
	attackerType = sys.argv[1]
	if(len(sys.argv) == 3):
		numPkts = int(sys.argv[2])
		threading.Thread(target=flowGen, args=[numPkts]).start()
	elif(len(sys.argv) == 4):
		mode = sys.argv[3]
		threading.Thread(target=flowGen, args=[numPkts,mode]).start()
	else:
		threading.Thread(target=flowGen).start()

	
	threading.Thread(target=attackTrafficGen, args=[attackerType]).start()




if __name__ == "__main__":
    main()


