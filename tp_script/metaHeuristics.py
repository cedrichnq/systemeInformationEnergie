from neighborhoods import nextInFirstNeighborhood,nextInSecondNeighborhood, nextInThirdNeighborhood
from libs import rateSolution, isRealisable


def pickBestNextSolution(solution, times):
	sol1 = nextInFirstNeighborhood(solution)
	sol2 = nextInSecondNeighborhood(solution)
	sol3 = nextInThirdNeighborhood(solution)

	rate1 = rateSolution(sol1, times)
	rate2 = rateSolution(sol2, times)
	rate3 = rateSolution(sol3, times)

	if(rate1 > rate2 and rate1 > rate3):
		return sol1

	if (rate2 > rate1 and rate2 > rate3):
		return sol1

	return sol1


# Stop apres une etape seulement
def metaHeuristic1(solution, times):
	return pickBestNextSolution(solution, times)


def pickBestNextRealisableSolution(solution, times):
	sol1 = nextInFirstNeighborhood(solution)
	sol2 = nextInSecondNeighborhood(solution)
	sol3 = nextInThirdNeighborhood(solution)

	while not isRealisable(sol1):
		sol1 = nextInFirstNeighborhood(solution)

	while not isRealisable(sol2):
		sol2 = nextInSecondNeighborhood(solution)

	while not isRealisable(sol3):
		sol3 = nextInThirdNeighborhood(solution)

	rate1 = rateSolution(sol1, times)
	rate2 = rateSolution(sol2, times)
	rate3 = rateSolution(sol3, times)

	if (rate1 > rate2 and rate1 > rate3):
		return sol1

	if (rate2 > rate1 and rate2 > rate3):
		return sol1

	return sol1


# Stop a la premiere solution realisable
def metaHeuristic2(solution, times):
	return pickBestNextRealisableSolution(solution, times)


# def stop(newSolution, oldSolution, times):
# 	return rateSolution(newSolution, times) >= rateSolution(oldSolution, times)
#

# Stop a la premiere solution meileur que celle d'avant
# def metaHeuristic2(solution, times):
# 	newSolution = solution
# 	oldSolution = []
#
# 	while not stop(newSolution, oldSolution, times):
# 		oldSolution = newSolution
# 		newSolution = pickBestNextSolution(newSolution)
#
# 	return newSolution
