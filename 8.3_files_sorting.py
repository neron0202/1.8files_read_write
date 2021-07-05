def merge_txt_files():
    files_list = ['1.txt', '2.txt', '3.txt']
    num_of_lines = {}

    for file in files_list:
        with open(file, 'r') as current_file:
            counter = 0
            for line in current_file:
                counter += 1
        num_of_lines[file] = counter
    num_of_lines = list(num_of_lines.items())
    num_of_lines.sort(key=lambda tup: tup[1])
    # print(num_of_lines)
    num_of_lines = dict(num_of_lines)
    # print(num_of_lines)

    for file in num_of_lines.items():
        print(file[0])
        print(file[1])
        with open(file[0], 'r') as current_file:
            print(current_file.read().strip())

merge_txt_files()
