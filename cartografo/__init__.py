CONFIG_MAP_KIND = 'ConfigMap'
SECRET_KIND = 'Secret'

DEFAULT_OBJECT = CONFIG_MAP_KIND
DEFAULT_TARGET = 'new.yaml'

DEFAULT_CONFIG_MAP = {'kind': 'ConfigMap', 'apiVersion': 'v1', 'data': {}, 'metadata': {'name': 'type the name'}}
DEFAULT_SECRET = {'kind': 'Secret', 'apiVersion': 'v1', 'data': {}, 'metadata': {'name': 'type the name'}}