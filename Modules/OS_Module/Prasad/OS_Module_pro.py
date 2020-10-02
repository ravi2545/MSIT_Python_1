import os
import os.path

#for item in [attribute for attribute in dir(os) if not attribute.startswith('__')]:
    #print(item)


python_files = []
g = os.walk(os.getcwd())


for dir_path, directory_names, file_names in g:
    for filename in file_names:
        if filename.endswith(".py"):
            #print(dir_path+"\\"+filename)
            #print(os.path.join(dir_path,filename))
            python_files.append(os.path.join(dir_path,filename))


for python_file in python_files:
    print(python_file)
