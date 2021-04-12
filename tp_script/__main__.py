from customTypes import Car, Distances, Times, Visits
from heuristics import heuristic
from libs import printMatrix
import sys
import csv
import os


RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + "/results/"


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

	result = heuristic(visits, distances, times, car)

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
