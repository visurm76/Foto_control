import package

# Путь, где хранится файл базы данных
path_connect_sqlite = '/home/viktor/Общедоступные/Foto_control/package/gubaha.sqlite'

for foto in package.connect_sqlite(path_connect_sqlite):
    if foto not in package.read_json_files():
        print('------------------------------')
        print(f'Нет фото: кв.{foto[0]} выдел {foto[1]}')

for vid in package.read_json_files():
    if vid not in package.connect_sqlite(path_connect_sqlite):
        print(f'Фото в непокрытой лесом площади: кв.{vid[0]} выдел {vid[1]} ')
