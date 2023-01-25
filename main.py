import package
import openpyxl as op
import os

NAME_FILE = 'list.xlsx'

lst_files = os.listdir(os.getcwd() + '/files_ex')
path_connect_sqlite = '/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'
lst = []
for foto in package.connect_sqlite(path_connect_sqlite):
    if foto not in package.read_json_files():
        lst.append(foto)

wb = op.Workbook()
ws = wb.active
# wb.create_sheet(title = 'Первый лист', index = 0)
sheet = wb['NotPhoto']
dict_name_row = {'A1': 'Квартал', 'B1': 'Выдел', 'C1': 'Имя таксатора'}
for key, val in dict_name_row.items():
    sheet[key] = val
    sheet[key].value

for row in lst:
    ws.append(row)
wb.save('files_ex/' + NAME_FILE)

"""
# Путь, где хранится файл базы данных
path_connect_sqlite = '/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'
lst = []
for foto in package.connect_sqlite(path_connect_sqlite):
    if foto not in package.read_json_files():
        lst.append(foto)
pyexcel.save_as(array=lst, dest_file_name="list_data.xlsx")
"""
"""
for vid in package.read_json_files():
    if vid not in package.connect_sqlite(path_connect_sqlite):
        print()
        print(f'Фото в непокрытой лесом площади')
        print('____________________________')
        print('|№ кв|№ выдела|Наличие фото|')
        print('____________________________')
        print('|{:4}| {:7}|{:>12}|'.format(vid[0], vid[1], 'Да'))

"""
