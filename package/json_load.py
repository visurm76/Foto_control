import json
import os


def read_json_files():
    """
    Функиция чтения json файлов и формирует список списков из номера квартала и номера выдела
    :return: список списков
    """
    link = os.listdir('json_files')  # Получает список имен файлов в директории
    path = os.getcwd()  # Текущая директория
    lst_data = []
    for i in sorted(link):
        # Открываем поочередно файлы и считываем данные
        with open(path + '/json_files/' + i, "r") as read_file:
            data = json.load(read_file)
            lst_data.append(data)

    return lst_data
