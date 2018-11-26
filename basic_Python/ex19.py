# 19. Write a Python program to get file creation and modification date/times.

import os.path, time
print("creation time : " , time.ctime(os.path.getmtime("ex5.py")))
print("Modification Time : ", time.ctime(os.path.getctime('ex5.py')))