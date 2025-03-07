import os

def delete_file(file_path):
    if os.path.exists(file_path):
        print(f"The file '{file_path}' exists.")
        
        if os.access(file_path, os.R_OK | os.W_OK):
            print(f"The file '{file_path}' is accessible.")
            
            os.remove(file_path)
            print(f"The file '{file_path}' has been deleted.")
        else:
            print(f"The file '{file_path}' is not accessible (missing read/write permissions).")
    else:
        print(f"The file '{file_path}' does not exist.")

file_path = r"C:\Users\HOME\Desktop\pp2_2025\lab6\Directories,files Python\test.txt"
delete_file(file_path)