'''sqlite database'''
import sqlite3
import traceback
import os
import logging
class Database():
    def __init__(self, setting):
        self.db_setting = setting # copy all the attributes inside setting and assign to db_setting
        self.connection = sqlite3.connect(self.db_setting.database_file_location)
        self.create_account_table()
        logging.basicConfig(
            filename='database.log',
            level=logging.DEBUG,
            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )

    def create_account_table(self):
        cur = self.connection.cursor()
        try:
            cur.execute('''CREATE TABLE account (
                 username TEXT PRIMARY KEY, password TEXT,	email TEXT,	account_type TEXT,	contact_no INT)''')  # create table
            # Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
            self.connection.commit()  # apply the changes to the database
            self.connection.close()
        except:  # if the table exist just skip
            pass
    def create_order_table(self):
        cur = self.connection.cursor()
        try:
            cur.execute('''CREATE TABLE orders (
                      username TEXT PRIMARY KEY, password TEXT,	email TEXT,	account_type TEXT,	contact_no INT)''')  # create table
            # Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
            self.connection.commit()  # apply the changes to the database
            self.connection.close()
        except:  # if the table exist just skip
            pass
    def create_stock_table(self):
        cur = self.connection.cursor()
        try:#QTRLY EPS DATE	TICKER	STOCK CODE	NAME	ST TREND %	LT TREND %	PRICE	VOLUME	TURNOVER	MAIN INDUSTRY
            cur.execute('''CREATE TABLE stocks (
                            date DATE, ticker INT PRIMARY KEY, stock_code TEXT UNIQUE, stock_name TEXT, st_trend_per FLOAT, lt_trend_per FLOAT, 
                            price FLOAT, volume INT, turnover INT, industry TEXT)''')  # create table
            # Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
            self.connection.commit()  # apply the changes to the database
            self.connection.close()
        except:  # if the table exist just skip
            pass

    def insert_account_data(self, username=None, password=None,email=None, account_type = "user", contact_num = None):
        conn = self.database_connection()
        cur = conn.cursor()
        query = '''INSERT INTO account VALUES ( ? , ?, ?, ?, ? ) '''

        if (username != None and password!=None and email!=None):
            try:
                cur.execute(query, (username, password, email, account_type, contact_num))
                conn.commit()
            except:
                err = traceback.format_exc()
                print(err)

        cur.close()
        conn.close()

    def retrieve_account_by_user_name(self, username):
        conn = self.database_connection()
        cur = conn.cursor()
        query = '''SELECT * FROM account WHERE username =?'''
        account_found = None
        logging.info("account account_found={}".format(account_found))
        try:
            cur.execute(query, (username,))
            logging.info("executed successfully")
            account_found = cur.fetchone()
            logging.info("account account_found={}".format(account_found))
        except:
            err = traceback.format_exc()
            logging.error("error execute sql = {}".format(traceback.format_exc()))
        cur.close()
        conn.close()
        logging.info("account info={}".format(account_found))
        return account_found

    def retrieve_accounts(self):
        conn = self.database_connection()
        cur = conn.cursor()
        query = '''SELECT * FROM account'''
        all_account = []
        try:
            cur.execute(query)
            rows= cur.fetchall()
            for row in rows :
                all_account.append(row)
        except:
            err = traceback.format_exc()
            print()
        cur.close()
        conn.close()
        return all_account

    def edit_account_type(self, username=None, account_type= None):
        ''' This function is used by the admin or moderator only to change the type of user's account '''
        conn = self.database_connection()
        cur = conn.cursor()
        query = '''UPDATE account SET account_type = ? WHERE username = ? '''
        if (account_type != None and username != None):
            try:
                cur.execute(query, (account_type, username))
                conn.commit()
            except:
                err = traceback.format_exc()
                print()
        cur.close()
        conn.close()

#         UPDATE
#         table
#         SET
#         column_1 = new_value_1,
#         column_2 = new_value_2
#
#     WHERE
#     search_condition
#
#
# ORDER
# column_or_expression


    def create_stock_table(self):
        #Date	Open	High	Low	Close	Adjusted_close	Volume
        cur = self.connection .cursor()
        try:
            cur.execute('''CREATE TABLE stocks (
            code TEXT, name TEXT,	st_trend_per REAL,	lt_trend_per REAL,	price REAL,	volume INT, turn_over INT, 
            industry TEXT,  qtrly_eps_date DATE )''')#create table
            #Stock*',               'Open',     'High',     'Low',     'Last*',      Vol*
            self.connection.commit() #apply the changes to the database
            self.connection.close()
        except: #if the table exist just skip
            pass
    def database_connection(self):
        self.connection = sqlite3.connect(self.db_setting.database_file_location)
        return  self.connection

    def insert_stock_data(self, code, name,  st_trend_per,
                               lt_trend_per,price,
                                  volume,turn_over,
                               industry,qtrly_eps_date):
        conn = self.database_connection()
        cur = conn.cursor()
        query = '''INSERT INTO stocks VALUES ( ? , ?, ?, ?, ?, ?, ? ,?, ?) '''

        try:
            cur.execute(query,(code, name,
                           st_trend_per,
                           lt_trend_per,price,
                              volume,turn_over,
                           industry,qtrly_eps_date))
            conn.commit()
            logging.debug("inserting data %s"%code)
        except:
            err = traceback.format_exc()
            print("error insert stock to database " ,err)
        logging.info("inserting data completed")
        cur.close()
        conn.close()

    def retrieve_row(self, stock_name):
        query ='''SELECT * FROM stocks WHERE  stock = ?'''
        conn = self.database_connection()
        cur = conn.cursor()
        try:
            cur.execute(query, (stock_name,))
        except:
            pass
        row_data = cur.fetchone()
        conn.close()
        return row_data


    def retrieve_some_rows(self, amount):
        """return row in dictionary"""
        query = '''SELECT * FROM stocks WHERE  stock = "MCD"'''
        conn = self.database_connection()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        try:
            cur.execute(query)
        except:
            pass
        row_data = []
        for row in cur.fetchmany(amount):
            row_data.append((dict(row)))
        conn.close()
        return row_data

    def retrieve_rows_from_stock_table(self):
        """return row in list"""
        query = '''SELECT * FROM stocks'''
        conn = self.database_connection()

        cur = conn.cursor()
        row = None
        try:
            cur.execute(query)
            row = cur.fetchall()
        except:
            print(traceback.format_exc())
        return row
#
# from setting import Setting
# setting = Setting()
# db = Database(setting)
# #db.create_account_table()
# #db.create_stock_table()
#
# #insert account data for testing
# #db.insert_account_data("acc1", "acc1Pass", "acc1@gmail.com","user", 1234556)
# #db.edit_account_type("acc1","premium")
# all_account = db.retrieve_accounts()
# all_stock=db.retrieve_rows_from_stock_table()
# print(all_stock)