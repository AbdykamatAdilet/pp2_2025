import os

def list_directories(path):
    print("Directories:")
    for entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, entry)):
            print(entry)

def list_files(path):
    print("Files:")
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(entry)

def list_all(path):
    print("All directories and files:")
    for entry in os.listdir(path):
        print(entry)

path = "."

list_directories(path)
print()
list_files(path)
print()
list_all(path)