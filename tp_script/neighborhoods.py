from random import randint
import copy

from libs import removeEmptyTours

testRealisableSolution = [[0, 1, 2, 3, 4, 5, 0], [0, 6, 7, 0], [0, 8, 9, 10, 11, 0], [0, 12, 13, 14, 15, 16, 17, 0], [0, 18, 19, 20, 0], [0, 21, 22, 23, 0], [0, 24, 25, 26, 0], [0, 27, 0], [0, 28, 29, 30, 0], [0, 31, 32, 33, 34, 35, 36, 0], [0, 37, 38, 39, 40, 0]]


# Get random visit of random tour and push it in after a random visit in another random tour
def nextInFirstNeighborhood(solution):
    newSolution = copy.deepcopy(solution)

    popTourIndex = randint(0, len(newSolution) - 1)
    popTour = newSolution[popTourIndex]

    popVisitIndex = randint(0, len(popTour) - 1)
    popVisit = popTour.pop(popVisitIndex)

    insertTourIndex = randint(0, len(newSolution) - 1)
    insertTour = newSolution[insertTourIndex]
    insertVisitIndex = randint(0, len(insertTour) - 1)

    newSolution[insertTourIndex].insert(insertVisitIndex, popVisit)

    return removeEmptyTours(newSolution)


def nextInSecondNeighborhood(solution):
    return testRealisableSolution


def nextInThirdNeighborhood(solution):
    return testRealisableSolution

