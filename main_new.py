import package as pkg
import openpyxl as op
import os

NAME_FILE = 'list.xlsx'
FILENAME = 'gubaha_kizel.sqlite'
TABLENAME = 'gubaha_vydel'


def searchFile(filename):
    """
    Функиция определения пути расположения файла по его названию
    """

    for root, dirnames, filenames in os.walk('/home/viktor/'):
        for file in filenames:
            if file == filename:
                return os.path.join(root, file)


class PhotoFilter(object):
    """
    Формирует список списков из файлов json, в зависимости от заданных ключей
    """

    def __init__(self, *args):
        self.row = list(args)

    def __repr__(self):
        return str(self.row)

    def fotoFilter(self):
        mass_filter = []
        for i in pkg.read_json_files():
            kv_vid = {k: v for k, v in i.items() if k in self.row}
            mass_filter.append(list(kv_vid.values()))
        return mass_filter

    def __getitem__(self, item):
        if 0 <= item < len(self.fotoFilter()):
            return self.fotoFilter()[item]
        else:
            raise IndexError("Индекс за границами массива")


class SqliteFilter(object):

    def __init__(self, *args):
        self.row = list(args)

    def sqliteFilter(self):
        row_name = ','.join(self.row)
        sql = 'SELECT' + ' ' + row_name + ' ' + 'FROM' + ' ' + TABLENAME
        return pkg.connect_sqlite(searchFile(FILENAME), sql)


d = PhotoFilter('kv', 'vid')
a = PhotoFilter('kv', 'vid', 'tax_name')
s = SqliteFilter('kv', 'sknr', 'zk')

lst = []

for foto in s.sqliteFilter():
    if foto not in d.fotoFilter():
        lst.append(foto)
print(lst)
print(a[0][2])