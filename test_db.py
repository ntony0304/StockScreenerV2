from setting import Setting
from database import Database
setting = Setting()

db = Database(setting)

#result=(db.retrieve_accounts())
#db.create_stock_table()
result = db.retrieve_rows_from_stock_table()
print("test",result)
