class ChargingStationCategory():
    fast = 'fast'
    medium = 'medium'
    slow = 'slow'

class Car:
    "A car wich run and delivery things until she need to be refilled. That's a car life."

    def __init__(self, capacity=10, maxDist=100):
        self.capacity = capacity	# the number of objects that can be carry by the car
        self.max_dist = maxDist 	# maximum distance the car can drive
        self.charge = maxDist		# the number of kilometers that the car can still drive 

    def getCharge(self):
    	return self.charge


class ChargingStation: 
	def __init__(self, category=ChargingStationCategory.medium):
		self.category = category

	def getCategory(self):
		return self.category
