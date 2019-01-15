import os
from cartografo import argument_parser
from cartografo.cartografo import generate

def init_shell():
    os.system('clear')
    print(' * K8S ConfigMap/Secrets Generator * ')

if __name__ == '__main__':
    init_shell()
    arguments = argument_parser.get_arguments()
    generate(arguments)