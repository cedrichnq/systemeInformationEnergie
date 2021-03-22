from customTypes import Car, Distances, Times, Visits
from algorithms import firstAlgo
import sys
import csv
import os


RESULTS_DIR = os.path.dirname(os.path.realpath(__file__)) + "/results/"

def writeToCsv(data, file):
	with open(file, 'w', newline='\n') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		for row in data:
			spamwriter.writerow(row)

def main(args):
	dataFolder = args[1]

	car = Car.getCar(dataFolder+"/vehicle.ini")
	distances = Distances(dataFolder+"/distances.txt")
	times = Times(dataFolder+"/times.txt")
	visits = Visits(dataFolder+"/visits.csv")	
	
	result = firstAlgo(visits)

	writeToCsv(result, RESULTS_DIR + 'result1.csv')


if __name__ == "__main__":
    # execute only if run as a script
    if(len(sys.argv) != 2):
    	print("Uage :")
    	print("$ python3 __main__.py <dataFolder>")
    	print("exemple :")
    	print("$ python3 __main__.py ./Data/lyon_40_1_1/")
    else: 
    	main(sys.argv)
