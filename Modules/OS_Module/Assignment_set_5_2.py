import os


total_size = 0
g_path = os.walk(os.getcwd())
sizes = []
for path, dirs, files in g_path:
     for d in dirs:
         for file_name in files:
            fp = os.path.join(path, file_name)
            total_size+= os.path.getsize(fp)
            print(d,total_size)
            
        
        
#print("Directory size:{} KB ".format(total_size/1024))



