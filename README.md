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

Given two <i>n</i>-tuples of postive integers <<i>v</i><sub>1</sub>,<i>v</i><sub>2</sub>,...,<i>v</i><sub>n</sub>> and <<i>w</i><sub>1</sub>,<i>w</i><sub>2</sub>,...,<i>w</i><sub>n</sub>> and <i>W</i>>0 we want to determine the subset ![subset intersection](http://www.sciweavers.org/tex2img.php?eq=T%20%20%5Csubseteq%20%20%5Cbig%5C%7B1%2C2%2C...%2C%5Ctextit%7Bn%7D%5Cbig%5C%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0) (of items to put in knapsack) 

maximize ![maximizes such that the value is highest](http://www.sciweavers.org/tex2img.php?eq=%20%5Csum_%7B%28%5Ctextit%7Bi%7D%20%5Cin%20%5Ctextit%7BT%7D%29%7D%5C%20%5Ctextit%7Bv%7D_i&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0) 

subject to ![maximizes the weight in terms of defined limit](http://www.sciweavers.org/tex2img.php?eq=%20%5Csum_%7B%28%5Ctextit%7Bi%7D%20%5Cin%20%5Ctextit%7BT%7D%29%7D%5C%20%5Ctextit%7Bw%7D_i%20%20%5Cleq%20W&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

# Solving the problem
The knapsack problem is a combinatorial optimization problem and is considered an NP-Complete problem.
![P!=NP Diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/P_np_np-complete_np-hard.svg/300px-P_np_np-complete_np-hard.svg.png)

One possible solution would be to brute force the problem.  This would involve creating every possible combination of items with a total weight less than or equal to the maximim defined weight.  Such a solution would become exponentially more difficult to solve as the number of items increase.