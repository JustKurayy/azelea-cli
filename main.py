import os
import sys
import dload

n = len(sys.argv)
root = os.getcwd()

def init_prog():
    if os.path.exists(root):
        dload.save_unzip("https://github.com/JustKurayy/azelea-test/releases/download/V1.0.2/azelea-template.zip", root)

def main():
    match sys.argv[1]:
        case "project:init":
            init_prog()
            return
        case "cache:clear":
            cwd = os.path.dirname(os.path.realpath(__file__))
            filename = cwd + "\\azelea-template.zip"
            if os.path.exists(filename):
                os.remove(filename)
                return
            else:
                print("Cache is already empty")
                return
        case _:
            print("no argument passed!")
            return

main()
