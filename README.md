# 0-1 Knapsack
A dynamic programming solution to the 0-1 Knapsack problem

![Knapsack](https://upload.wikimedia.org/wikipedia/commons/e/ec/19th_century_knowledge_hiking_and_camping_sheepskin_knapsack_sleeping_bag_rolled_up.jpg)

# The Problem
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.  Moreover, there is only one of each item (you can't put the same item in the bag more than once) and the weight and value of each item are non-negetive integers.

# A More Formal Mathematical Definition
This problem is considered a 0-1 Knapsack Problem because it restricts the number of instances of an item that are placed in the knapsack to zero or 1 (not the knapsack or in the knapsack).

Given a set of <i>n</i> items numbered from 1 up to <i>n</i>, each with a weight <i>w<sub>i</sub></i> and a value <i>v<sub>i</sub></i>, along with a maximum weight capacity <i>W</i>, 

maximize ![maximize knapsack weight](https://wikimedia.org/api/rest_v1/media/math/render/svg/85620037d368d2136fb3361702df6a489416931b)

subject to ![maximize knapsack value and weight bound by max weight](https://wikimedia.org/api/rest_v1/media/math/render/svg/dd6e7c9bca4397980976ea6d19237500ce3b8176) and ![maximize such that item either exists in bag or does not](https://wikimedia.org/api/rest_v1/media/math/render/svg/07dda71da2a630762c7b21b51ea54f86f422f951).

# A More Formal Programmer Definition
Given two <i>n</i>-tuples of postive integers <<i>v</i><sub>1</sub>,<i>v</i><sub>2</sub>,...,<i>v</i><sub>n</sub>> and <<i>w</i><sub>1</sub>,<i>w</i><sub>2</sub>,...,<i>w</i><sub>n</sub>>
