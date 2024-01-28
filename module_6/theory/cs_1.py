import sys

if len(sys.argv) != 2:
    print("Not enough parameters")
    quit()

try:
    file = open(sys.argv[1], 'r', encoding="utf-8")
    try:
        line = file.readline()
        counter = 0
        while counter < 10 and line != "":
            line = line.rstrip()
            print(line)
            counter += 1
            line = file.readline()
    except OSError:
        print(f"Error while reading {sys.argv[1]}")
    finally:
        file.close()
except OSError:
    print(f"Error with right for file {sys.argv[1]}")