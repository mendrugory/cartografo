import yaml
import os 

from cartografo import CONFIG_MAP_KIND, SECRET_KIND, DEFAULT_CONFIG_MAP, DEFAULT_SECRET

def read_yaml_file(yaml_file_path, object_type=CONFIG_MAP_KIND):
    if not os.path.isfile(yaml_file_path):
        return __default_values(object_type)
    with open(yaml_file_path, 'r') as f:
        data = yaml.load(f) 
        if not data or data['kind'] != object_type :
            data = __default_values(object_type)
        return data

def __default_values(object_type):
    return DEFAULT_SECRET if object_type == SECRET_KIND else DEFAULT_CONFIG_MAP

def write_yaml_file(yaml_file_path, obj):
    with open(yaml_file_path, 'w') as f:
        yaml.dump(obj, f, explicit_start=True, default_flow_style=False)    