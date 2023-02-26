import sqlite3

KATZEM = {3, 10, 8, 9}

<<<<<<< HEAD
def connect_sqlite(path_files):
    """
    Функция считывания данных из базы данных
    return: список списков (квартал, выдел)
    """
    conn = sqlite3.connect(path_files)
    cur = conn.cursor()
    # Делаем запрос к базе данных и выбираем нужные столбцы из таблицы"SELECT kv,sknr,zk FROM gubaha_vydel"
    cur.execute("SELECT kv,sknr,zk FROM gubaha_kizel")
    # Результат запроса в виде списка кортежей
    results = cur.fetchall()
    array = []
    for i in results:
        if i[2] == 3 or i[2] == 10 or i[2] == 8:
            array.append([int(i[0]), i[1]])
    conn.close()
    return array
=======
try:
    def connect_sqlite(path_files, sql):
        """
        Функция считывания данных из базы данных
        return: список списков (квартал, выдел)
        """
        conn = sqlite3.connect(path_files)
        cur = conn.cursor()
        # Делаем запрос к базе данных и выбираем нужные столбцы из таблицы"SELECT kv,sknr,zk FROM gubaha_vydel"
        cur.execute(sql)
        # Результат запроса в виде списка кортежей
        results = tuple(cur.fetchall())
        array = []
        for i in results:
            if i[2] in KATZEM:
                array.append([int(i[0]), i[1]])
        conn.close()
        return array
except:
    raise ConnectionError("No connect")
>>>>>>> ex
