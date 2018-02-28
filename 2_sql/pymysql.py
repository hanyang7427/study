import pymysql
# 创建一个connection
db = pymysql.connect('localhost','root','123456','testDB')
# 使用cursor()方法创建一个游标对象cursor
cursor = db.cursor()

# sql语句绑定到变量
SQL = 'select * from customers;'

# 使用execute() 方法执行sql查询
# 返回sql执行结果的行数
# 或cursor.execute(select * from customers;)
cursor.execute(SQL)

# 使用fetchone()方法获得单条数据,一行一行返回，返回到最后返回None
data = cursor.fetchone()

# 注意，返回的data是保存在元祖tuple中
print("the first row in the table is",data)

# 写sql语句，创建一个新的表格，叫customers_backup,包括 id,name,age,address,salary,gender
SQL = 'create table customers_backup(id int,name varchar(20),age int,address varchar(20),salary int,gender char(5));'
cursor.execute(SQL)

# 写sql语句，像customers_bkp表中插入行，完成对customers表内容的复制
SQL = 'insert into customers_backup select * FROM customers'
cursor.execute(SQL)     # 返回的结果为N rows in set (0.00 sec)中的N

# fectchall()接收上一条cursor.execute(SQL)全部的返回结果，即表中所有行，返回结果存在元组中(只能取一次)，再取返回空元组
# fetchone()和fetchall()只有在上一条cursor.execute(SQL)返回了结果才会绑定内容(只能取一次)
data2 = cursor.fetchall()
print('all data is',data2)

# rowcount是一个只读属性，返回执行上一条cursor.execute()放法影响的行数(Query OK, 1 row affected (0.03 sec)),或返回结果的行数(5 rows in set (0.00 sec),可以重复访问
print(cursor.rowcount)

# commit
db.commit()

# 关闭数据库连接
db.close()

# 练习：
# 把customers表中工资大于所有顾客的平均工资的人的姓名和工资还有地址打印出来
# pymysql实现
# 创建connection
db = pymysql.connect('localhost','root','123456','testDB')
# 创建游标
cursor = db.cursor()
# 写SQL
SQL = 'select name,salary,address from customers where salary > (select avg(salary) from customers)'
# execute方法执行SQL
cursor.execute(SQL)
data = cursor.fetchall()
for i in data:
    print(i[0] + '的工资是' + str(float(i[1])) + '地址是' + i[2])
# 关闭connection
db.close()

