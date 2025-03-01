import os

def path(path):
    if os.path.exists(path):
        return os.path.dirname(path), os.path.basename(path)
    return "Path does not exist"

print(path("test.txt"))