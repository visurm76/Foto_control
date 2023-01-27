import package
import openpyxl as op

NAME_FILE = 'list.xlsx'
PATH_CON_SQLITE = '/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'

lst = []
lst_json = package.read_json_files()
"""
for foto in lst_json:
    if foto[:2] not in package.connect_sqlite(PATH_CON_SQLITE):
        lst.append(foto)
print(lst)

"""
for foto in package.connect_sqlite(PATH_CON_SQLITE):
    if foto not in lst_json:
        lst.append(foto)
print(lst)
wb = op.Workbook()
ws = wb.active
sheet = wb['Sheet']
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
