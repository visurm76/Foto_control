import package as pkg
import openpyxl as op

NAME_FILE = 'list.xlsx'


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
    PATH_CON_SQLITE = '/home/viktor/Общедоступные/Foto_control/gubaha.sqlite'

    def __init__(self, *args):
        self.row = list(args)

    def sqliteFilter(self):
        row_name = ','.join(self.row)
        sql = 'SELECT' + ' ' + row_name + ' ' + 'FROM gubaha_vydel'
        print(sql)
        return pkg.connect_sqlite(SqliteFilter.PATH_CON_SQLITE, sql)


d = PhotoFilter('kv', 'vid')
print(d.fotoFilter())
s = SqliteFilter('kv', 'sknr', 'zk')
print(s.sqliteFilter())
