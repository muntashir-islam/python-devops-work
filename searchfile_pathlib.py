from pathlib import Path


def search_file(directory, filename):
    path = Path(directory)
    for file in path.rglob(filename):
        return file
    return None


directory_to_search = '/path/to/search'
file_to_find = 'myfile.txt'

result = search_file(directory_to_search, file_to_find)
if result:
    print(f"File found: {result}")
else:
    print("File not found")
