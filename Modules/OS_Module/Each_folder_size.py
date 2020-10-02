import os


path = os.getcwd()

lists = os.listdir(path)
for files in lists:
    location = os.path.join(path, files)
    size = os.path.getsize(location)
    print(size)

