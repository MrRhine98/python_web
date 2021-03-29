from pymysql import *
import os
import re
import time

class User(object):
	def __init__(self):
		self.username = ""
		self.password = ""
		self.conn = connect(
			host="localhost", 
			port=3306,
			user='root',
			password='mysql',
			database='amazon',
			charset='utf8'
		)
		self.cs = self.conn.cursor()
		os.system("clear")


	def _execute(self, sql):
		self.cs.execute(sql)
		ret = self.cs.fetchall()
		return ret


	def _input(self):
		"""Validate the user identity"""
		self.username = input("Username:")
		self.password = input("password:")
		ret = re.match(r"^\w{1,20}$", self.username)
		print("------>input string", self.username)
		print("------>matched string",ret)	
		time.sleep(1)
		if ret == None:
			return True
		else:
			pass

		sql = f"""select name, password from users where name='{self.username}';"""
		print("----------->", sql)
		time.sleep(1)
		count = self.cs.execute(sql)
		print(count)
		if (self.username, self.password) == self.cs.fetchone():
			print("Login Successfully")
			time.sleep(1)
			return False
		else:
			print("Wrong username or password")
			time.sleep(1)
			return True


	def _sign_up(self):
		
		# Some notification
		print("Welcome to Amazon:")
		print("Please set your account")
		while True:
			# input username
			username = input("Username:")
			ret = re.match(r"^\w{1,20}$", username)
			if ret == None:
				os.system("clear")
				print("Your username has some invalid characters!")
				continue
			else:
				# validate username
				sql = f"""select id from users where name='{username}';"""
				count = self.cs.execute(sql)
				if count == 0:
					# input password
					pwd = input("Password:")
						
				else:
					os.system("clear")
					print("Sorry, the username you choose has been taken, please choose another:")
					continue
				print("username----->", username)
				print("password---->", pwd)
				
				# update users table
				sql = f"""insert into users values(0, "{username}", "{pwd}");"""
				self._execute(sql)
				self.conn.commit()
				print("Congrats! Now you can sign in and enjoy!")
				print("Press any button to exit")
				input()
				break


	def login(self):
		""" 
		User enters the username and password 
		Retrieve data from the table "users"
		Successfully login if matched, re-enter if not
		"""
		while True:
			os.system('clear')
			print("1. Sign in")
			print("2. Sign up")
			choice = input()
			if choice == "1":
				break
			else:
				self._sign_up()

		while self._input():
			os.system("clear")
			print("Wrong username or password! Please re-enter.")

	def _show_all_goods(self):
		sql = "select * from goods;"
		ret = self._execute(sql)
		title = "Show all"
		t1, t2, t3, t4, t5 = "id", "name", "category", "brand", "price"
		os.system("clear")
		print(f"{title:=^81}")
		print(f"|{t1:^15}|{t2:^15}|{t3:^15}|{t4:^15}|{t5:^15}|")
		
		for data in ret:
			item_id, name, cate_id, brand_id, price = data
			brand = self._get_data_by_id("goods_brands", brand_id, "name")
			cate = self._get_data_by_id("goods_cates", cate_id, "name")
			print("+---------------"*5 + "+")
			print(f"|{item_id:^15}|{name:^15}|{cate:^15}|{brand:^15}|{price:^15}|")

		print("+==============="*5 + "+")

			
	def _show_cate(self):
		sql = "select name from goods_cates;"
		ret = self._execute(sql)
		os.system("clear")
		title = "Categories"
		print(f"{title:=^17}")

		for data in ret:
			(name, ) = data
			print(f"|{name:^15}|")
			print("+---------------+")


	def _show_brand(self):
		sql = "select name from goods_brands;"
		ret = self._execute(sql)
		os.system("clear")
		title = "Brands"
		print(f"{title:=^17}")

		for data in ret:
			(name, ) = data
			print(f"|{name:^15}|")
			print("+---------------+")


	@staticmethod
	def _show_menu():
		print("1. Show all")
		print("2. Categories")
		print("3. Brands")
		print("4. Order now")


	def _order(self):
		while True:
			self._show_all_goods()
			item_id = input(" Please enter the id of the item you want to purchase:")
			quantity = input("How many items do you wish to purchase:")
			sql = f"select id from goods where id={item_id};"
			ret = self._get_data_by_id("goods", item_id, "id")
			if ret == None:
				print("Item doesn't exit")
				print("Do you wish to re-enter? [y/n]")
				re_do = input()
				if re_do == "y" or re_do == "Y":
					continue
				else:
					break
			else:
				print("--->ret", ret)
				print("--->item_id", item_id)
			# get datetime
				sql = "select now();"
				((datetime, ), ) = self._execute(sql)
				print("---->datetime", datetime)
			# get user id
				sql = f"""select id from users where name="{self.username}";"""
				((user_id,),) = self._execute(sql)
				print("----->user_id", user_id)

			# update orders
				sql = f"""insert into orders values(0, "{datetime}", {user_id});"""
				self._execute(sql)
				self.conn.commit()

			# get order_id
				sql = """select last_insert_id();"""
				((order_id,),) = self._execute(sql)
				print("----->order_id", order_id)

			# update order detail
				sql = f"""insert into orders_details values(0, {order_id}, {item_id}, {quantity});"""
				self._execute(sql)
				self.conn.commit()
				print("Thanks for ordering, your purchase will be delivered asap!")
				ret = input("Continue ordering or exit?[c/e]")
				print(ret)
				
				if ret == "c" or ret == "C":
					continue
				else:
					break



	def browse(self):
		"""
		Retrieve data from database and show them on the UI screen
		"""
		os.system("clear")
		self._show_menu()
		while True:
			choice = input("Enter the according number above:")

			if choice == "1":
				self._show_all_goods()
			elif choice == "2":
				self._show_cate()
			elif choice == "3":
				self._show_brand()
			elif choice == "4":
				self._order()
				os.system('clear')
			else:
				continue
			self._show_menu()

			


	def _get_data_by_id(self, table, id_, name):
		sql = f"select {name} from {table} where id={id_};"
		# print("----->sql", sql)
		count = self.cs.execute(sql)
		if count == 0:
			return None
		else:
			(ret, ) = self.cs.fetchone()
			# print (ret)
			return ret


def main():
	user = User()
	user.login()
	user.browse()

	#login()
	#browse()

if __name__ == "__main__":
	main()