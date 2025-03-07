import os

def check(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
        
        directory = os.path.dirname(path)
        print(f"Directory portion: {directory}")
        
        filename = os.path.basename(path)
        print(f"Filename portion: {filename}")
    else:
        print(f"The path '{path}' does not exist.")

path = r"C:\Users\HOME\Desktop\pp2_2025\lab6\Directories,files Python\test.txt"
check(path)