# 0-1 Knapsack
A dynamic programming solution to the 0-1 Knapsack problem

![Knapsack](https://upload.wikimedia.org/wikipedia/commons/e/ec/19th_century_knowledge_hiking_and_camping_sheepskin_knapsack_sleeping_bag_rolled_up.jpg)

# The Problem
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.  Moreover, there is only one of each item (you can't put the same item in the bag more than once) and the weight and value of each item are non-negetive integers.

# A More Formal Mathematical Definition
This problem is considered a 0-1 Knapsack Problem because it restricts the number of instances of an item that are placed in the knapsack to zero or one (not in the knapsack or in the knapsack).

Given a set of <i>n</i> items numbered from 1 up to <i>n</i>, each with a weight <i>w<sub>i</sub></i> and a value <i>v<sub>i</sub></i>, along with a maximum weight capacity <i>W</i>, 

maximize ![maximize knapsack weight](https://wikimedia.org/api/rest_v1/media/math/render/svg/85620037d368d2136fb3361702df6a489416931b)

subject to ![maximize knapsack value and weight bound by max weight](https://wikimedia.org/api/rest_v1/media/math/render/svg/dd6e7c9bca4397980976ea6d19237500ce3b8176) and ![maximize such that item either exists in bag or does not](https://wikimedia.org/api/rest_v1/media/math/render/svg/07dda71da2a630762c7b21b51ea54f86f422f951).

# A More Formal Programmer Friendly Definition
We will define <i>i</i> as an item which has
<i>w<sub>i</sub></i> weight and <i>v<sub>i</sub></i> value.

Given two <i>n</i>-tuples of postive integers <<i>v</i><sub>1</sub>,<i>v</i><sub>2</sub>,...,<i>v</i><sub>n</sub>> and <<i>w</i><sub>1</sub>,<i>w</i><sub>2</sub>,...,<i>w</i><sub>n</sub>> and <i>W</i>>0 we want to determine the subset ![subset intersection](https://raw.githubusercontent.com/AndrewGEvans95/Knapsack/master/resources/T%20exists%20in%20set.png) (of items to put in knapsack) 

maximize ![maximizes such that the value is highest](https://raw.githubusercontent.com/AndrewGEvans95/Knapsack/master/resources/Sum%20of%20values%20in%20set.png) 

subject to ![maximizes the weight in terms of defined limit](https://raw.githubusercontent.com/AndrewGEvans95/Knapsack/master/resources/Sum%20of%20weight%20in%20set.png)

# Solving the problem
The knapsack problem is a combinatorial optimization problem and is considered an NP-Complete problem.
![P!=NP Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/P_np_np-complete_np-hard.svg/300px-P_np_np-complete_np-hard.svg.png)

One possible solution would be to brute force the problem.  This would involve creating every possible combination of items with a total weight less than or equal to the maximim defined weight.  Such a solution would become exponentially more difficult to solve as the number of items increase.
