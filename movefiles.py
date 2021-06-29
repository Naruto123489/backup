import os
import shutil
source=input("type the source folder name:  ")
dest=input("enter destination folder name:  ")
source= source+'/'
dest= dest+'/'
list_of_files= os.listdir(source)
for file in list_of_files:
    shutil.move((source+file),dest)