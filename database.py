import sqlite3
CONNECT = sqlite3.connect('login.db')
CURSOR = CONNECT.cursor()


def sign_up(username, email, password):
    error_list = []
    res_find = CURSOR.execute(f"SELECT * FROM users WHERE (username = ?) OR (email = ?)",
                              (username, email)).fetchone()
    if len(username) < 3:
        error_list.append('lenError_user')
    if len(email) < 4:
        error_list.append('lenError_email')
    if len(password) < 4:
        error_list.append('lenError_pass')
    if res_find:
        error_list.append('secondAccount')
    if len(error_list) == 0:
        CURSOR.execute("INSERT INTO users VALUES(?, ?, ?)", (username, email, password))
        CONNECT.commit()
        return False
    else:
        return error_list


def login(username, password):
    res_user = CURSOR.execute("SELECT * FROM users WHERE (username = ?)", (username,)).fetchall()
    if res_user:
        if password == res_user[0][2]:
            return False
        else:
            return 'wrongPassword'
    else:
        return 'unknownLogin'


login('abc', 'abc')

