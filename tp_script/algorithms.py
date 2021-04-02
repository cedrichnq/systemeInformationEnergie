import datetime
import random

def popList(arr, idsToPop):
	newArr = []
	
	for i, e in enumerate(arr):
		if(i not in idsToPop):
			newArr.append(e)
	return newArr

# TODO prendre en compte le nombre de trucs transportées par la voiture
# TODO prendre en compte le temsp de chargement & (rechargement)

def firstAlgo(visits, distances, times, car):
	tours = []
	# visits.sortByDemand() # pour tester
	m_visit = visits.getMatrix()

	vehicleTour = [0] # the journey of one vehicle, contain id of all visits (start to 0)
	vehiclePosition = 0 # id of where the vehicule is
	visitsToPop = []
	distToDeposit = 0



	while(len(m_visit)):
		#i = random.randint(0, len(m_visit) - 1)
		i = 0
		v = m_visit[i]

		remainingTime = car.end_time - car.start_time

		distToNext = distances.getDistanceBetween(vehiclePosition, v.id)
		distToDeposit = distances.distToDeposit(v.id)
		distToNextToDeposit = distToNext + distToDeposit

		timeToNext = times.getTimeBetween(vehiclePosition, v.id)
		timeToDeposit = times.timeToDeposit(v.id)
		timeToNextToDeposit = timeToNext + timeToDeposit

		demandOfNextDeposit = v.demand

		print("--")
		print(demandOfNextDeposit)
		print(v.demand)
		
		if(distToNextToDeposit <= car.charge and timeToNextToDeposit <= remainingTime and car.filling >= demandOfNextDeposit):
			print(v.id)
			print(len(visitsToPop))
			vehiclePosition = v.id
			vehicleTour.append(v.id)
			car.move(distToNext)
			visitsToPop.append(i)

			remainingTime -= timeToNext

		else:
			vehicleTour.append(0)
			vehiclePosition = 0
			car.refill()
			car.recharge()
			if (timeToNextToDeposit <= remainingTime):
				tours.append(vehicleTour)
				vehicleTour = [0]
			
				

		m_visit = popList(m_visit, visitsToPop)
		visitsToPop = []

	print(tours)
	return tours

def secondAlgo(visits, distances, times, car):
	tours = []
	# visits.sortByDemand() # pour tester
	m_visit = visits.getMatrix()

	while(len(m_visit) > 0):
		vehicleTour = [0]
		vehiclePosition = 0
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

		vehicleTour.append(0)
		car.refill()
		tours.append(vehicleTour)

		m_visit = popList(m_visit, visitsToPop)

	print(tours)
	return tours
