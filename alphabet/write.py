import time


def write_file():
    a_list = [chr(i) for i in range(97, 123)]
    filename = 'project1.txt'
    index = 0
    while True:
        time.sleep(1)
        with open(filename, 'a') as file_object:
            write_text = a_list[index]
            file_object.write(write_text)
            # print(write_text)
            index += 1
            index = index % 26
