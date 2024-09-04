import os
from shutil import move

class DirectoryManager:
    def __init__(self):
        self.directory_structure = self.load_directory_structure()

    def load_directory_structure(self):
        return {
           'Programming Files': set(os.getenv('PROGRAMMING_FILES', '').split(',')),
            'Music': set(os.getenv('MUSIC_FILES', '').split(',')),
            'Videos': set(os.getenv('VIDEO_FILES', '').split(',')),
            'Pictures': set(os.getenv('PICTURE_FILES', '').split(',')),
            'Applications': set(os.getenv('APPLICATION_FILES', '').split(',')),
            'Compressed': set(os.getenv('COMPRESSED_FILES', '').split(',')),
            'Documents': set(os.getenv('DOCUMENT_FILES', '').split(',')),
            'Other': set([])
        }

    def create_folders(self):
        for dir_ in self.directory_structure:
            os.makedirs(dir_, exist_ok=True)
            print(f'{dir_:20} Created')

    def get_folder(self, ext):
        for folder, exts in self.directory_structure.items():
            if ext in exts:
                return folder
        return 'Other'


class FileOrganizer:
    def __init__(self, directory_manager: DirectoryManager):
        self.directory_manager = directory_manager

    def organize_files(self):
        for filename in os.listdir():
            # Skip the script file and hidden files
            if filename != __file__ and filename[0] != '.' and '.' in filename:
                ext = os.path.splitext(filename)[-1][1:]  # Get extension without dot
                folder = self.directory_manager.get_folder(ext)
                destination_path = os.path.join(folder, filename)

                if not os.path.isfile(destination_path):
                    move(filename, folder)
                    print(f'Moved {filename} to {folder}')


def main():
    directory_manager = DirectoryManager()
    directory_manager.create_folders()

    file_organizer = FileOrganizer(directory_manager)
    file_organizer.organize_files()


if __name__ == '__main__':
    main()
