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

    def fotoFilter(self):
        mass_filter = []
        for i in pkg.read_json_files():
            kv_vid = {k: v for k, v in i.items() if k in self.row}
            mass_filter.append(list(kv_vid.values()))
        return mass_filter


class SqliteFilter(object):

    def __init__(self, *args):
        self.row = list(args)

    def sqliteFilter(self):
        row_name = ','.join(self.row)
        sql = 'SELECT' + ' ' + row_name + ' ' + 'FROM' + ' ' + TABLENAME
        return pkg.connect_sqlite(searchFile(FILENAME), sql)


d = PhotoFilter('kv', 'vid')
print(d.fotoFilter())
s = SqliteFilter('kv', 'sknr', 'zk')
print(s.sqliteFilter())
