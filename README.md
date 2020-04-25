# cs375GroupProject
Spring 2020 CS 375 Group Project
Execution instructions:

1. install Python, preferably enter as PATH or environmental variable
2. Enter directory with .py file
3. In linux terminal enter "python backtrack.py <input.txt> <output.txt>"
or "python brute_force_KS.py <input.txt> <output.txt>"
or "python brute_force_optimized.py <input.txt> <output.txt>"
or "python executor.py <numberofelements(int)> <testingiterations(int)>
___________________________________________________________
backtrack.py:
Immutable arrays for holding items and some single lists for output. 
Global variables because implementing a class is slower.
Initial sort on items is O(nlogn), so add bound complexity from the algorithm and worst time complexity is O(2^n)


brute_force_KS.py and brute_force_optimized: serves to find solution to 0-1 knapsack by generating all sets
powerset that has all combinations of elements. Immutable arrays for holding items and some single and double lists for output. 
optimized version does not check sets of certain length.
Worst time complexity is O(2^n)

executor.py
Uses subprocess to call other scripts. No structures. Can randomly generate data.



