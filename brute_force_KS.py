import sys
import time

def powerset(items):
    ret = [[]]
    for item in items:
        newset = [r+[item] for r in ret]
        ret.extend(newset)
    return ret

def knapsackBruteForce(pset, capacity):
    maxProfit = 0
    bestKnapsack = []
    count = 0
    for s in pset:
        count += 1
        currentWeight = sum([item[0] for item in s])
        currentProfit = sum([item[1] for item in s])
        if currentWeight <= capacity and currentProfit > maxProfit:
            bestKnapsack = s
            maxProfit = currentProfit
    print(count)
    return bestKnapsack, maxProfit

file = open(sys.argv[1], "r")
lines = file.readlines()
problemSize = 0
capacity = 0
items = [];
count = -1
for line in lines:
    temp = line.split(",")
    if count == -1:
        problemSize = int(temp[0])
        capacity = int(temp[1])
    else:
       items.append((int(temp[0]), int(temp[1])))
    count = 1

file.close()

start = time.time()
pset = powerset(items)
knapsack, maxProfit = knapsackBruteForce(pset, capacity)
end = time.time()
totalTime = end - start

output = open(sys.argv[2], "w")
output.write("# of Items: " +  str(problemSize) + '\n')
output.write("Capacity: " + str(capacity) + '\n')
output.write("Max Profit: " + str(maxProfit) + '\n')
output.write("Running Time: " + str(totalTime) + '\n')
output.write("----Items-----" + '\n')
for item in knapsack:
    output.write(str(item) + '\n')

output.close()
