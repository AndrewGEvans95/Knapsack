#A brute force solution to the 0-1 Knapsack Problem
#weight     |	value
#-----------|----------
#	15  |	2
#	13  |	5
#	13  |	9
#	12  |	5
#	12  |	9
#	11  |	7
#(weight, value)
items = [(15, 2), (13, 5), (13, 9), (12, 5), (12, 9), (11, 7)]
#Weight capacity
W = 20

def solve(items, weight):
	#First we need every possible combination of our set
	combinations = [[]]
	bestSolution = []

	#Initilize best value and weight variables
	bestValue = 0
	bestWeight = 0

	#Create a powerset of the possible items
	for i in items:
		newsubsets = [subset + [i] for subset in combinations]
		combinations.extend(newsubsets)
	#At least one item needs to go into the knapsack
	combinations.pop(0)

	#Go through each subset of the powerset to find optimal solution
	for lists in combinations:
		
		#Initilize value and weight of each subset
		sumValue = 0
		sumWeight = 0
		
		#Traverse the subsets and add up weights and values
		for i in lists:
			sumWeight = sumWeight+i[0]
			sumValue = sumValue+i[1]

		#Set the best solution to the value of the subset that is below or equal to the set constraint W, and the value is greater than previous best solutions
		if sumWeight <= weight and sumValue > bestValue:
			bestValue = sumValue
			bestWeight = sumWeight
			bestSolution = lists
	print "The best solution is " + str(bestSolution) + " with a weight of " + str(bestWeight) + " and value of " + str(bestValue)

solve(items, W)
