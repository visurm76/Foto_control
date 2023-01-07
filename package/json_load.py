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
            # Фильтруем словарь с номером квартала и выдела
            mass_kv_vid = {k: v for k, v in data.items() if k == 'kv' or k == 'vid'}
            lst_data.append(list(mass_kv_vid.values()))

    return lst_data



