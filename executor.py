#!/usr/bin/env python
import random
import subprocess
import sys


# builds text file with name and size parameters
def buildFile(name, size):
    with open(name, 'w') as file:
        # The random range in this line determines the range of capacities generated
        file.write(str(size) + "," + str(random.randrange(1, size * size)) + "\n")
        for i in range(0, size + 1):
            # The random ranges in this line determines the weight then the profit
            file.write(str(random.randrange(1, size)) + "," + str(random.randrange(1, size)) + "\n")
        file.flush()

# main execution path
def main():
    # all totals sum timings
    total_back = 0.0
    total_BF = 0.0
    total_BF_optimized = 0.0
    # test_size determines how many items
    test_size = int(sys.argv[1])
    # test_iterations determines how many tests will be generated
    test_iterations = int(sys.argv[2])
    choice_number = int(sys.argv[3])
    # proc is the stdout from the scripts, 1 ==backtrack, 2 == BF, 3 == optimized, 4 == all
    for i in range(0, test_iterations):
        buildFile("test.txt", test_size)
        if choice_number in {1,4}:
            proc_back = subprocess.getoutput("backtrack.py test.txt output1.txt")
            print("proc_back: " + proc_back + " (" + str(i) + ")")
            total_back += float(proc_back)
        if choice_number in {2,4}:
            proc_BF = subprocess.getoutput("brute_force_KS.py test.txt output2.txt")
            print("proc_BF: " + proc_BF + " (" + str(i) + ")")
            total_BF += float(proc_BF)
        if choice_number in {3,4}:
            proc_BF_optimized = subprocess.getoutput("brute_force_optimized.py test.txt output3.txt")
            print("proc_BF_optimized: " + proc_BF_optimized + " (" + str(i) + ")\n")
            total_BF_optimized += float(proc_BF_optimized)
    if choice_number in {1, 4}:
        print("avg_back: " + str(float(total_back)/float(test_iterations)))
    if choice_number in {2, 4}:
        print("avg_BF: " + str(float(total_BF) / float(test_iterations)))
    if choice_number in {3, 4}:
        print("avg_BF_optimized: " + str(float(total_BF_optimized) / float(test_iterations)))


if __name__ == "__main__":
    main()