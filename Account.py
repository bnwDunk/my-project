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
  def __init__(self, name, password, email, tel, address):
    Person.__init__(self, name, password, email, tel, address)

class Customer(Person):
  def __init__(self, name, password, email, tel, address):
    Person.__init__(self, name, password, email, tel, address)
    
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

#======Person=======
dunk = Person("dunk", "123456", "dunk@gmail.com", "0611111111", "bangkok")
first = Person("first", "123456", "first@gmail.com", "0622222222", "bangkok")
mile = Person("mile", "123456", "mile@gmail.com", "0633333333", "bangkok")
mai = Person("mai", "123456", "mai@gmail.com", "0644444444", "bangkok")
thana = Person("thana", "123456", "thana@gmail.com", "0655555555", "bangkok")
deef = Person("deef", "123456", "deef@gmail.com", "0666666666", "bangkok")
mew = Person("mew", "123456", "mew@gmail.com", "0677777777", "bangkok")
brown = Person("brown", "123456", "brown@gmail.com", "0688888888", "bangkok")

#======Admin=======
ad_dunk = Admin("dunk", "123456", "dunk@gmail.com", "0611111111", "bangkok")
ad_first = Admin("first", "123456", "first@gmail.com", "0622222222", "bangkok")
ad_mile = Admin("mile", "123456", "mile@gmail.com", "0633333333", "bangkok")
ad_mai = Admin("mai", "123456", "mai@gmail.com", "0644444444", "bangkok")

#======Customer=======
cus_thana = Customer("thana", "123456", "thana@gmail.com", "0655555555", "bangkok")
cus_deef = Customer("deef", "123456", "deef@gmail.com", "0666666666", "bangkok")
cus_mew = Customer("mew", "123456", "mew@gmail.com", "0677777777", "bangkok")
cus_brown = Customer("brown", "123456", "brown@gmail.com", "0688888888", "bangkok")