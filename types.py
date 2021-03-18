loadingTime = 10		# time to charge all items in a car (in minutes)
deliveryUnitTime = 10/6 # time to decharge one item (minutes)
deliveryTime = 5		# time to decharge items (minutes)

class Distances:
	def __init__(self, distancesFile):
		self.distances = distancesFile

class Times:
	def __init__(self, rawTimes):
		self.times = rawTimes

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

class Visits:
	def __init__(self, id, name, demand):
		self.id = id
		self.name = name
		self.demand = demand

