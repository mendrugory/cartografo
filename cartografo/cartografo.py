import base64
import os

from cartografo import SECRET_KIND
from cartografo.files_folder_helper import get_files_from_folder, read_file
from cartografo.yaml_helper import read_yaml_file, write_yaml_file

def get_data_transformer(kind):
    if kind == SECRET_KIND:
        return lambda x: base64.encodebytes(x.encode()).decode().strip()
    else:
        return lambda x: x

def generate(arguments):
    data = read_yaml_file(arguments['target'])
    all_files = get_files_from_folder(arguments['source'])
    transformer = get_data_transformer(arguments['object'])
    for f in all_files:
        try:
            filename = os.path.basename(f)
            data['data'][filename] = transformer(read_file(f))
        except Exception as e:
            print("Exception with file {}: {}".format(f, e))
    write_yaml_file(arguments['target'], data)