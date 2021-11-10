# import csv
# import traceback
#
# import sqlite3
# #connect to database
# con = None
# try: #attempt to create database if not exist
#     con = sqlite3.connect(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\new_database.db")
#     query = ''' CREATE TABLE stock_data (stock TEXT PRIMARY KEY, open REAL, high REAL, low REAL, last REAL, vol REAL)'''
#     c = con.cursor() #cursor to execute query
#     c.execute(query)
#     con.commit()
# except:
#     pass
#     #print(traceback.format_exc())
# # finally:#
# #     if con is not None:
# #         con.close() #close connection to database
#
#         #print all information in database
# # con = sqlite3.connect(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\new_database.db")
# # c= con.cursor()
# # c.execute('''select * from stock_data ''')
# # data = c.fetchall()
# # con.close()
# # print(f"current data in database {data}")
#
# #open file method 1
# with open(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\210930_A&M.csv", 'r') as file:
#     csv_reader = csv.reader(file) #reader from csv library will read all the data and place them to the variable csv_reader (row by row)
#     next(csv_reader) # go to the next row
#     #make a connection to database
#     con = sqlite3.connect(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\new_database.db")
#     c= con.cursor()
#     for row in csv_reader:
#         #insert query
#         query = '''INSERT INTO stock_data VALUES(?, ?, ?, ?, ?, ?) '''
#         try:
#             c.execute(query, (row[0], row[1], row[2],row[3],row[4],row[5] ))
#         except:
#             pass
#     con.commit()# save the changes
#
# #retrieve data from database
# con = sqlite3.connect(r"C:\Users\quang nguyen\PycharmProjects\StockScreener\new_database.db")
# c= con.cursor()
# c.execute('''select * from stock_data ''')
# data = c.fetchall()
# con.close()
# #
# # for item in data:
# #     if item[0] =='AEMULUS':
# #         print(item)
#             #column index  0         1       2     3      4      5
# #row index
# #0                         ACO	    0.29	0.3	  0.28	0.29	43548
# #1                       Aemulus    1.06    1.08  10.4
# #2
# #3
#
#
#
# #(([@[Close 0.30]]-[@Open])/ ([@High]-[@Low]) )*100
# # def calculate60body(close, open, high, low):
# #     try:
# #         result =   ((close - open) / (high - low) )* 100
# #         if result > 25:
# #             print(f"60bodyvalue  {row[0]} : {result}")
# #     except:#ignore case of zero division
# #         pass
# #
# #
# # for row in data : #row[0] #n = 0,1,2,3,4,5,6,7
# #     #(stock TEXT PRIMARY KEY, open REAL, high REAL, low REAL, last REAL, vol REAL)''
# #     close = row[4]
# #     open = row[1]
# #     high = row[2]
# #     low = row[3]
# #     calculate60body(close,open,high,low)
#
# #method 2 using return
# def calculate60body(close, open, high, low):
#     result = 0
#     try:
#         result =   ((close - open) / (high - low) )* 100
#     except:#ignore case of zero division
#         pass
#     return result
#
#
# for row in data : #row[0] #n = 0,1,2,3,4,5,6,7
#     #(stock TEXT PRIMARY KEY, open REAL, high REAL, low REAL, last REAL, vol REAL)''
#     close = row[4]
#     open = row[1]
#     high = row[2]
#     low = row[3]
#     result = calculate60body(close,open,high,low)
#     if result >25:
#         print(f"60bodyvalue  {row[0]} : {result}")
#

#method 1 import 1 method/function
from test import print_a
print_a()

from test import example_class
ex = example_class()

#
import test #import everything
test.print_a()
#1. to use print_c
test.example_class().print_c()
#2. to use print_c
ex = test.example_class() #create object example_class
ex.print_c()





