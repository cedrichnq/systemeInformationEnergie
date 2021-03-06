from customTypes import Car, MatrixFromFile, Visits
from heuristics import heuristic
from metaHeuristics import metaHeuristic1, metaHeuristic2, metaHeuristic3
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
    car = Car.getCar(dataFolder + "/vehicle.ini")
    distances = MatrixFromFile(dataFolder + "/distances.txt")
    times = MatrixFromFile(dataFolder + "/times.txt")
    visits = Visits(dataFolder + "/visits.csv")
    context = (distances, times, car)

    result = heuristic(visits, context)
    writeToCsv(result, RESULTS_DIR + 'result1.csv')
    print("Le fichier de resultat s'appel result1.csv")

    better_result = metaHeuristic3(result, context)
    print(result)
    print(better_result)
    writeToCsv(better_result, RESULTS_DIR + 'better_result.csv')
    print("Le fichier de resultat s'appel better_result1.csv")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uage :")
        print("$ python3 tp_script <dataFolder>")
        print("exemple :")
        print("$ python3 tp_script ./Data/lyon_40_1_1/")
    else:
        dataFolder = sys.argv[1]
        main(dataFolder)

