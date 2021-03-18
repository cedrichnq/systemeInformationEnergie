import types
import sys

def main(args):
	dataFolder = args[1]
	car = types.Car.getCar(dataFolder+"vehicle.ini")
	distances = types.Distances(dataFolder+"distances.txt")
	times = types.Times(dataFolder+"times.txt")
	visits = types.Visits(dataFolder+"visits.csv")	
	print(visits.getMatrix())


if __name__ == "__main__":
    # execute only if run as a script
    if(len(sys.argv) != 2):
    	print("Uage :")
    	print("$ python3 __main__.py <dataFolder>")
    	print("exemple :")
    	print("$ python3 __main__.py ./Data/lyon_40_1_1/")
    else: 
    	main(sys.argv)
