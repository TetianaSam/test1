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