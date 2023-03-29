from Call import *

class AuthenticateAdmin(Admin):
    def __init__(self, name, password, email, tel, address, role):
        super().__init__(name, password, email, tel, address, role)
        self.__manger_admin_account = Person()
        self.__product = AddProduct()
        self.__modify_product = ModifyProduct()

    # =========== Product

    def add_tshirt(self, name_product, picture, size, chest, long, price, stock):
        self.__product.TShirt(name_product, picture, size, chest, long, price, stock)
        
    def add_Hood(self, name_product, picture, size, chest, long, price, stock):
        self.__product.Hood(name_product, picture, size, chest, long, price, stock)
        
    def add_Pants(self, name_product, picture, size, waist_first_stretch, waist_back_stetch, hip, legs, price, stock):
        self.__product.Pants(name_product, picture, size, waist_first_stretch, waist_back_stetch, hip, legs, price, stock)
        
    def add_Jeans(self, name_product, picture, size, waist, length, thigh_tip, hips, price, stock):
        self.__product.Jeans(name_product, picture, size, waist, length, thigh_tip, hips, price, stock)
        
    def add_Hats(self, name_product, picture, size, round_cap, price, stock):
        self.__product.Hats(name_product, picture, size, round_cap, price, stock)
        
    def Bags(self, name_product, picture, size, width, height, thickness, line_length, price, stock):
        self.__product.Bags(name_product, picture, size, width, height, thickness, line_length, price, stock)
        
    def mod_product(self,name_product):
        self.__modify_product.modify_product(name_product)
        
    def mod_product(self,name_product):
        self.__modify_product.modify_product(name_product)

    # =========== Account

    def add_data_account(self, Person):
        self.__manger_admin_account.add_account_to_data(Person)

    def modify_account(self, Person):
        self.__manger_admin_account.modify_account_to_data(Person)
    
    def remove_account(self, Person):
        self.__manger_admin_account.remove_account_form_data(Person)

    
class AuthenticateUser(Customer):
    def __init__(self, name, password, email, tel, address, role):
        super().__init__(name, password, email, tel, address, role)
        self.__manger_customer_account = Person()
        self.__shopping_cart = ""

    # =========== Cart

    def get_shopping_cart(self):
        self.__shopping_cart = Cart()

    def add_to_cart(self,item):
        # print("dfadfasdf : "+str(item.name_product))
        self.__shopping_cart.add_to_cart_data(item)

    def remove_from_cart(self,item):
        self.__shopping_cart.remove_from_cart_data(item)

    def clear_cart(self,item):
        self.__shopping_cart.clear_cart_data(item)
    
    # =========== Payment

    def make_payment(self):
        self.__my_payment = Payment()

    def confirm_payment(self,ckeck_confirm_payment,select_payment_method):
        self.__confirm_order = ckeck_confirm_payment
        self.__select_payment_method = select_payment_method
        self.__my_payment.confirm_payment(self.__confirm_order, self.__select_payment_method)

    def cancle_payment(self):
        self.__my_payment.cancle_payment

    # =========== Account

    def modify_account(self, Person):
        self.__manger_customer_account.modify_account_customer_to_data(Person)