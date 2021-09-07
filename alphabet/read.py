import time


def read_file():
    while True:
        time.sleep(1)
        with open('project1.txt') as file_object:
            lines = file_object.readlines()
            line = lines[-1]
            print(line[-1])
