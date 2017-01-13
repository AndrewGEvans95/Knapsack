#weight     |   value
#-----------|----------
#   15      |   2
#   13      |   5
#   13      |   9
#   12      |   5
#   12      |   9
#   11      |   7
#(weight, value)
items = [(15, 2), (13, 5), (13, 9), (12, 5), (12, 9), (11, 7)]
#Weight capacity
W = 100

# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W
def knapSack(W, wt, val, n):

    #Create table
    V = [[0 for x in range(W+1)] for x in range(n+1)]
    print V
    keepTable = [[0 for x in range(W+1)] for x in range(n+1)]
    # Build table K[][] in bottom up manner
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                V[i][w] = 0
                keepTable[i][w] = 1
            #If this item weighs less than or equal to the previous item    
            elif wt[i-1] <= w:
                if(((val[i-1] + V[i-1][w-wt[i-1]]) > V[i-1][w])):
                    V[i][w] = (val[i-1] + V[i-1][w-wt[i-1]])
                    keepTable[i][w] = 1
                else:
                    V[i][w] = V[i-1][w]
                    keepTable[i][w] = 0
                #V[i][w] = max(val[i-1] + V[i-1][w-wt[i-1]],  V[i-1][w])
                print str(val[i-1] + V[i-1][w-wt[i-1]]) + " vs " + str(V[i-1][w]) + " new K cell value " + str(V[i][w])
    K = W
    for i in range(n):
        if(keepTable[i][K]==1):
            print items[i]
            K = K-wt[i]
            print K
    print keepTable
    return V[n][W]
wt, val = zip(*items)
n = len(items)
print knapSack(W, wt, val, n)