# kNN algorithm implemention from scratch in python
# Description of assignment

**Goal: To implement the kNN algorith from scratch.**
In this assignment, kNN algorithm is implemented without using any library function. The code is tested on the iris.data dataset.

**Purpose**

- kNN is a widely used intuitive algorithm in the machine learning domain.
- With this project I wanted to explore the kNN in details and implement it from the very begining. 


**kNN Algorithm**

- The kNN algorithm is part of the instance-based, competitive, and lazy learning algorithms families. Instance-based algorithms generate predictions by modeling the problem using data instances (or rows). Because all training observations are maintained as part of the model, the kNN algorithm is an extreme example of instance-based methods. 

- The term "lazy learning" refers to the fact that algorithm does not construct a model until a prediction is needed. It is sluggish because it only works at the last possible moment. This has the advantage of only adding data that is relevant to the unknown data, which is referred to as a localized model. One problem is that running the same or similar searches on huge training datasets can be computationally expensive.

- Lastly, kNN is efficient because it makes no assumptions about the data other than that a distance measure between any two instances may be calculated reliably. Because it does not adopt a functional form, it is referred to as non-parametric or non-linear.

**Project details**

- Envoirment: Windows 10
- Python 3.9
- Libraries used: csv, random, operator, math
- How to run?: Clone the Git repository and run knn_from_scratch.py

**About code**

Code consists of four functions, they are as follow:
1. `load_data()`
	- It reads the 'iris.data' file and splits the data into two parts for training and testing purposes.

2. `get_euclidean_distance()`
	- As kNN is a distance based algorithm, this function is used to calculate the distance between two dataset points.
	- It takes input of two points and the lenghth of the test dataset.
	- Formula: https://www.gstatic.com/education/formulas2/443397389/en/euclidean_distance.svg

3. `get_votes()`
	- After the distance is calculated then we need to find the 'k' nearest points to categorize the input point.
	- It creates a Python dictionary in which all the nodes and votes are placed as key-value pair.
	- This dictonary is sorted in reverse order so that it can show top closest neighbors.

4. `get_accuracy()`
	- Calculating accuracy of a machine learning model is very important step.
	- This function takes sorted dictionary as input from 'get_votes' function and checks the if it consists correct entries by comparing to the test dataset.
	- If entry is correct then a counter is incremented and in the end accuracy is calculated by dividing counter by the size of test dataset.
