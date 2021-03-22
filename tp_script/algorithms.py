def firstAlgo(visits):
	visits.sortByDemand()

	m_visit = visits.getMatrix()

	vehicleTour = [] # the journey of one vehicle, contain id of all visits
	for v in m_visit:
		visitId = v.id
		
	print(vehicleTour)
	
	return [
		[0, 2, 10, 4],
		[0, 3, 5, 1]
	]
