from data_create import name_data, surname_data, phone_data, address_data
from fs import read_data_first_csv, read_data_second_csv


def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
                    f"1 вариант: \n"
                    f"{name}\n{surname}\n{phone}\n{address}\n\n"
                    f"2 вариант: \n"
                    f"{name};{surname};{phone};{address}\n\n"
                    f"Выберите вариант: "))

    while var != 1 and var != 2:
        print("Неправильный ввод")
        var = int(input("Введите число: "))

    if var == 1:
        with open("data_first_variant.csv", 'a', encoding='utf-8') as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def search_data_first(my_list, my_name):
    result = -1
    for i in range(len(my_list)):
        if my_list[i].lower() == my_name.lower():
            result = i

    return result


def edit_data_first():
    new_phone_book = read_data_first_csv("data_first_variant.csv")
    i = - 1

    print("По какому параметру искать абонента?\n"
          "1. - По имени.\n"
          "2. - По фамилии.\n")
    choice = int(input("Введите номер меню: "))
    if choice == 1:
        while i == -1:
            name = input("Введите имя: ")
            i = search_data_first(new_phone_book, name)
            if i == -1:
                print("Абонент с таким именем не найден")
        new_phone_book[i] = name_data()
        new_phone_book[i + 1] = surname_data()
        new_phone_book[i + 2] = phone_data()
        new_phone_book[i + 3] = address_data()
    elif choice == 2:
        while i == -1:
            name = input("Введите фимилию: ")
            i = search_data_first(new_phone_book, name)
            if i == -1:
                print("Абонент с фамилией не найден")
        new_phone_book[i - 1] = name_data()
        new_phone_book[i] = surname_data()
        new_phone_book[i + 1] = phone_data()
        new_phone_book[i + 2] = address_data()

    return new_phone_book


def delete_data_first():
    new_phone_book = read_data_first_csv("data_first_variant.csv")
    i = - 1

    print("По какому параметру искать абонента?\n"
          "1. - По имени.\n"
          "2. - По фамилии.\n")
    choice = int(input("Введите номер меню: "))
    if choice == 1:
        while i == -1:
            name = input("Введите имя: ")
            i = search_data_first(new_phone_book, name)
            if i == -1:
                print("Абонент с таким именем не найден")
        new_phone_book.pop(i + 3)
        new_phone_book.pop(i + 2)
        new_phone_book.pop(i + 1)
        new_phone_book.pop(i)
    elif choice == 2:
        while i == -1:
            name = input("Введите фимилию: ")
            i = search_data_first(new_phone_book, name)
            if i == -1:
                print("Абонент с фамилией не найден")
        new_phone_book.pop(i + 2)
        new_phone_book.pop(i + 1)
        new_phone_book.pop(i)
        new_phone_book.pop(i - 1)

    return new_phone_book


def search_data_second(my_list, my_name, my_number):
    result = -1
    for i in range(0, len(my_list), 2):
        if my_list[i][my_number].lower() == my_name.lower():
            result = i

    return result


def edit_data_second():
    new_phone_book = read_data_second_csv("data_second_variant.csv")
    i = -1

    print("По какому параметру искать абонента?\n"
          "1. - По имени.\n"
          "2. - По фамилии.\n")
    choice = int(input("Введите номер меню: "))
    if choice == 1:
        number = 0
        while i == -1:
            name = input("Введите имя: ")
            i = search_data_second(new_phone_book, name, number)
            if i == -1:
                print("Абонент с таким именем не найден")
        new_phone_book[i][0] = name_data()
        new_phone_book[i][1] = surname_data()
        new_phone_book[i][2] = phone_data()
        new_phone_book[i][3] = address_data()
    elif choice == 2:
        number = 1
        while i == -1:
            name = input("Введите фимилию: ")
            i = search_data_second(new_phone_book, name, number)
            if i == -1:
                print("Абонент с таким именем не найден")
        new_phone_book[i][0] = name_data()
        new_phone_book[i][1] = surname_data()
        new_phone_book[i][2] = phone_data()
        new_phone_book[i][3] = address_data()

    return new_phone_book


def delete_data_second():
    new_phone_book = read_data_second_csv("data_second_variant.csv")
    i = -1

    print("По какому параметру искать абонента?\n"
          "1. - По имени.\n"
          "2. - По фамилии.\n")
    choice = int(input("Введите номер меню: "))
    if choice == 1:
        number = 0
        while i == -1:
            name = input("Введите имя: ")
            i = search_data_second(new_phone_book, name, number)
            if i == -1:
                print("Абонент с таким именем не найден")
        new_phone_book.pop(i)
    elif choice == 2:
        number = 1
        while i == -1:
            name = input("Введите фимилию: ")
            i = search_data_second(new_phone_book, name, number)
            if i == -1:
                print("Абонент с таким именем не найден")
        new_phone_book.pop(i)

    return new_phone_book


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append("".join(data_first[j:i + 1]))
                j = i
        print(data_first_list)
        print("".join(data_first_list))

    print("Вывожу данные из 2 файла: \n")
    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)
