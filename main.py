import package

# Путь, где хранится файл базы данных
path_connect_sqlite = '/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'
print('Перечень выделов, в которых нет фото')
print('___________________________')
print('|№ кв|№ выдела|Наличие фото|')
print('____________________________')
for foto in package.connect_sqlite(path_connect_sqlite):
    if foto not in package.read_json_files():
        print('|{:4}| {:7}| {:>11}|'.format(foto[0], foto[1], 'Нет'))
print('____________________________')
print()
print(f'Фото в непокрытой лесом площади')
print('____________________________')
print('|№ кв|№ выдела|Наличие фото|')
print('____________________________')
for vid in package.read_json_files():

    if vid not in package.connect_sqlite(path_connect_sqlite):
        print('|{:4}| {:7}|{:>12}|'.format(vid[0], vid[1], 'Да'))
print('____________________________')
