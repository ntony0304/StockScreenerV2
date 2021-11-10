'''just to demonstrate using a module without creating class '''
import sqlite3
from setting2 import Setting2
setting = Setting2()
connection = sqlite3.connect(setting.database_file_location)


def create_account_table():
    cur = self.connection.cursor()
    try:
        cur.execute('''CREATE TABLE account (
             username TEXT PRIMARY KEY, password TEXT,	email TEXT,	account_type TEXT,	contact_no INT)''')  # create table
        # Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
        self.connection.commit()  # apply the changes to the database
        self.connection.close()
    except:  # if the table exist just skip
        pass


def create_order_table():
    cur = connection.cursor()
    try:
        cur.execute('''CREATE TABLE orders (
                  username TEXT PRIMARY KEY, password TEXT,	email TEXT,	account_type TEXT,	contact_no INT)''')  # create table
        # Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
        connection.commit()  # apply the changes to the database
        connection.close()
    except:  # if the table exist just skip
        pass


def create_stock_table(self):
    cur = connection.cursor()
    try:  # QTRLY EPS DATE	TICKER	STOCK CODE	NAME	ST TREND %	LT TREND %	PRICE	VOLUME	TURNOVER	MAIN INDUSTRY
        cur.execute('''CREATE TABLE stocks (
                        date DATE, ticker INT PRIMARY KEY, stock_code TEXT UNIQUE, stock_name TEXT, st_trend_per FLOAT, lt_trend_per FLOAT, 
                        price FLOAT, volume INT, turnover INT, industry TEXT)''')  # create table
        # Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
        connection.commit()  # apply the changes to the database
        connection.close()
    except:  # if the table exist just skip
        pass


def insert_account_data(username=None, password=None, email=None, account_type="user", contact_num=None):
    conn = database_connection()
    cur = conn.cursor()
    query = '''INSERT INTO account VALUES ( ? , ?, ?, ?, ? ) '''

    if (username != None and password != None and email != None):
        try:
            cur.execute(query, (username, password, email, account_type, contact_num))
            conn.commit()
        except:
            err = traceback.format_exc()
            print(err)

    cur.close()
    conn.close()


def retrieve_accounts(self):
    conn = self.database_connection()
    cur = conn.cursor()
    query = '''SELECT * FROM account'''
    all_account = []
    try:
        cur.execute(query)
        rows = cur.fetchall()
        print(rows)
        for row in rows:
            all_account.append(row)
    except:
        err = traceback.format_exc()
        print()
    cur.close()
    conn.close()
    return all_account
