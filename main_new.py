import package as pkg
import openpyxl as op

# NAME_FILE = 'list.xlsx'
FILENAME = 'gubaha_kizel.sqlite'
TABLENAME = 'gubaha_vydel'


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
        return pkg.connect_sqlite(pkg.searchFile(FILENAME), sql)


d = PhotoFilter('kv', 'vid')
a = PhotoFilter('kv', 'vid', 'tax_name')
s = SqliteFilter('kv', 'sknr', 'zk')


def filterFotoVydel():
    lst = []
    for foto in s.sqliteFilter():
        if foto not in d.fotoFilter():
            lst.append(foto)
    return lst


wb = op.Workbook()
ws = wb.active
sheet = wb['Sheet']
dict_name_row = {'A1': 'Квартал', 'B1': 'Выдел', 'C1': 'Имя таксатора'}
for key, val in dict_name_row.items():
    sheet[key] = val
    sheet[key].value

for row in filterFotoVydel():
    ws.append(row)
wb.save('files_ex/' + a[0][2] + '.xlsx')
