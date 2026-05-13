"""
File Handling
"""
import os


def manage_file(file):
    if os.path.exists(os.path.join(os.curdir, file)):
        with open(file, mode='r') as f:
            for line in f:
                print(line, end='')
    else:
        print("File doesn't exist!")

def main() -> None:
    manage_file("content.txt")


if __name__ == "__main__":
    main()
