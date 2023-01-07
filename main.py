import package

for foto in package.connect_sqlite():
    if foto not in package.read_json_files():
        print('------------------------------')
        print(f'Фото отсутвует в кв.{foto[0]} выдел {foto[1]}')

for i in package.read_json_files():
    if i not in package.connect_sqlite():
        print(f'Фото в непокрытой лесом площади кв.{i[0]} выдел {i[1]} ')
