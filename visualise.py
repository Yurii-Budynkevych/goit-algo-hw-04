import sys
import pathlib
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset color after each print

def list_directory(path: pathlib.Path, level=0):
    indent = "  " * level  # Indent based on level of depth

    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/")
                list_directory(item, level + 1)  # Recursive call
            else:
                print(f"{indent}{Fore.GREEN}{item.name}")
    except PermissionError:
        print(f"{indent}{Fore.RED}[Permission Denied] {item.name}")

def main():
    try:
        dir_path = pathlib.Path(sys.argv[1])
        if not dir_path.exists():
            print(Fore.RED + "Path not found")
        elif not dir_path.is_dir():
            print(Fore.RED + "Given path is not a directory")
        else:
            list_directory(dir_path)
    except IndexError:
        print(Fore.RED + "No path provided. Please provide a directory path as an argument.")

if __name__ == '__main__':
    main()