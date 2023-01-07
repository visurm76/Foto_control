gimport sqlite3


def connect_sqlite():
    """
    Функция считывания данных из базы данных
    return: список списков (квартал, выдел)
    """
    conn = sqlite3.connect('gubaha.sqlite')
    cur = conn.cursor()
    # Делаем запрос к базе данных и выбираем нужные столбцы из таблицы"SELECT kv,sknr,zk FROM gubaha_vydel"
    cur.execute("SELECT kv,sknr,zk FROM gubaha_vydel")
    # Результат запроса в виде списка кортежей
    results = cur.fetchall()
    array = []
    for i in results:
        if i[2] == 3 or i[2] == 10 or i[2] == 8:
            array.append([int(i[0]), i[1]])
    conn.close()
    return array
