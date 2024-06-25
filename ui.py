from logger import (input_data,
                    edit_data_first,
                    delete_data_first,
                    edit_data_second,
                    delete_data_second,
                    print_data)
from fs import write_data_first_csv, write_data_second_csv

def interface():
    print("Добрый день! Добро пожаловать в программу для работы с телефонным справочником.\n"
          "1. - Запись данных.\n"
          "2. - Редактировать 1 файл.\n"
          "3. - Удалить абонента из 1 файла.\n"
          "4. - Редактировать 2 файл.\n"
          "5. - Удалить абонента из 2 файла.\n"
          "6. - Вывод данных.\n")
    command = int(input("Введите число: "))

    while (command != 1
           and command != 2
           and command != 3
           and command != 4
           and command != 5
           and command != 6):
        print("Неправильный ввод")
        command = int(input("Введите число: "))

    if command == 1:
        input_data()
    elif command == 2:
        phone_book = edit_data_first()
        write_data_first_csv(phone_book, "data_first_variant.csv")
        print("Данные изменены.")
    elif command == 3:
        phone_book = delete_data_first()
        write_data_first_csv(phone_book, "data_first_variant.csv")
        print("Абонент удален.")
    elif command == 4:
        phone_book = edit_data_second()
        write_data_second_csv(phone_book, "data_second_variant.csv")
        print("Данные изменены.")
    elif command == 5:
        phone_book = delete_data_second()
        write_data_second_csv(phone_book, "data_second_variant.csv")
        print("Абонент удален.")
    elif command == 6:
        print_data()
