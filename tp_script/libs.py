import copy

from const import TIME_TO_DELIVERY_ONE_ITEM, TIME_TO_DELIVERY
import customTypes as types


def printMatrix(matrix):
	string = ''
	for row in matrix:
		string += str(row) + '\n'
	return string


def parseMatrixFile(file):
	matrix = []
	with open(file, 'r') as fp:
		line = fp.readline()
		while line:
			line = line[:-1] # remove end of line car
			rowData = line.split()
			rowData = [float(numeric_string) for numeric_string in rowData] # convert to floats
			matrix.append(rowData)
			line = fp.readline()
	return matrix


def csvToVisits(file):
	matrix =[]
	with open(file, 'r') as fp:
		line = fp.readline()
		line = fp.readline() # remove header
		while line:
			line = line[:-1] # remove end of line car
			row = line.split(',')
			matrix.append(types.Visit(row))
			line = fp.readline()
	
	return matrix[1:] # remove first line : deposit


def timeToDelivery(nb_tiems):
	return TIME_TO_DELIVERY_ONE_ITEM * nb_tiems + TIME_TO_DELIVERY


##############################################################################


def removeEmptyTours(solution):
	newSolution = []
	for tour in solution:
		if tour:
			newSolution.append(copy.deepcopy(tour))
	return newSolution


##############################################################################


def rateSolution(solution, context):
	(distances, times, car) = context

	tmp_transit = 0
	tour_tmp_transit = 0
	nb_cars = 0

	for tour in solution:
		nb_cars += 1
		for index, visit in enumerate(tour):
			if index + 1 < len(tour):
				nextVisit = tour[index + 1]
				visit_tmp_transit = times.between(visit, nextVisit)
				tour_tmp_transit += visit_tmp_transit

		tmp_transit += tour_tmp_transit
		tour_tmp_transit = 0

	nb_cars_bonus = 500*nb_cars
	tmp_transit_bonus = -tmp_transit/60
	return nb_cars_bonus + tmp_transit_bonus


# # Just verify start and stop with deposit
# def isRealisable(solution, context):
# 	startAndStopAtDeposit = True
#
# 	for tour in solution:
# 		startAndStopAtDeposit = tour[0] == 0 and tour[len(tour) - 1] == 0 and startAndStopAtDeposit
#
# 	return startAndStopAtDeposit


# # Verify (start and stop with deposit) and distances
# def isRealisable(solution, context):
# 	(distances, times, car) = context
#
# 	startAndStopAtDeposit = True
# 	distanceIsCorrect = True
# 	distance = 0
#
# 	for tour in solution:
# 		startAndStopAtDeposit = tour[0] == 0 and tour[len(tour) - 1] == 0 and startAndStopAtDeposit
# 		for index, visit in enumerate(tour):
# 			nextVisit = tour[index + 1]
# 			distanceIsCorrect = distance <= car.max_dist and distanceIsCorrect
# 			if visit == 0:
# 				distance = 0
# 			else:
# 				distance += distances.between(visit, nextVisit)
#
# 	return startAndStopAtDeposit and distanceIsCorrect


# Verify (start and stop with deposit) and distances and time
def isRealisable(solution, context):
	(distances, times, car) = context

	startAndStopAtDeposit = True
	distanceIsCorrect = True
	distance = 0
	timeIsCorrect = True
	time = 0

	for tour in solution:
		startAndStopAtDeposit = tour[0] == 0 and tour[len(tour) - 1] == 0 and startAndStopAtDeposit
		for index, visit in enumerate(tour):
			if index + 1 < len(tour):
				nextVisit = tour[index + 1]

				if index < len(tour):
					time += times.between(visit, nextVisit)

				distanceIsCorrect = distance <= car.max_dist and distanceIsCorrect
				if visit == 0:
					distance = 0
				else:
					distance += distances.between(visit, nextVisit)

		timeIsCorrect = time <= car.end_time - car.start_time

	return startAndStopAtDeposit and distanceIsCorrect and timeIsCorrect
