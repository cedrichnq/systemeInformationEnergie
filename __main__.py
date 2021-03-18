import customTypes as types
import algorithms
import sys
import csv

def writeToCsv(data, file):
	with open(file, 'w', newline='\n') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')
		for row in data:
			spamwriter.writerow(row)

def main(args):
	dataFolder = args[1]

	car = types.Car.getCar(dataFolder+"vehicle.ini")
	distances = types.Distances(dataFolder+"distances.txt")
	times = types.Times(dataFolder+"times.txt")
	visits = types.Visits(dataFolder+"visits.csv")	

	result = algorithms.firstAlgo()
	writeToCsv(result, 'result1.csv')


if __name__ == "__main__":
    # execute only if run as a script
    if(len(sys.argv) != 2):
    	print("Uage :")
    	print("$ python3 __main__.py <dataFolder>")
    	print("exemple :")
    	print("$ python3 __main__.py ./Data/lyon_40_1_1/")
    else: 
    	main(sys.argv)
