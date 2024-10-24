import os


def search_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None


directory_to_search = '/Users/muntashir'
file_to_find = 'myfile.txt'

result = search_file(directory_to_search, file_to_find)
if result:
    print(f"File found: {result}")
else:
    print("File not found")
