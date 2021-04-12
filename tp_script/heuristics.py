from libs import timeToDelivery
import datetime
import random

def popList(arr, idsToPop):
	newArr = []
	
	for i, e in enumerate(arr):
		if(i not in idsToPop):
			newArr.append(e)
	return newArr

def heuristic(visits, distances, times, car, deterministic = True):
	tours = []
	
	# visits.sortByDemand()
	
	m_visit = visits.getMatrix()

	vehicleTour = [0] # the journey of one vehicle, contain id of all visits (start to 0)
	vehiclePosition = 0 # id of where the vehicule is
	visitsToPop = []
	distToDeposit = 0

	while(len(m_visit)):
		i = 0
		if(not deterministic):
			i = random.randint(0, len(m_visit) - 1)
		v = m_visit[i]

		remainingTime = car.end_time - car.start_time

		distToNext = distances.between(vehiclePosition, v.id)
		distToDeposit = distances.toDeposit(v.id)
		distToNextToDeposit = distToNext + distToDeposit
		timeToNext = times.between(vehiclePosition, v.id)
		timeToNextAndDelevery = timeToNext + timeToDelivery(v.demand)
		timeToDeposit = times.toDeposit(v.id)
		timeToNextToDeposit = timeToNextAndDelevery + timeToDeposit

		demandOfNextDeposit = v.demand

		def canGoToNextPoint(): 
			return distToNextToDeposit <= car.charge and timeToNextToDeposit <= remainingTime and car.filling >= demandOfNextDeposit 
		
		if(canGoToNextPoint()):
			# Go to the next delivery point
			vehiclePosition = v.id
			vehicleTour.append(v.id)
			car.move(distToNext)
			visitsToPop.append(i)

			remainingTime -= timeToNext

		if(not canGoToNextPoint() or len(m_visit) == 1):
			# Comme back to depository
			vehicleTour.append(0)
			vehiclePosition = 0
			car.refill()
			car.recharge()
			if (timeToNextToDeposit <= remainingTime):
				tours.append(vehicleTour)
				vehicleTour = [0]
			

		m_visit = popList(m_visit, visitsToPop)
		visitsToPop = []

	return tours
