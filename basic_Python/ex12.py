# 12. Write a python program to call an external command in Python.
from subprocess import  *
command = input("Enter command you want to call : ")
call(command)