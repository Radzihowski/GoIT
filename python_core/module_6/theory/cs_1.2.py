import sys

if len(sys.argv) != 2:
    print("Not enough parameters")
    quit()

NUM_LINES = 10

try:
    file = open(sys.argv[1], 'r', encoding="utf-8")
    lines = list()
    try:
        for line in file:
            lines.append(line)
            if len(lines) > NUM_LINES:
                lines.pop(0)
        for line in lines:
            print(line)

    except OSError:
        print(f"Error while reading {sys.argv[1]}")
    finally:
        file.close()
except OSError:
    print(f"Error with right for file {sys.argv[1]}")
except Exception as e:
    print(f"{e} with file {sys.argv[1]}")