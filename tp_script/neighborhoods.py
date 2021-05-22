from random import randint
import copy

from libs import removeEmptyTours

testRealisableSolution = [[0, 1, 2, 3, 4, 5, 0], [0, 6, 7, 0], [0, 8, 9, 10, 11, 0], [0, 12, 13, 14, 15, 16, 17, 0], [0, 18, 19, 20, 0], [0, 21, 22, 23, 0], [0, 24, 25, 26, 0], [0, 27, 0], [0, 28, 29, 30, 0], [0, 31, 32, 33, 34, 35, 36, 0], [0, 37, 38, 39, 40, 0]]
testNonRealisableSolution = [[0, 1, 2, 3, 4, 5], [0, 6, 7, 0], [0, 8, 9, 10, 11, 0], [0, 12, 13, 14, 15, 16, 17, 0], [0, 18, 19, 20, 0], [0, 21, 22, 23, 0], [0, 24, 25, 26, 0], [0, 27, 0], [0, 28, 29, 30, 0], [0, 31, 32, 33, 34, 35, 36, 0], [0, 37, 38, 39, 40, 0]]


def getRandomClientVisit(tour):
	popVisitIndex = randint(1, len(tour) - 2)
	while tour[popVisitIndex] == 0:
		popVisitIndex = randint(1, len(tour) - 2)

	return tour.pop(popVisitIndex)

def insertDepositVisits(solution, context):
	(distances, times, car) = context
	totalDist = 0

	for tour in solution:		
		for index, visit in enumerate(tour):
			if(index != len(tour) - 1):
				distToNext = distances.between(visit, tour[index + 1])
				distToDeposit = distances.toDeposit(tour[index + 1])
				totalDist += distToNext
				distToNextToDeposit = totalDist + distToDeposit

				if(distToNextToDeposit > car.max_dist):
					tour.insert(index, 0)

		totalDist = 0


	return solution


# Get random visit of random tour and push it in after a random visit in another random tour
# never remove depository 
def nextInFirstNeighborhood(solution, context):
    newSolution = copy.deepcopy(solution)

    popTourIndex = randint(0, len(newSolution) - 1)
    popTour = newSolution[popTourIndex]

    popVisit = getRandomClientVisit(popTour)

    insertTourIndex = randint(0, len(newSolution) - 1)
    insertTour = newSolution[insertTourIndex]
    insertVisitIndex = randint(1, len(insertTour) - 2)

    newSolution[insertTourIndex].insert(insertVisitIndex, popVisit)

    return insertDepositVisits(removeEmptyTours(newSolution), context)


# Replace a visit by another in the same tour
# never remove depository 
def nextInSecondNeighborhood(solution, context):
    newSolution = copy.deepcopy(solution)

    tourIndex = randint(0, len(newSolution) - 1)
    tour = newSolution[tourIndex]

    popVisit = getRandomClientVisit(tour)

    insertVisitIndex = randint(0, len(tour) - 1)

    newSolution[tourIndex].insert(insertVisitIndex, popVisit)

    return insertDepositVisits(removeEmptyTours(newSolution), context)



def nextInThirdNeighborhood(solution, context):
    return testNonRealisableSolution

