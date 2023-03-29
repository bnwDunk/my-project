from Call import *

#=======================Class===========================

class Account:
  def __init__(self, id, password, status):
    self.id = id
    self.password = password
    self.status = status

class Person:
  def __init__(self, name, password, email, tel, address):
    self.name = name
    self.password = password
    self.email = email
    self.tel = tel
    self.address = address

class Admin(Person):
  def __init__(self, name, password, email, tel, address, role):
    Person.__init__(self, name, password, email, tel, address)
    self.role = Admin
    self.__admin_list = []

  def add_account_to_data(self, Person):
    self.__admin_list.append(Person)

  def modify_account_to_data(self, Person):
    #loop เพื่อหาข้อมูลของ account ที่จะแก้ไข้

    self.__admin_list(Person)

  def remove_account_form_data(self, Person):
    self.__admin_list.remove(Person)
    
class Customer(Person):
  def __init__(self, name, password, email, tel, address, role):
    Person.__init__(self, name, password, email, tel, address)
    self.role = Customer
    self.__customer_list = []

  def modify_account_customer_to_data(self, Person):
    self.__customer_list.remove(Person)



#=========================Instant================================

#======Account=======
AD_bnWDunk = Account("00001","bnwdunk","admin")
AD_Metear = Account("00002","metear","admin")
AD_maipk = Account("00003","maipk","admin")
AD_BigMom = Account("00004","bigmom","admin")

APThana = Account("00005","thana","customer")
monkey = Account("00006","deef","customer")
turtle = Account("00007","camew","customer")
brownie = Account("00008","brown","customer")

#======Admin=======
ad_dunk = Admin("dunk", "123456", "dunk@gmail.com", "0611111111", "bangkok", "admin")
ad_first = Admin("first", "123456", "first@gmail.com", "0622222222", "bangkok", "admin")
ad_mile = Admin("mile", "123456", "mile@gmail.com", "0633333333", "bangkok", "admin")
ad_mai = Admin("mai", "123456", "mai@gmail.com", "0644444444", "bangkok", "admin")

#======Customer=======
cus_thana = Customer("thana", "123456", "thana@gmail.com", "0655555555", "bangkok", "customer")
cus_deef = Customer("deef", "123456", "deef@gmail.com", "0666666666", "bangkok", "customer")
cus_mew = Customer("mew", "123456", "mew@gmail.com", "0677777777", "bangkok", "customer")
cus_brown = Customer("brown", "123456", "brown@gmail.com", "0688888888", "bangkok", "customer")