import pyexcel
import package


"""
Записываем данные в файл excel
"""

for foto in package.connect_sqlite('/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'):
    if foto not in package.read_json_files():
        pyexcel.save_as(array=foto, dest_file_name="list_data.xlsx")