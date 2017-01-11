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
<i>x</i><sub>i</sub> is the binary decision of whether or not to place item in the knapsack. 

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


A simple python based brute force method can be found [here](https://github.com/AndrewGEvans95/Knapsack/blob/master/solutions/BruteForce.py "0-1 Knapsack brute force solution")

Using a brute force solution would ultimately results in an ![Big O Complexity](https://raw.githubusercontent.com/AndrewGEvans95/Knapsack/master/resources/Time%20Complexity%20of%20Brute%20Force.png) time complexity.
At this point we ask our selves, "How can I make this faster?"
The answer, such is the case for almost all of life's problems, is to divide and conquer.  

Well not actually.

><i>"There were timelines branching and branching, a mega-universe of universes, millions more every minute. Billions? Trillions? The universe split every time someone made a decision. Split, so that every decision ever made could go both ways. Every choice made by every man, woman, and child was reversed in the universe next door."</i> ― (Larry Niven. <i>All the Myriad Ways.</i> 1985)

Dividing the problem into subproblems would not result in a faster solution time due to the fact that breaking down combinatorial optimization problems results in subproblems which are not indepedent, i.e. subproblems share subsubproblems, which results in repeatedly solving the same common subsubproblems.  Doing more work than is nessecary is typically frowned upon by computer scientists and, well, just about anyone.

# Going a Step Beyond Divide and Conquer
The main issue with the divide and conquer technique is the extra work required to repeatedly solve subsubproblems which have already been solved by other subproblems.

The answer: Dynamic Programming

# Dynamic Programming: An Adventure in Space Time
The main idea behind dynamic programming is to compute the solutions to subsubproblems once and store the solutions in an array so that they may be reused later.
This ultimately increases the amount of memory used while decreasing the time needed to solve the problem.  This is refered to as Space-Time tradeoff.

# The Basics of Constructing a Dynamic Programming Solution
1. Break the problem into smaller subproblems and characterize the structure of an optimal solution.
  * First we constuct an array V[0..<i>n</i>, 0..W].  For 1 <= <i>i</i> <= <i>n</i>, and 0 <= <i>w</i> <= W, where V[<i>i</i>,<i>w</i>] will store the maximum weight of any subset of item {1,2,...,<i>i</i>} of combined value at most <i>w</i>.  This means that the array entry V[<i>n</i>, W] will contain the highest sum total value of items that meet the set weight constraint.
2. Recursively define the definition of an optimal solution
  * Initial settings V[0, <i>w</i>]=0 for 0<=<i>w</i><=W, and any V[0, <i>w</i>]=-inifinty for <i>w</i><=0 is illegal.  Our recursive step is V[<i>i</i>,<i>w</i>]=max(V[<i>i-1</i>,<i>w</i>],<i>v<sub>i</sub></i>+V[<i>i</i>-1,<i>w</i>-<i>w<sub>i</sub></i>]) for 1<=<i>i</i><=<i>n</i>, 0<=<i>w</i><=W.
3. Compute the value of an optimal solution in a bottom-up fashion using a table structure
  * Bottom: V[0,<i>w</i>]=0 for all 0<=<i>w</i><=W Bottom up: V[<i>i</i>,<i>w</i>]=max(V[<i>i-1</i>,<i>w</i>],<i>v<sub>i</sub></i>+V[<i>i</i>-1,<i>w</i>-<i>w<sub>i</sub></i>])
4. Find optimal solution using the computed information
