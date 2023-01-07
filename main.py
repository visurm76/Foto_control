#from my_module import connect_base as cb, json_load as jl
import package


for foto in package.connect_sqlite():
    if foto not in package.read_json_files():
        print('------------------------------')
        print(f'Фото отсутвует в кв.{foto[0]} выдел {foto[1]}')
