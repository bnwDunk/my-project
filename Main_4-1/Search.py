class Product:
    def __init__(self, name_product, picture, price, stock):
        self.name_product = name_product
        self.picture = picture
        self.price = price
        self.stock = stock

class TShirt(Product):
    def __init__(self, name_product, picture, size, chest, long, price, stock):
        Product.__init__(self, name_product, picture, price, stock)
        self.size = size
        self.chest = chest
        self.long = long

    def re_turn(self):
        return self.name_product


class Search:
    # def get(self):
    #     self.k = TShirt()
    

    def get_t(self):
        self.k = TShirt()


    def read_specific_product(self,name,i):
        self.k.self.name_product(i)
        # for j in i : 
        #     if name == i :
        #         print("True")
            



    def show_menu(self,menu):

        pass


# class AuthenticateUser(Customer):

#     def __init__(self, name, password, email, tel, address, role):
#         super().__init__(name, password, email, tel, address, role)
#         self.__search = ""



#     def get_search(self):
#         self.__search = Search()

#     def read_s_p(self,name):
#         self.__search.read_specific_product(name)

#     def show_m(self,menu):
#         self.__search.show_menu(menu)






m = [ TShirt("LALISA", "LALISA.png", "L", '48cm', "29.30cm", 690.00, 10),
 TShirt("HOMEBOY_AIR_M","HOMEBOY_AIR.png", "M", "43cm", "29cm", 550.00, 10),
 TShirt("HOMEBOY_AIR_L","HOMEBOY_AIR.png", "L", "47cm", "30cm", 550.00, 10),
TShirt("HOMEBOY_AIR_XL","HOMEBOY_AIR.png", "L", '51cm', '31cm', 550.00, 10),
 TShirt("HB_ANTI_V_M", "HB_ANTI_V.png", "M", '43cm', '29cm', 550.00, 10),
 TShirt("HB_ANTI_V_L", "HB_ANTI_V.png", "L", '47cm', '30cm', 550.00, 10),
]

s = Search()
for i in m:
    s.read_specific_product("LALISA", i)
    print(i)



# s = Search()
# 
# s.get_product()
