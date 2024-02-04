import sys
import pathlib
from colorama import Fore, Style

try:
    dir_path = pathlib.Path(sys.argv[1])
    if dir_path.exists():
        if dir_path.is_dir():
            items = dir_path.iterdir()
            for item in items:
                print(Fore.GREEN + str(item))
        else:
            print(Fore.RED + 'can not list file, give dir')    
    else:
        print(Fore.RED + 'not found')
except IndexError as err:
    print(Fore.RED + f'{err}, plese write a path')

Style.RESET_ALL        