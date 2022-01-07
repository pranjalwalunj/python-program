import os
path = os.curdir
print(path)
os.chdir(path)
for f in os.listdir():
    print(f)






