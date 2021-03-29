from pymysql import *

def main():
	conn = connect(
		host="localhost", 
		port=3306,
		user='root',
		password='mysql',
		database='test',
		charset='utf8'
	)
	cs1 = conn.cursor()

	count = cs1.execute('select * from student;')
	ret1 = cs1.fetchone()
	ret2 = cs1.fetchall()
	ret3 = cs1.fetchmany(5)
	print(ret1)
	print(ret2)

	cs1.close()
	conn.close()

if __name__ == "__main__":
	main()