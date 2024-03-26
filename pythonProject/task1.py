import re
def task1(source, output_name, treshold=7):
    print("reading data")
    file_handler = open(source, "r")
    data = file_handler.read()
    file_handler.close()


    print("preprocesing data")
    output_data =[]
    split_data = re.split(r'\s+|entr', data)
    #print(type(split_data))
    print("filtration data")
    for word in split_data:
        if len(word) >= treshold:
            output_data.append(f"{word}\n")

    print("write down data")
    file_handler = open(output_name, "w")
    file_handler.writelines(output_data)
    file_handler.close()
    print("Finished")


task1("source.txt", "output.txt", 4)

def task3(source_name, output_name):
    f_handler = open(source_name, "r")
    data = f_handler.readlines()
    f_handler.close()

    f_handler = open(output_name, "w")
    f_handler.close()

    if data[-1][-1] != "\n":
        data[-1] = data[-1] + "\n"

    f_handler = open(output_name, "a")
    for i in range(len(data) - 1, -1, -1):
        f_handler.write(data[i])
    f_handler.close()

task3("source3.txt", "output3.txt")

