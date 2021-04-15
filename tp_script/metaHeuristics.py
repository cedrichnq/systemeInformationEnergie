def ratedSolution(solution):
	return 10

def stop(newSolution, oldSolution):
	return ratedSolution(newSolution) >= ratedSolution(oldSolution)

def pickNextSolution(solution):
	return solution

# On prend une livraison au hasard d'une tournée au hasard et on l'insère au hasard dans une autre solution au hasard.
# Stop a la premiere solution meileur que celle d'avant
def metaHeuristic1(solution):
	newSolution = solution
	oldSolution = solution

	while not stop(newSolution, oldSolution):
		oldSolution = newSolution
		newSolution = pickNextSolution(newSolution)

	return newSolution
