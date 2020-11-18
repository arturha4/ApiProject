import pymysql

db=pymysql.connect(
    host='localhost',
    user='root',
    password='ghghrfth',
    database='testdb'
)

mycursor=db.cursor()

mycursor.execute("CREATE TABLE User (telegram_id VARCHAR(50), vk_id VARCHAR(30),time_in_vk SMALLINT)")
