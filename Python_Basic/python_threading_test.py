# *-* coding:gb2312 *-*
import threading
import time

stationName=("stop 0","Stop 1","Stop 2","Stop 3","Stop 4","Stop 5","Stop 6")
currentStationIndex = -1
eventBusStop = threading.Event()
eventClosedDoor = threading.Event()
eventOpenedDoor = threading.Event()
stationCount = len(stationName)

class Passenger(threading.Thread):
    def __init__(self,no,getonStation,getoffStation):
        self.no =no
        self.getonStation=getonStation
        self.getoffStation=getoffStation
        threading.Thread.__init__(self)

    def run(self):
        bExit= False
        global currentStationIndex
        global stationCount
        bAlreadyGetOnStation = False
        while not bExit:
            eventOpenedDoor.wait()
            if self.getonStation == currentStationIndex and bAlreadyGetOnStation == False:
                print "Passenger%d onboard at %s stop" %(self.no,stationName[currentStationIndex])
                bAlreadyGetOnStation =True
            elif self.getoffStation == currentStationIndex:
                print "Passenger %d get off at %s stop" %(self.no,stationName[currentStationIndex])
                bExit = True
            time.sleep(1)



class Driver(threading.Thread):
    def run(self):
        bExit= False
        global currentStationIndex
        global stationCount
        while not bExit:
            print "Driver: Bus is leaving from the station....."
            time.sleep(5)
            currentStationIndex += 1
            print "Driver: arrived at the station: ",stationName[currentStationIndex]
            eventBusStop.set()
            eventClosedDoor.wait()
            eventClosedDoor.clear()
            if currentStationIndex == stationCount-1:
                bExit= True

class Conductor(threading.Thread):
    def run(self):
        bExit= False
        global currentStationIndex
        global stationCount
        while not bExit:
            eventBusStop.wait()
            eventBusStop.clear()
            print "Conductor opened the door: %s arrived" %(stationName[currentStationIndex])
            eventOpenedDoor.set()
            time.sleep(5)
            print "Conductor closed the door"
            eventOpenedDoor.clear()
            eventClosedDoor.set()
            if currentStationIndex == stationCount-1:
                bExit = True


def test():
    passPool=[]

    passPool.append(Passenger(0,0,3))
    passPool.append(Passenger(1,1,3))
    passPool.append(Passenger(2,2,4))
    passPool.append(Passenger(3,0,5))
    passPool.append(Passenger(4,1,3))
    passPool.append(Passenger(5,2,4))
    passPool.append(Passenger(6,4,5))
    passPool.append(Passenger(7,0,2))
    passPool.append(Passenger(8,1,3))

    passPool.append(Conductor())
    passPool.append(Driver())
    leng = len(passPool)
    for i in range(leng):
        passPool[i].start()

if __name__=='__main__':
    test()
