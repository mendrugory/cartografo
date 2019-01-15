import os

def get_files_from_folder(folder_path):
    if not os.path.isdir(folder_path):
        return None
    return [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

def read_file(file_path):
    if not os.path.isfile(file_path):
        return None
    with open(file_path, 'r') as f:
        return f.read()

