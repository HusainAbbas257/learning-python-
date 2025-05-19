import os

# we can get current working directory by os.getcwd()
curent_dir=os.getcwd()
print(curent_dir)

# to create a directory by ourself we use mkdir
path="C:/Users/DELL/Desktop/created by python"
try:
    os.mkdir(path)
except Exception as e:
    print("error occured while making files ")
else:
    print(f'made file succesfully->{path}')


# to rename any folder or file we use rename(original name,new name)
new_name='C:/Users/DELL/Desktop/created using os module'
try:
    os.rename(path,new_name)
except Exception as e:
    print("error occured while renaming files")
else:
    print(f'renamed file succesfully->{new_name}')


# to check wether a file exist ort not we use
print(os.path.exists(new_name))


# to get a list of all directories within a file we use listdir()
list_dir=os.listdir('C:/Users/DELL/Desktop/Learning-python-')
print(list_dir)

# to Check if it's a file or folder
print(os.path.isdir(new_name))
print(os.path.isfile(new_name))  

# to change current directory we use chdir()
os.chdir('C:/Users/DELL/Desktop/Learning-python-/modules and packages/in built modules')
print(os.getcwd())

# to run a specific command we use 
os.system("echo \" hey i made it inside python\" ")


# to open a specific file we use
os.startfile(os.getcwd())

#to delete any file we use:
try:
    os.remove('C:/Users/DELL/Desktop/num.txt')
    print(os.path.exists('C:/Users/DELL/Desktop/num.txt'))
except Exception as e:
    print(e)

# to remove a  empty folder we use
try:
    os.rmdir(new_name)
    print(os.path.exists(new_name))
except Exception as e:
    print(e)