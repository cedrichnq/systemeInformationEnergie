def firstAlgo(visits):
	visits.sortByDemand()

	visits_m = visits.getMatrix()

	vehicleTour = [] # the journey of one vehicle, contain id of all visits
	for v in visits_m:
		print(v)
	
	return [
		[0, 2, 10, 4],
		[0, 3, 5, 1]
	]
