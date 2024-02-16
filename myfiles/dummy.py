from clickhouse_driver import Client
from helper_function import ClickHouseConnection
clickhouse_cred = {
    "host" : "localhost","port":9000,"user":"default","password":"Yuva","database":"db"
}
with ClickHouseConnection(**clickhouse_cred) as cursor:
    create = "SELECT * FROM user_data"
    cursor.execute(create)
    mydata = cursor.fetchall()
    row = cursor.rowcount
    print(row)
    print(mydata)

    