import os

def generate_text_files():
    if not os.path.exists("alphabet_files"):
        os.makedirs("alphabet_files")
    for letter in range(ord('A'), ord('Z') + 1):
        filename = f"alphabet_files/{chr(letter)}.txt"
        with open(filename, 'w') as file:
            file.write(f"This is the file {chr(letter)}.txt\n")
    
    print("26 text files (A.txt to Z.txt) have been generated in the 'alphabet_files' directory.")

generate_text_files()