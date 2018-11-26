# 2. Write a Python program to get the command-line arguments (name of the script,
#  the number of arguments, arguments) passed to a script.

import sys
print("Name of the script : "),sys.argv[1]
print("The number of arguments : ", len(sys.argv))
print("Arguments : ", str(sys.argv))