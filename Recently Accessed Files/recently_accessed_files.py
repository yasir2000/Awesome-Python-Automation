import os
import datetime
from abc import ABC, abstractmethod
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class FileAccess(ABC):
    @abstractmethod
    def get_access_time(self, file_path):
        pass

class OSFileAccess(FileAccess):
    def get_access_time(self, file_path):
        return os.path.getatime(file_path)

class FileVisitor:
    def visit(self, file_path):
        access_time = self.file_access.get_access_time(file_path)
        self.on_file_accessed(file_path, access_time)

    @abstractmethod
    def on_file_accessed(self, file_path, access_time):
        pass

class RecentFileCollector(FileVisitor):
    def __init__(self, time_threshold=None):
        self.time_threshold = time_threshold
        self.recently_accessed_files = []

    def on_file_accessed(self, file_path, access_time):
        if self.time_threshold is None or access_time >= self.time_threshold:
            self.recently_accessed_files.append(file_path)

    def get_files(self):
        return sorted(self.recently_accessed_files, key=lambda file: os.path.getatime(file), reverse=True)

class FileSystemTraverser:
    def __init__(self, directory_path, file_access, collector):
        self.directory_path = directory_path
        self.file_access = file_access
        self.collector = collector

    def traverse(self):
        for root, dirs, files in os.walk(self.directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                self.collector.visit(file_path)

class FileAccessFacade:
    def __init__(self, directory_path, time_threshold=None):
        self.file_access = OSFileAccess()
        self.collector = RecentFileCollector(time_threshold)
        self.traverser = FileSystemTraverser(directory_path, self.file_access, self.collector)

    def get_recently_accessed_files(self):
        self.traverser.traverse()
        return self.collector.get_files()

def main():
    directory_path = input("Enter the directory path to search: ")
    time_threshold = os.getenv('TIME_THRESHOLD')

    facade = FileAccessFacade(directory_path, time_threshold)
    recently_accessed_files = facade.get_recently_accessed_files()

    print("List of recently accessed files:")
    for file_path in recently_accessed_files:
        print(f"{file_path}")

if __name__ == "__main__":
    main()
