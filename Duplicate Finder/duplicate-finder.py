import os
import hashlib
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

class HashingStrategy:
    """Strategy pattern for different hashing algorithms."""
    def calculate_hash(self, filepath):
        raise NotImplementedError

class MD5Hashing(HashingStrategy):
    """Concrete strategy for MD5 hashing."""
    def calculate_hash(self, filepath):
        hasher = hashlib.md5()
        with open(filepath, 'rb') as f:
            buf = f.read()
            hasher.update(buf)
        return hasher.hexdigest()

class DuplicateFinder:
    """Facade for finding duplicate files."""
    def __init__(self, directory, min_size=0, hashing_strategy=None):
        self.directory = directory
        self.min_size = min_size
        self.hashing_strategy = hashing_strategy or MD5Hashing()

    def find_duplicates(self):
        hashes = {}
        duplicates = {}

        for dirpath, dirnames, filenames in os.walk(self.directory):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                if os.path.getsize(filepath) >= self.min_size:
                    file_hash = self.hashing_strategy.calculate_hash(filepath)
                    if file_hash in hashes:
                        duplicates.setdefault(file_hash, []).append(filepath)
                        if hashes[file_hash] not in duplicates[file_hash]:
                            duplicates[file_hash].append(hashes[file_hash])
                    else:
                        hashes[file_hash] = filepath

        return {k: v for k, v in duplicates.items() if len(v) > 1}

class ActionHandler:
    """Handles actions for duplicate files."""
    def __init__(self, duplicates):
        self.duplicates = duplicates

    def execute_action(self, action):
        if action == "d":
            for paths in self.duplicates.values():
                for path in paths[1:]:
                    os.remove(path)
                    print(f"Deleted {path}")
        elif action == "m":
            target_dir = os.getenv('TARGET_DIR')
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            for paths in self.duplicates.values():
                for path in paths[1:]:
                    target_path = os.path.join(target_dir, os.path.basename(path))
                    os.rename(path, target_path)
                    print(f"Moved {path} to {target_path}")
        else:
            print("No action taken.")

def main():
    directory = os.getenv('DIRECTORY')
    min_size = int(os.getenv('MIN_SIZE', default=0))
    finder = DuplicateFinder(directory, min_size)
    duplicates = finder.find_duplicates()

    if not duplicates:
        print("No duplicates found.")
        return

    print("\nDuplicates found:")
    for paths in duplicates.values():
        for path in paths:
            print(path)
        print("------")

    action = input("\nChoose an action: (D)elete, (M)ove, (N)o action: ").lower()
    handler = ActionHandler(duplicates)
    handler.execute_action(action)

if __name__ == "__main__":
    main()
