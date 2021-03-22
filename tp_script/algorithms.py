def firstAlgo(visits, distances):
	visits.sortByDemand()

	m_visit = visits.getMatrix()

	vehicleTour = [] # the journey of one vehicle, contain id of all visits
	vehiclePosition = 0
	for v in m_visit:
		distanceToNext = distances.getDistanceBetween(vehiclePosition, v.id)
		print(distanceToNext)

	print(vehicleTour)
	
	return [
		[0, 2, 10, 4],
		[0, 3, 5, 1]
	]
