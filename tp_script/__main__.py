from customTypes import Car, Distances, Times, Visits
from algorithms import firstAlgo, secondAlgo
from libs import printMatrix
import sys
import csv
import os


RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + "/results/"

def tests(distances, times, visits):
	print("################## TESTS ##################")

	print(distances.distToDeposit(1)) # 2.195
	print(distances.distToDeposit(0)) # 0
	print(distances.distToDeposit(4)) # 4.107
	print()
	print(distances.getDistanceBetween(1, 2)) # 1.646
	print(distances.getDistanceBetween(2, 1)) # 1.646
	print(distances.getDistanceBetween(0, 4)) # 4.107
	print('\n -- \n')
	print(times.timeToDeposit(1)) # 197
	print(times.timeToDeposit(0)) # 0
	print(times.timeToDeposit(4)) # 369
	print()
	print(times.getTimeBetween(1, 2)) # 148
	print(times.getTimeBetween(2, 1)) # 148
	print(times.getTimeBetween(0, 4)) # 369

	print("################ END TESTS #################")


def writeToCsv(data, file):
	with open(file, 'w', newline='\n') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		for row in data:
			spamwriter.writerow(row)

def main(dataFolder):
	car = Car.getCar(dataFolder+"/vehicle.ini")
	distances = Distances(dataFolder+"/distances.txt")
	times = Times(dataFolder+"/times.txt")
	visits = Visits(dataFolder+"/visits.csv")

	#tests(distances, times, visits)

	result = firstAlgo(visits, distances, times, car)
	#result = secondAlgo(visits, distances, times, car)

	print(printMatrix(result))

	writeToCsv(result, RESULTS_DIR + 'result1.csv')

	print("Le fichier de resultat s'appel result1.csv")


if __name__ == "__main__":
    if(len(sys.argv) != 2):
    	print("Uage :")
    	print("$ python3 tp_script <dataFolder>")
    	print("exemple :")
    	print("$ python3 tp_script ./Data/lyon_40_1_1/")
    else: 
    	dataFolder = sys.argv[1]
    	main(dataFolder)
