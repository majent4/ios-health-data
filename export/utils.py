from sys import exit as sys_exit

def print_exit(error):
    print(f'{error}\nExiting now')
    sys_exit(1)
