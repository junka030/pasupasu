# import bcrypt
from cryptography.fernet import Fernet
import mysql.connector as SQLC
from tkinter import messagebox

KEY_FILE = "encryption_key.key"

"""
Initial connection
"""
# connect to database
def get_db_connection(password):

    try:
        conn = SQLC.connect(
            host = "localhost",
            user = "root",
            password = password,
            database = "pasuwarudo"
        )
    
        return conn
    
    except SQLC.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

        return None
    


"""
Encrypt & Decrypt
"""
def generate_and_save_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open(KEY_FILE, 'rb') as key_file:
        key = key_file.read()
    return key

def encrypt_password(key, password):
    f = Fernet(key)
    enc_pw = f.encrypt(password.encode())
    
    return enc_pw

def decrypt_password(key, enc_pw):
    f = Fernet(key)
    dec_pw = f.decrypt(enc_pw).decode()

    return dec_pw



"""
Database functions
"""
# add new password
def add_password(db_conn, key, appname, loginid, password):
    
    if appname and password and loginid:
        # cursor to execute SQL commands
        cursor = db_conn.cursor()
        
        # encrypt password
        enc_pw = encrypt_password(key, password)
        
        # insert to db
        statement = "INSERT INTO pasurecord (app_name,login_id,pw_enc) VALUES (%s,%s,%s)"
        cursor.execute(statement,(appname,loginid,enc_pw))
        db_conn.commit()
        cursor.close()

        messagebox.showinfo("Success", "Password added~ʕ๑•ω•ฅʔ✧")

    else:

        messagebox.showerror("Error", "Please complete all fields ʕ´• ᴥ •`ʔ!!")

# retrieve password
def get_password(db_conn, key, appname):

    if appname:
        cursor = db_conn.cursor()

        statement = "SELECT login_id,pw_enc FROM pasurecord WHERE app_name = %s"
        cursor.execute(statement,(appname,))
        result = cursor.fetchone()
        cursor.close()

        if result:
            login_id = result[0]
            enc_pw = result[1]
            if isinstance(enc_pw, str):
                enc_pw = enc_pw.encode()
            raw_pw = decrypt_password(key,enc_pw)

            return login_id,raw_pw
        else:
            messagebox.showinfo("Passwords","App does not existʕ ฅ ฅ ʔ!")
            return None, None
        
    else:
        
        messagebox.showerror("Error","Please enter app nameʕ ฅ ฅ ʔ!")
        return None, None

# list all applications registered
def list_apps(db_conn):
    
    cursor = db_conn.cursor()
    statement = "SELECT app_name FROM pasurecord"
    cursor.execute(statement)
    result = cursor.fetchall()
    cursor.close()

    app_names = [row[0] for row in result]

    return app_names

# remove password from db
def delete_password(db_conn,appname):

    if appname:
        cursor = db_conn.cursor()

        statement = "DELETE FROM pasurecord WHERE app_name = %s"
        cursor.execute(statement,(appname,))
        db_conn.commit()
        cursor.close()

        messagebox.showinfo("Success",f"App {appname} deleted ʕ ˵• ₒ •˵ ʔ")

    else:
        
        messagebox.showerror("Error","Please enter app nameʕ ฅ ฅ ʔ!")



"""
RUN ONCE ONLY TO GENERATE AND SAVE KEY
"""
# generate_and_save_key()
