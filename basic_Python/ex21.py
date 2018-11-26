# 21. Write a Python program to sort files by date.

import glob,os
files = glob.glob("*.py")
files.sort(key=os.path.getmtime)
print("\n".join(files))
