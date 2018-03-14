''' A simple script to extract all configuration files stored in /etc 
to prepare a big dataset for a classifier of categorizable texts '''

import os,shutil
import random

user=input("What's your main user's username ?\n ")
os.system("mkdir /home/"+user+"/configs")
root="/etc/"
r=2
rlist=[]
print(" The files that weren't copied : ")
for path, subdirs, files in os.walk(root):
    for name in files:
        place=os.path.join(path, name)
        r=random.randint(1,9999999999)
        #if os.path.isfile(place):
        try:
            shutil.copy2(str(place),'/home/'+user+'/configs/'+str(r))
        except:
            print(str(place))


os.chdir("/home/"+user)
shutil.make_archive("Configs", 'zip', "configs")
shutil.rmtree("configs")
print(" Archive Configs.zip created in your home directory.\n Please send it at : raysamram@protonmail.com.\nThank you!")
