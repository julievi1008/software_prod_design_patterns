'''
Proxy provides a substitute or placeholder for another object.

Examples:
    - Caching --- database (spl) proxy for normal users/ admin users
    - Monitoring or logging operations
    - Control access (admin can do any operation, normal user only operations related to their user etc...)
'''

import hashlib
from pathlib import Path
from abc import ABC, abstractmethod

def calculate_md5(file_path): # md5 totally differ from markdown =)))))
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

# The base interface for reading files
class FileReaderInterface(ABC):
    @abstractmethod
    def read_file(self, file_path):
        pass

# This implements the FileReaderInterface with the real Python way to read a file
class RealFileReader(FileReaderInterface):
    def read_file(self, file_path):
        print("Reading content of file " + file_path)
        with open(file_path, "r") as file:
            content = file.read()
        return content

# This proxy takes in any FileReaderInterface and creates cache for content
# that we already know of
class FileReaderProxy(FileReaderInterface):
    def __init__(self):
        self.cache = {}
        self.real_reader = RealFileReader()

    def read_file(self, file_path):
        file_md5 = calculate_md5(file_path)
        if file_md5 in self.cache:
            print(f"Returning cached content for {file_path}")
            return self.cache[file_md5]

        print(f"Reading and caching content for {file_path}")
        content = self.real_reader.read_file(file_path)
        self.cache[file_md5] = content
        return content

###
# Usage
###
file_path = "example.txt"

file_reader_with_cache : FileReaderInterface = FileReaderProxy()
file_reader_without_cache : FileReaderInterface = RealFileReader()

print("\n#### WITHOUT CACHE:")
# Without cache
###for i in range(3):
###    content = file_reader_without_cache.read_file(file_path)
###    print(content)
print(file_reader_without_cache.read_file(file_path))

print("\n#### WITH CACHE:")
# With cache
###for i in range(3):
###    content = file_reader_with_cache.read_file(file_path)
###    print(content)

print(file_reader_with_cache.read_file(file_path))
print(file_reader_with_cache.read_file(file_path))
