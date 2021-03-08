class Car:
    "A car wich run and delivery things until she need to be refilled. That's a car life."

    def __init__(self, capacity=10):
        self.capacity = capacity	# the number of objects that can be carry by the car
        self.charge = 100			# the number of kilometers that the car can still drive 

    def getCharge(self): 
    	return self.charge
