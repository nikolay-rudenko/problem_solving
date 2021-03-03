from os import listdir
from os.path import isfile, join


path = 'D:/Books/books about python'
only_files = [f for f in listdir(path) if isfile(join(path, f))]


for file in only_files:
    if 'api' in file:
        print(file)
