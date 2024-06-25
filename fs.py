def read_data_first_csv(my_filename):
    new_phone_book = list()
    with open(my_filename, 'r', encoding='utf-8') as f_in:
        for line in f_in:
            new_phone_book.append(line[:-1])
    return new_phone_book


def write_data_first_csv(my_list, my_filename):
    with open(my_filename, 'w', encoding='utf-8') as f_out:
        for i in my_list:
            f_out.write(f"{i}\n")


def read_data_second_csv(my_filename):
    new_phone_book = list()
    with open(my_filename, 'r', encoding='utf-8') as f:
        for line in f:
            record = line[:-1].split(sep=';')
            new_phone_book.append(record)

    return new_phone_book


def write_data_second_csv(my_list, my_filename):
    with open(my_filename, 'w', encoding='utf-8') as f_out:
        for line in my_list:
            record = ';'.join(line)
            f_out.write(f"{record}\n")
