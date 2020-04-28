#!/usr/bin/env python
import sys
import time

# powerset(items) takes item list of weights and profits
# creates a powerset(true combination) of all items as separate list elements
def powerset(items):
    # return double list
    ret = [[]]
    for item in items:
        newset = [r+[item] for r in ret]
        ret.extend(newset)
    return ret

# knapsackBruteForce(pset, capacity) takes generator powerset(list) and capacity
# it goes through every element in the psets and sums their profit and makes sure they are under capacity
def knapsackBruteForce(pset, capacity, maxSetSize):
    # maxprofit holds best value outide of for loop
    # bestKnapsack holds solution
    # count optional
    maxProfit = 0
    bestKnapsack = []
    count = 0
    for s in pset:
        if len(s) <= maxSetSize:
            count += 1
            # the sum of current element in pset
            currentWeight = sum([item[0] for item in s])
            currentProfit = sum([item[1] for item in s])
            if currentWeight <= capacity and currentProfit > maxProfit:
                bestKnapsack = s
                maxProfit = currentProfit
    return bestKnapsack, maxProfit


# main execution path
# read variables
file = open(sys.argv[1], "r")
lines = file.readlines()
# storing data from text files, item is list of profit and weights
problemSize = 0
capacity = 0
items = []
weights = []
count = -1
for line in lines:
    temp = line.split(",")
    if count == -1:
        problemSize = int(temp[0])
        capacity = int(temp[1])
    else:
       items.append((int(temp[0]), int(temp[1])))
       weights.append(int(temp[0]))
    count = 1

file.close()

start = time.time()
#The weights will be sorted in acsending order
weights.sort()
#All n items weights will be added and if their weight is 
#over the capacity we know we wont have to check sets of size n
#Repeat for items 1 to n-1 and so on
n = problemSize

for index in weights:
    totalSum = sum(weights[0:n])
    if totalSum <= capacity:
        break;
    n -= 1

# timings, and return variables
pset = powerset(items)
knapsack, maxProfit = knapsackBruteForce(pset, capacity, n+1)
end = time.time()
totalTime = end - start
print(totalTime)
output = open(sys.argv[2], "w")
#output.write("# of Items: " +  str(problemSize) + '\n')
#output.write("Capacity: " + str(capacity) + '\n')
#output.write("Max Profit: " + str(maxProfit) + '\n')
#output.write("Running Time: " + str(totalTime) + '\n')
#output.write("----Items-----" + '\n')
output.write(str(problemSize) + "," + str(maxProfit) + "," + str(totalTime) + "\n");
for item in knapsack:
    output.write(str(item) + '\n')

output.close()
