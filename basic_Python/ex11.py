# 11. Write a Python program to check whether a file exists.


import os
exists = os.path.isfile('/home/bridgeit/PycharmProjects/BasicPython/DataStructures/Array2.py')
if exists:
    print("Present")
else:
    print("Not present")