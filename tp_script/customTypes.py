import const as C
import libs 

class Distances:
	def __init__(self, distancesFile):
		self.distances = libs.parseMatrixFile(distancesFile)

	def getMatrix(self): 
		return self.distances

	def __str__(self):
		return libs.printMatrix(self.distances)


class Times:
	def __init__(self, timesFile):
		self.times = libs.parseMatrixFile(timesFile)

	def getMatrix(self): 
		return self.times

	def __str__(self):
		return libs.printMatrix(self.times)


class Car:
    "A car wich run and delivery things until she need to be refilled. That's a car life."

    def getCar(initFile):
    	with open(initFile, 'r') as fp:
    		line = fp.readline()
    		while line:
    			line = line[:-1] # remove end of line car
    			if(line.startswith('max_dist')):
    				max_dist = line.partition('= ')[2]
    			if(line.startswith('capacity')):
    				capacity = line.partition('= ')[2]
    			if(line.startswith('charge_fast')):
    				charge_fast = line.partition('= ')[2]
    			if(line.startswith('charge_medium')):
    				charge_medium = line.partition('= ')[2]
    			if(line.startswith('charge_slow')):
    				charge_slow = line.partition('= ')[2]
    			if(line.startswith('start_time')):
    				start_time = line.partition('= ')[2]
    			if(line.startswith('end_time')):
    				end_time = line.partition('= ')[2]
    			line = fp.readline()

    	return Car(capacity, max_dist, charge_fast, charge_medium, charge_slow)

    def __init__(self, capacity, maxDist, charge_fast, charge_medium, charge_slow):
        self.capacity = capacity	# the number of objects that can be carry by the car
        self.filling = 0			# number of items carried 
        self.max_dist = maxDist 	# maximum distance the car can drive
        self.charge = maxDist		# the number of kilometers that the car can still drive
        self.charge_fast = charge_fast
        self.charge_medium = charge_medium
        self.charge_slow = charge_slow

    def getCharge(self):
    	return self.charge


class Visit: 
	def __init__(self, rawVisit):
		self.id = rawVisit[C.ID]
		self.name = rawVisit[C.NAME]
		self.demand = rawVisit[C.DEMAND]

	def __str__(self):
		return '[id: ' + self.id + ', name: ' + self.name + ', demand: ' + self.demand + ']'


class Visits:
	def __init__(self, visitsFile):
		self.visits = libs.csvToVisits(visitsFile)

	def getMatrix(self):
		return self.visits

	def __str__(self):
		return libs.printMatrix(self.visits)

	def sortByDemand(self):
		return self.visits.sort(key = lambda x: int(x.demand), reverse=True)