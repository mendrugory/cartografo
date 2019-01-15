import argparse

from cartografo import DEFAULT_OBJECT, DEFAULT_TARGET


def __get_argparser():
    __parser.add_argument('--k8s-object', help='Output Kubernetes objet: secrets or configmap')
    __parser.add_argument('--target', help='Target file. If it exists, it will be modified')
    __parser.add_argument('files_folder', help='Folder where the actual files are.')

__parser = argparse.ArgumentParser()
__get_argparser()
__arguments = __parser.parse_args()

def get_arguments():
    return {
        "object": __arguments.k8s_object if __arguments.k8s_object else DEFAULT_OBJECT,
        "target": __arguments.target if __arguments.target else DEFAULT_TARGET,
        "source": __arguments.files_folder
    }