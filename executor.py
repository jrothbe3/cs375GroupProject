#!/usr/bin/env python
import random
import subprocess
import sys
import os

# builds text file with name and size parameters
def buildFile(name, size):
    with open(name, 'w') as file:
        file.write(str(size) + "," + str(random.randrange(5000, 10000)) + "\n")
        for i in range(0, size + 1):
            file.write(str(random.randrange(1, 100)) + "," + str(random.randrange(1, 300)) + "\n")
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
    for i in range(0, test_iterations):
        buildFile("test.txt", test_size)
        proc_back = subprocess.getoutput("backtrack.py test.txt output.txt")
        proc_BF = subprocess.getoutput("brute_force_KS.py test.txt output.txt")
        proc_BF_optimized = subprocess.getoutput("brute_force_optimized.py test.txt output.txt")
        print("proc_back: " + proc_back + " (" + str(i) + ")")
        print("proc_BF: " + proc_BF + " (" + str(i) + ")")
        print("proc_BF_optimized: " + proc_BF_optimized + " (" + str(i) + ")\n")
        total_back += float(proc_back)
        total_BF += float(proc_BF)
        total_BF_optimized += float(proc_BF_optimized)
    print("avg_back: " + str(float(total_back)/float(test_iterations)))
    print("avg_BF: " + str(float(total_BF) / float(test_iterations)))
    print("avg_BF_optimized: " + str(float(total_BF_optimized) / float(test_iterations)))


if __name__ == "__main__":
    main()