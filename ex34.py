# 34. Write a Python program to retrieve file properties.

import os.path
import time

print('File Name with path   :', __file__)
print('Access time  :', time.ctime(os.path.getatime(__file__)))
print('Modification time:', time.ctime(os.path.getmtime(__file__)))
print('Change time  :', time.ctime(os.path.getctime(__file__)))
print('Size         :', os.path.getsize(__file__))