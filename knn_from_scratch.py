import csv
import random

# loading the data from the iris.data file
def load_data(filename, split, train_set=[] , test_set=[]):
	with open(filename, 'rt') as input_data:
		lines = csv.reader(input_data)
		main_data = list (lines)
		for x in range(len(main_data)-1):
			for y in range(4):
				main_data[x][y] = float(main_data[x][y])
			if random.random() < split:
				train_set.append(main_data[x])
			else:
				test_set.append(main_data[x])

# calulating ecludiean distance
import math
def get_euclidean_distance(point_1, point_2, length):
	distance = 0
	for x in range(length):
		distance += pow((point_1[x] - point_2[x]), 2)
	return math.sqrt(distance)

# choosing subset with the smallest distance
import operator 
def get_closest_neighbors(train_set, test_instance, k):
	distances = []
	length = len(test_instance)-1
	for x in range(len(train_set)):
		dist = get_euclidean_distance(test_instance, train_set[x], length)
		distances.append((train_set[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

# predict the output for given input
import operator
def get_votes(neighbors):
	votes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in votes:
			votes[response] += 1
		else:
			votes[response] = 1
	sortedVotes = sorted(votes.items(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]

# calculate accuracy of the code
def get_accuracy(test_set, predictions):
	correct = 0
	for x in range(len(test_set)):
		if test_set[x][-1] in predictions[x]: 
			correct+=1			
	return (correct/float(len(test_set))*100) 

def main():
	# prepare data
	train_set=[]
	test_set=[]
	split = 0.67
	load_data('iris.data', split, train_set, test_set)
	print ('Train set: ' + repr(len(train_set)))
	print ('Test set: ' + repr(len(test_set)))
	# generate predictions
	predictions=[]
	k = 3
	for x in range(len(test_set)):
		neighbors = get_closest_neighbors(train_set, test_set[x], k)
		result = get_votes(neighbors)
		predictions.append(result)
		print('> predicted=' + repr(result) + ', actual=' + repr(test_set[x][-1]))
	accuracy = get_accuracy(test_set, predictions)
	print('Accuracy: ' + repr(accuracy) + ' %')
	
main()