# 25. Write a Python program to get the current value of the recursion limit.

import sys
print("System defined recursion limit : ",sys.getrecursionlimit())
sys.setrecursionlimit(2000)
print("User defined recursion limit : ", sys.getrecursionlimit())