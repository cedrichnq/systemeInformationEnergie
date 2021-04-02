from const import TIME_TO_DELIVERY_ONE_ITEM, TIME_TO_DELIVERY
import customTypes as types

def printMatrix(matrix):
	string = ''
	for row in matrix:
		string += str(row) + '\n'
	return string

def parseMatrixFile(file):
	matrix = []
	with open(file, 'r') as fp:
		line = fp.readline()
		while line:
			line = line[:-1] # remove end of line car
			rowData = line.split()
			rowData = [float(numeric_string) for numeric_string in rowData] # convert to floats
			matrix.append(rowData)
			line = fp.readline()
	return matrix

def csvToVisits(file):
	matrix =[]
	with open(file, 'r') as fp:
		line = fp.readline()
		line = fp.readline() # remove header
		while line:
			line = line[:-1] # remove end of line car
			row = line.split(',')
			matrix.append(types.Visit(row))
			line = fp.readline()
	
	return matrix[1:] # remove first line : deposit

def timeToDelivery(nb_tiems):
	return TIME_TO_DELIVERY_ONE_ITEM * nb_tiems + TIME_TO_DELIVERY
