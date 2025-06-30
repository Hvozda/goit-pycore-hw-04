
import sys
from pathlib import Path
from colorama import init, Fore, Style
# Intialize colorama to enable colored output
init(autoreset = True)


def print_directory_structure(path: Path, prefix: str = ""):
    try:
        items = sorted(path.iterdir(), key = lambda x: (x.is_file(), x.name.lower()))
    except FileNotFoundError:
            print(Fore.RED + prefix + "[Error] Directory not found: " + str(path))
            return
    for index, item in enumerate(items):
            connector = "|_" if index < len(items) - 1 else "'_"
            if item.is_dir():
                print(Fore.BLUE + prefix + connector + item.name + "/")
                print_directory_structure(item, prefix + ("| " if index < len(items) -1 else " "))
            else:
                print(Fore.GREEN + prefix + connector + item.name)
                def main():
                     if len(sys.argv) != 2:
                        print(Fore.RED + "Usage: python hw03.py <directory_path>")
                sys.exit(1)

                dir_path = Path(sys.argv[1])
                if not dir_path.exists():
                     print(Fore.RED + f"Directory does not exist: {dir_path}")
                     sys.exit(1)
                     if not dir_path.is_dir():
                          
                          print(Fore.YELLOW + f"Not a directory: {dir_path}\n")
                          print_directory_structure(dir_path)

                          if __name__ =="__main__":
                               main()
                              


<body>
<h2>exercises<h2>
<body>
                