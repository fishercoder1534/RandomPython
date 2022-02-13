import os, shutil, getpass
from random import randint

number = randint(100, 999)
file_name = f'practice{number}.txt'
f = open(file_name, 'w+')
f.write('This is a text string')
f.close()

print(os.getcwd())
print(os.listdir())
print(getpass.getuser())
user = getpass.getuser()

shutil.move(file_name, f'/Users/{user}/Personal/RandomPython/NoteBook')
