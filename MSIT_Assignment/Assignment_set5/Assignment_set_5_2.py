import os
directory_size = 0
large_size = 0
large_directory = ''
k = int(input("Enter how many directories you want to compare:"))

fsizedicr = {'Bytes': 1, 'Kilobytes': float(1)/1024, 'Megabytes': float(1)/(1024*1024), 'Gigabytes': float(1)/(1024*1024*1024)}
for i in range(k):
    HOME_FOLDER = input("Enter directory path:")
    for (path, dirs, files) in os.walk(HOME_FOLDER):
        for file in files:
            filename = os.path.join(path, file)
            directory_size += os.path.getsize(filename)
    if int(directory_size) > int(large_size):
        large_directory = HOME_FOLDER
        large_size = directory_size
    directory_size = 0


#for key in fsizedicr:
#print ("Folder Size: " + str(round(fsizedicr[key]*large_size, 2)) + " " + key)
print("Large Directory is " + large_directory)





