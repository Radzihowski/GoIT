import sys

if len(sys.argv) != 2:
    print("Not enough parameters")
    quit()

NUM_LINES = 10

for i in range(1, len(sys.argv)):
    file_name = sys.argv[i]
    print(file_name)
    try:
        with open (file_name,'r', encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()
                print(line)

    except Exception as e:
        print(f"{e} with file {file_name}")