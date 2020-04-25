#!/usr/bin/env python
# sys for input, time for complexity
import sys
import copy
import time

# You could place these in a class but it will be slower
# include is a temp solution for every recursive iteration
# maxprofit is global variable for holding end profit
# bestset is global varaiable for holding end solution
maxprofit = 0.0
include = []
bestset = []

# findBound(i, items, weight_limit) takes item array of values and weights, their size and capacity limit
# and uses the passed i to grab the values
# by iterating from the starting level through the remaning items, a bound can be formed from a fraction of an item that exceeds capacity
def findBound(i, profit, weight, items, weight_limit):
    # max_profit comparison
    bound = int(profit)
    # temp value starting with weight
    total_weight = weight
    # starting at i and iterating through adding to bound the items remaining
    while i < len(items) and total_weight + items[i][0] <= weight_limit:
        total_weight += items[i][0]
        bound += items[i][1]
        i += 1
    if i < len(items):
        bound += int((float(weight_limit) - float(total_weight)) * (float(items[i][1]) / float(items[i][0])))
    return bound


# promising(i, items, weight_limit) takes profit, weight, and items array so that it can pass to findBound
# this compares the generated bound from the remaining items and checks it against the max profit
def promising(i, profit, weight, items, weight_limit):
    if i + 1 >= len(items) or weight >= weight_limit:
        return False
    # bound returned
    bound = findBound(i + 1, profit, weight, items, weight_limit)
    global maxprofit
    return bound > maxprofit

# knapsack(i, profit, weight, weight_limit, items) passes an array of values and weights along with the size and capacity limits
# Its purpose is to check both paths for taking an item and not taking an item in the knapsack
# It then forms a bound for a node based on the possible remaining items
# depending on that bound, a path is chosen or not chosen
# it doesn't return anything and instead changes maxprofit and bestset global variables
def knapsack(i, profit, weight, weight_limit, items):
    # all variables in function are previously declared global variables
    global maxprofit
    if weight <= weight_limit and profit > maxprofit:
        maxprofit = profit
        global include
        global bestset
        bestset = copy.copy(include)
    if promising(i, profit, weight, items, weight_limit):
        include[i + 1] = 1
        knapsack(i + 1, profit + items[i + 1][1], weight + items[i + 1][0], weight_limit, items)
        include[i + 1] = 0
        knapsack(i + 1, profit, weight, weight_limit, items)

# main execution path
def main():
    # file and output are arguments that are passed in command line
    input = sys.argv[1]
    output = sys.argv[2]

    # basic definitions that aren't actually needed here because its python
    # item array for weight and value
    items = []
    # previously declared global variables
    global maxprofit
    maxprofit = 0.0
    global include
    include = [0]
    global bestset
    # item array for weight and value but they aren't converted to float ( so output can look like input)

    with open(input, 'r') as file:
        split_line = file.readline().split(',')
        num_items = int(split_line[0])
        weight_limit = int(split_line[1])

        for i, line in enumerate(file):
            if i <= num_items:
                include.append(0)
                items.append((float(line.strip().split(',')[0]), float(line.strip().split(',')[1])))

    # start_time and total time: timing for algorithm
    start_time = time.time()
    items.sort(key=lambda item: item[1] / item[0], reverse=True)
    items.insert(0, (0, 0))
    knapsack(0, 0, 0, weight_limit, items)
    total = time.time() - start_time
    print(total)

    with open(output, "w") as file:
        file.write(str(num_items) + ",")
        if maxprofit.is_integer():
            file.write(str(int(maxprofit)) + "\n")
        else:
            file.write(str(maxprofit) + "\n")
        for i in range(1, len(bestset)):
            if bestset[i] == 1:
                file.write(str(items[i][0]) + "," + str(items[i][1]) + "\n")


if __name__ == "__main__":
    main()