import package

# Путь, где хранится файл базы данных
path_connect_sqlite = '/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'
print('_____________________________________')
print('|№ кв|№ выдела|Наличие фото|Таксатор|')
print('-------------------------------------')
for foto in package.connect_sqlite(path_connect_sqlite):
    if foto not in package.read_json_files():
        print('|{:4}| {:7}| {:11}|'.format(foto[0], foto[1], 'Нет'))

for vid in package.read_json_files():
    if vid not in package.connect_sqlite(path_connect_sqlite):
        print(f'Фото в непокрытой лесом площади: кв.{vid[0]} выдел {vid[1]} ')
