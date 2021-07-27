import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               id INTEGER PRIMARY KEY NOT NULL,
               data1 TEXT,
               data2 TEXT);
                """)


def SET():
    data1 = input('Введите первое значение\n')
    data2 = input('Введите второе значение\n')
    try:
        if data1 == '':
            data1 = 'NULL'
        if data2 == '':
            data2 = 'NULL'
        data_tuple = (data1, data2)
        cursor.execute("INSERT INTO users (data1,data2) VALUES(?,?);", data_tuple)
        conn.commit()
        print('Данные добавлены')
    except:
        print('Ошибка добавления')  #


def GET():
    text = input('Введите первое значение\n')
    cursor.execute("SELECT id FROM users ")
    if len(cursor.fetchall()) == 0:
        print('NULL')
    else:
        for i in cursor.execute("SELECT * FROM users ORDER BY id DESC;"):
            if i[1] == text:
                print(i[2])
                break
            else:
                print('NULL')
            break


def UNSET():
    try:
        last_id = ''
        for i in cursor.execute("SELECT * FROM users ORDER BY id DESC;"):
            last_id = i[0]
            break
        cursor.execute(f"DELETE FROM users WHERE id = {last_id}")
        conn.commit()
        print('Откат на одну позицию назад')
    except:
        print('Записей больше нет!')


def COUNTS():
    text = input('Введите первое значение\n')
    count = 0
    cur = cursor.execute("SELECT * FROM users;")
    for i in cur:
        if i[2] == text:
            count += 1
    return print(f'Данные "{text}" повторяются {count} раз!')


def FIND():
    text = input('Введите переменную\n')
    cur = cursor.execute("SELECT data2 FROM users WHERE data1 = ?;", text)
    for i in cur:
        print(f'{text} = {i[0]}', end=', ')
    print()

while True:
    task = input('''SET - сохраняет аргумент в базе данных.
GET - возвращает, ранее сохраненную переменную. Если такой переменной не было сохранено, возвращает NULL
UNSET - удаляет, ранее установленную переменную. Если значение не было установлено, не делает ничего.
COUNTS - показывает сколько раз данные значение встречается в базе данных.
FIND - выводит найденные установленные переменные для данного значения.
END - закрывает приложение.
Введите первую букву\n''').upper()
    if task == 'S':
        SET()
        continue
    elif task == 'G':
        GET()
        continue
    elif task == 'U':
        UNSET()
        continue
    elif task == 'C':
        COUNTS()
        continue
    elif task == 'F':
        FIND()
        continue
    elif task not in 'SGUCFE':
        print('Неверный запрос')
        continue
    elif task == 'E':
        print('Приложение закрыто')
        break
