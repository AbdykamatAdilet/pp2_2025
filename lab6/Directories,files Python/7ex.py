def copy_file(source_file, destination_file):
    with open(source_file, 'r') as src:
        contents = src.read()
    
    with open(destination_file, 'w') as dest:
        dest.write(contents)
    
    print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")

source_file = r"C:\Users\HOME\Desktop\pp2_2025\lab6\Directories,files Python\test.txt" 
destination_file = r"C:\Users\HOME\Desktop\pp2_2025\lab6\Directories,files Python\test2.txt"

copy_file(source_file, destination_file)
with open(source_file, 'r') as file:
    print(file.read())
with open(destination_file, 'r') as file:
    print(file.read())