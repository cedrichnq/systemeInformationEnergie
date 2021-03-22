from const import ID, NAME, DEMAND
from libs import parseMatrixFile, printMatrix, csvToVisits
import datetime

class Distances:
    """
        Distances matrix
    """

    def __init__(self, distancesFile):
        self.distances = parseMatrixFile(distancesFile)

    def getMatrix(self): 
        return self.distances

    def __str__(self):
        return printMatrix(self.distances)

    def getDistanceBetween(self, pos1, pos2):
        return self.distances[pos1][pos2]

    def distToDeposit(self, pos):
        return self.distances[pos][0]


class Times:
    def __init__(self, timesFile):
        self.times = parseMatrixFile(timesFile)

    def getMatrix(self): 
        return self.times

    def __str__(self):
        return printMatrix(self.times)

    def getTimeBetween(self, pos1, pos2):
        return self.times[pos1][pos2]

    def timeToDeposit(self, pos):
        return self.times[pos][0]


class Car:
    """
        A car wich run and delivery things until she need to be refilled. That's a car life.
    """

    def getCar(initFile):
        with open(initFile, 'r') as fp:
            line = fp.readline()
            while line:
                line = line[:-1] # remove end of line car
                if(line.startswith('max_dist')):
                    max_dist = float(line.partition('= ')[2])
                if(line.startswith('capacity')):
                    capacity = float(line.partition('= ')[2])
                if(line.startswith('charge_fast')):
                    charge_fast = float(line.partition('= ')[2])
                if(line.startswith('charge_medium')):
                    charge_medium = float(line.partition('= ')[2])
                if(line.startswith('charge_slow')):
                    charge_slow = float(line.partition('= ')[2])
                if(line.startswith('start_time')):
                    start_time_string = line.partition('= ')[2]
                    start_time_time = datetime.datetime.strptime(start_time_string, '%H:%M').time()
                    start_time = start_time_time.hour * 60 * 60 + start_time_time.minute * 60
                if(line.startswith('end_time')):
                    end_time_string = line.partition('= ')[2]
                    end_time_time = datetime.datetime.strptime(end_time_string, '%H:%M').time()
                    end_time = end_time_time.hour * 60 * 60 + end_time_time.minute * 60
                line = fp.readline()

        return Car(capacity, max_dist, start_time, end_time)

    def __init__(self, capacity, maxDist, start_time, end_time):
        self.capacity = capacity        # the number of objects that can be carry by the car
        self.filling = 0                # number of items carried 
        self.max_dist = maxDist         # maximum distance the car can drive
        self.charge = maxDist           # the number of kilometers that the car can still drive
        self.start_time = start_time    # in secondes
        self.end_time = end_time        # in secondes

    def move(self, distance):
        self.charge -= distance

    def refill(self):
        self.charge = self.max_dist


class Visit: 
    """
        A point to delivery
    """

    def __init__(self, rawVisit):
        self.id = int(rawVisit[ID])
        self.name = rawVisit[NAME]
        self.demand = int(rawVisit[DEMAND])

    def __str__(self):
        return '[id: ' + str(self.id) + ', name: ' + str(self.name) + ', demand: ' + str(self.demand) + ']'


class Visits:
    """
        List of visits, without first line : deposit
    """

    def __init__(self, visitsFile):
        self.visits = csvToVisits(visitsFile)

    def getMatrix(self):
        return self.visits

    def __str__(self):
        return printMatrix(self.visits)

    def sortByDemand(self):
        return self.visits.sort(key = lambda x: x.demand, reverse=True)
