from neighborhoods import nextInFirstNeighborhood, nextInSecondNeighborhood, nextInThirdNeighborhood
from libs import rateSolution, isRealisable


def pickBestNextSolution(solution, context):
	sol1 = nextInFirstNeighborhood(solution)
	sol2 = nextInSecondNeighborhood(solution)
	sol3 = nextInThirdNeighborhood(solution)

	rate1 = rateSolution(sol1, context)
	rate2 = rateSolution(sol2, context)
	rate3 = rateSolution(sol3, context)

	if rate1 > rate2 and rate1 > rate3:
		return sol1

	if rate2 > rate1 and rate2 > rate3:
		return sol1

	return sol1


# Stop apres une etape seulement
def metaHeuristic1(solution, context):
	return pickBestNextSolution(solution, context)


def pickBestNextRealisableSolution(solution, context):
	sol1 = nextInFirstNeighborhood(solution)
	sol2 = nextInSecondNeighborhood(solution)
	sol3 = nextInThirdNeighborhood(solution)

	while not isRealisable(sol1, context):
		sol1 = nextInFirstNeighborhood(solution)

	while not isRealisable(sol2, context):
		sol2 = nextInSecondNeighborhood(solution)

	while not isRealisable(sol3, context):
		sol3 = nextInThirdNeighborhood(solution)

	rate1 = rateSolution(sol1, context)
	rate2 = rateSolution(sol2, context)
	rate3 = rateSolution(sol3, context)

	if rate1 > rate2 and rate1 > rate3:
		return sol1

	if rate2 > rate1 and rate2 > rate3:
		return sol1

	return sol1


# Stop a la premiere solution realisable (premiere solution realisable)
def metaHeuristic2(solution, context):
	return pickBestNextRealisableSolution(solution, context)



######################################### descentes #########################################


def stop(newSolution, oldSolution, context):
	return rateSolution(newSolution, context) >= rateSolution(oldSolution, context)


def metaHeuristic3(solution, context):
	oldSolution = solution
	newSolution = pickBestNextRealisableSolution(oldSolution, context)

	while not stop(newSolution, oldSolution, context):
		oldSolution = newSolution
		newSolution = pickBestNextRealisableSolution(newSolution, context)

	return newSolution
