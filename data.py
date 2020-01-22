import sqlite3
from cryptography.fernet import Fernet
import hashlib
CONNECT = sqlite3.connect('login.db')
CURSOR = CONNECT.cursor()


def sign_up(username, email, password):  # регистрирует пользователя, при недостаточной длине, выбрасываются ошибки
    error_list = []  # создание списка, содержащего все ошибки
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
    if ('@' not in email) and ('.' not in email):
        error_list.append('wrongEmail')
    if len(error_list) == 0:  # если нет ошибок, тогда аккаунт добаляется в бд
        CURSOR.execute("INSERT INTO users VALUES(?, ?, ?)",
                       (username, email, hashlib.md5(bytes(password, encoding='utf8')).hexdigest()))
        CONNECT.commit()
        return False
    else:
        return error_list


def login(username, password):  # авторизирует пользователя, при вводе неправильных данных, выбрасываются ошибки
    if username == '' or password == '':
        return 'emptyString'
    res_user = CURSOR.execute("SELECT * FROM users WHERE (username = ?)", (username,)).fetchall()
    if res_user:
        if hashlib.md5(bytes(password, encoding='utf8')).hexdigest() == res_user[0][2]:
            return False
        else:
            return 'wrongPassword'
    else:
        return 'unknownLogin'


def encrypto(username, file_dir):  # шифрует файлы
    if file_dir == '':
        return 'emptyDir'
    file_name = file_dir[-int(file_dir[::-1].find('/')):len(file_dir):1]  # из директории файла выбирает имя файла
    res_names = CURSOR.execute('SELECT * FROM files WHERE filename = ? AND username = ?',
                               (file_name, username,)).fetchone()  # проверяет на наличие файлов с такими же названиями
    if res_names:
        return 'secondFilename'
    else:
        file_to_encrypto = open(file_dir, 'rb').read()
        directory = file_dir[:file_dir.find(file_name)]
        cipher_key = Fernet.generate_key()
        cipher = Fernet(cipher_key)
        encrypted_text = cipher.encrypt(file_to_encrypto)  # шифрует байт код из изначального файла
        f1 = open(directory + file_name + '.encrypted.txt', 'wb')
        f1.write(encrypted_text)  # записывает зашифрованный байт код в файл с расширением .encrypted.txt
        f1.close() 
        f2 = open(directory + file_name + '.encrypted.txt', 'rb').read()
        # добавление данных в бд
        CURSOR.execute("INSERT INTO files VALUES(?, ?, ?, ?, ?)", (username, file_name,
                                                                hashlib.md5(f2).hexdigest(), cipher_key, ''))
        CONNECT.commit() 
        f3 = open(directory + 'cipher_key ' + file_name + '.txt', 'wb')
        f3.write(cipher_key)  # записывается ключ для расшифровки
        f3.close()


def decrypto(file_dir, cipher_key):  # расшифровавает файлы
    if file_dir == '':
        return 'emptyDir'
    file_name_with_exstension = file_dir[-int(file_dir[::-1].find('/')):len(file_dir):1]  # берет имя фалйа
    file_name = file_name_with_exstension[:file_name_with_exstension.find('.en')]  # убирает специальное расширение
    file_exstension = file_name[file_name.find('.'):]
    directory = file_dir[:file_dir.find(file_name)]
    encrypted_text = open(file_dir, 'rb').read()
    decrypted_file = open(directory + file_name[:file_name.find('.')] + '_decrypted' + file_exstension, 'wb')
    hash_encrypt = hashlib.md5(encrypted_text).hexdigest()  # хэширует текст файла
    hash_from_bd = CURSOR.execute("SELECT hash FROM files WHERE (key = ?) "
                                  "AND (filename = ?)", (bytes(cipher_key, encoding='utf8'), file_name)).fetchone()[0]
    if hash_from_bd:  # возврат ошибок
        if hash_from_bd != hash_encrypt:
            return 'changedFile'
    else:
        return 'unknownCipherKey'
    cipher = Fernet(cipher_key)
    decrypted_file.write(cipher.decrypt(encrypted_text))


def take_from_bd(username):  # функия берет данные из бд, чтобы заполнить таблицу
    return CURSOR.execute("SELECT username, filename, hash FROM files WHERE username = ?", (username, )).fetchall()


def delete_file(username, filename):  # функция удаляет файл
    CURSOR.execute("DELETE FROM files WHERE username = ? AND filename = ?", (username, filename))
    CONNECT.commit()


def set_default_folder(file_dir, username):  # устанавливает директорию по умолчанию
    CURSOR.execute("UPDATE files SET default_folder = ? WHERE username = ?", (file_dir, username,))
    CONNECT.commit()


def check_old_pass(password, username):  # проверяет правильно ли введен старый пароль
    res = CURSOR.execute("SELECT password FROM users WHERE username = ?", (username,)).fetchall()[0]
    if res[0] == hashlib.md5(bytes(password, encoding='utf8')).hexdigest():
        return False
    return True


def set_new_pass(password, username):  # обновляет пароль в бд
    CURSOR.execute("UPDATE users SET password = ? WHERE username = ?",
                   (hashlib.md5(bytes(password, encoding='utf8')).hexdigest(), username,))
    CONNECT.commit()


def check_default_folder(username):  # проверяет установлена ли папка по умолчанию
    res = CURSOR.execute("SELECT default_folder FROM files WHERE username = ?", (username,)).fetchone()[0]
    return res



