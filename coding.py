import connect_base as cb
import json_load as jl


for foto in cb.connect_sqlite():
    if foto not in jl.read_json_files():
        print('------------------------------')
        print(f'Фото отсутвует в кв.{foto[0]} выдел {foto[1]}')
