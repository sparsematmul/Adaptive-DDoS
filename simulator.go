package main

import (
	"os"
	// "github.com/golang-collections/go-datastructures/fifo"
	// "fmt"
	"encoding/json"
	"log"
	"runtime"
	"time"
)

var (
	CONFIGURATION      Config
	CURR_TRAFFIC_STATS []map[string]int
	backlog [256]string
	// PREV_TRAFFIC_STATS []map[string]int
	PEAK_TRAFFIC []float64
	MIN_TRAFFIC  []float64
	AVG_TRAFFIC  []float64
	// RECEIVE_COUNTER []int
	legitimateDropCounter []int
	// processCounter []int
	// BUFFER []*fifo.Queue
	NUM_VMs                 []int
	INGRESS_CAP             []*VM
	PKT_LEN                 float64 = 100.0 * 8 / 1000000
	UDP_DETECT_ACCURACY     float64 = 0.9
	TCP_SYN_DETECT_ACCURACY float64 = 0.9
	DNS_AMP_DETECT_ACCURACY float64 = 0.9
	EPOCH_TIME                      = 5.0
	WINDOW_COUNTER          int
    BACKLOG int = 0
)

func main() {

	runtime.GOMAXPROCS(4)
	if len(os.Args) < 2 {
		log.Fatal("PLEASE ENTER FILENAME FOR CONFIG")
	}
	var configurationFile string = os.Args[1]
	_DEBUG.Println("Hello from main")

	_DEBUG.Println("Reading configuration file")

	CONFIGURATION = LoadConfiguration(configurationFile)
	s, _ := json.MarshalIndent(CONFIGURATION, "", "\t")
	_DEBUG.Printf("%s", s)

	_DEBUG.Printf("Initialize traffic stats data structures in ISP")
	// initialize traffic stats data structures
	initializeISP()

	_DEBUG.Printf("Initialize capacity of ingress locations depending on the defense type")
	initializeDefense()

	initializeLocks()

	// start legitimate traffic thread
	_DEBUG.Printf("Start legitimate traffic thread")
	for j := 0; j < CONFIGURATION.INGRESS_LOC; j++ {
		go flowGenBenign("simple", j)
	}
	// start attack traffic thread
	_DEBUG.Printf("Start attack traffic thread")
	go attack()

	// start dequeuing pkts after delay equivalent to processing delay
	_DEBUG.Printf("Start packet processing thread - processing delay = %f s", CONFIGURATION.PROCESSING_DELAY)
	_DEBUG.Printf("Start stats collection thread - epoch = %f s", EPOCH_TIME)
	// stopProcess = Event()
	// processingThread = RepeatingThread(stopProcess,PROCESSING_DELAY,"packet processingThread",buffer.processPacket)
	// processingThread.start()
	statsTicker := time.NewTicker(time.Duration(EPOCH_TIME) * time.Second)
	processTicker := time.NewTicker(time.Duration(CONFIGURATION.PROCESSING_DELAY) * time.Millisecond)
	// go processing()
	// go flowGenBenign("simple", 0)
	for {
		select {
		case <-processTicker.C:
			go processPacket()
		case <-statsTicker.C:
			go collectStats()
		}
	}

}
