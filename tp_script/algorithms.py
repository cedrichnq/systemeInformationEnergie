def firstAlgo(visits, distances, car):
	visits.sortByDemand()

	m_visit = visits.getMatrix()

	vehicleTour = [] # the journey of one vehicle, contain id of all visits
	vehiclePosition = 0
	for i, v in enumerate(m_visit):
		distanceToNext = distances.getDistanceBetween(vehiclePosition, v.id)
		if(distanceToNext <= car.charge):
			vehicleTour.append(v.id)
			car.move(float(distanceToNext))
			m_visit.pop(i)
		print(distanceToNext)

	print(vehicleTour)
	
	return [
		[1, 2, 3],
		[3, 0, 8],
		[5, 5, 3]
	]
