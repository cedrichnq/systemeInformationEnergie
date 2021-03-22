import datetime

def popList(arr, idsToPop):
	newArr = []
	
	for i, e in enumerate(arr):
		if(i not in idsToPop):
			newArr.append(e)
	return newArr

def firstAlgo(visits, distances, times, car):
	tours = []
	# visits.sortByDemand() # pour tester
	m_visit = visits.getMatrix()

	while(len(m_visit) > 0):
		vehicleTour = [0] # the journey of one vehicle, contain id of all visits (start to 0)
		vehiclePosition = 0 # id of where the vehicule is
		visitsToPop = []
		distToDeposit = 0

		remainingTime = car.end_time - car.start_time

		for i, v in enumerate(m_visit):
			distToNext = distances.getDistanceBetween(vehiclePosition, v.id)
			distToDeposit = distances.distToDeposit(v.id)
			distToNextToDeposit = distToNext + distToDeposit

			timeToNext = times.getTimeBetween(vehiclePosition, v.id)
			timeToDeposit = times.timeToDeposit(v.id)
			timeToNextToDeposit = timeToNext + timeToDeposit

			if(distToNextToDeposit <= car.charge and timeToNextToDeposit <= remainingTime):
				vehiclePosition = v.id
				vehicleTour.append(v.id)
				car.move(distToNext)
				visitsToPop.append(i)

				remainingTime -= timeToNext

		#vehiclePosition = 0 # useless
		vehicleTour.append(0)
		#car.move(distToNext) # useless
		car.refill()
		tours.append(vehicleTour)

		m_visit = popList(m_visit, visitsToPop)

	print(tours)
	return tours
