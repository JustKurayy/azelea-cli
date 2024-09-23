import os
import sys
import dload

n = len(sys.argv)
root = "C:\\Users\\Kuray\\Documents\\git\\aclt"

def init_prog():
    if os.path.exists(root):
        dload.save_unzip("https://github.com/JustKurayy/azelea-test/releases/download/V1.0.8/azelea-template.zip", root)

def main():
    match sys.argv[1]:
        case "project:init":
            init_prog()
            return
        case _:
            print("no argument passed!")
            return

main()
