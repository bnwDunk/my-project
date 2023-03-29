from Call import *

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

class Hood(Product):
    def __init__(self, name_product, picture, size, chest, long, price, stock):
        Product.__init__(self, name_product, picture, price, stock)
        self.size = size
        self.chest = chest
        self.long = long

class Pants(Product):
    def __init__(self, name_product, picture, size, waist_first_stretch, waist_back_stetch, hip, legs, price, stock):
        Product.__init__(self, name_product, picture, price, stock)
        self.size = size
        self.waist_first_stretch = waist_first_stretch
        self.waist_back_stetch = waist_back_stetch
        self.hip = hip
        self.legs = legs

class Jeans(Product):
    def __init__(self, name_product, picture, size, waist, length, thigh_tip, hips, price, stock):
        Product.__init__(self, name_product, picture, price, stock)
        self.size = size
        self.waist = waist
        self.length = length
        self.thigh_tip = thigh_tip
        self.hips = hips

class Hats(Product):
    def __init__(self, name_product, picture, size, round_cap, price, stock):
        Product.__init__(self, name_product, picture, price, stock)
        self.size = size
        self.round_cap = round_cap

class Bags(Product):
    def __init__(self, name_product, picture, size, width, height, thickness, line_length, price, stock):
        Product.__init__(self, name_product, picture, price, stock)
        self.size = size
        self.width = width
        self.height = height
        self.thickness = thickness
        self.line_length = line_length





# TShirt ########################

LALISA_L = TShirt("LALISA", "LALISA.png", "L", '48cm', "29.30cm", 690.00, 10)
HOMEBOY_AIR_M = TShirt("HOMEBOY_AIR_M","HOMEBOY_AIR.png", "M", "43cm", "29cm", 550.00, 10)
HOMEBOY_AIR_L = TShirt("HOMEBOY_AIR_L","HOMEBOY_AIR.png", "L", "47cm", "30cm", 550.00, 10)
HOMEBOY_AIR_XL = TShirt("HOMEBOY_AIR_XL","HOMEBOY_AIR.png", "L", '51cm', '31cm', 550.00, 10)
HB_ANTI_V_M = TShirt("HB_ANTI_V_M", "HB_ANTI_V.png", "M", '43cm', '29cm', 550.00, 10)
HB_ANTI_V_L = TShirt("HB_ANTI_V_L", "HB_ANTI_V.png", "L", '47cm', '30cm', 550.00, 10)
HB_ANTI_V_XL = TShirt("HB_ANTI_V_M", "HB_ANTI_V.png", "XL", '51cm', '31cm', 550.00, 10)
HB_FUTURE_L = TShirt("HB_FUTURE_L", "HB_FUTURE.png", "L", '47cm', '30cm', 550.00, 10)
HB_LABRADOR_L = TShirt("HB_LABRADOR_L", "HB_LABRADOR.png", "L", '47cm', '30cm', 550.00, 10)
HB_LABRADOR_XL = TShirt("HB_LABRADOR_XL", "HB_LABRADOR.png", "XL", '51cm', '31cm', 550.00, 10)
HB_BLACKSWORD_M = TShirt("HB_BLACKSWORD_M", "HB_BLACKSWORD.png", "M", '43cm', '29cm', 550.00, 10)
HB_BLACKSWORD_L = TShirt("HB_BLACKSWORD_L", "HB_BLACKSWORD.png", "L", '47cm', '30cm', 550.00, 10)
HB_BLACKSWORD_XL = TShirt("HB_BLACKSWORD_XL", "HB_BLACKSWORD.png", "XL", '51cm', '31cm', 550.00, 10)
HB_XXTENATIONS_F = TShirt("HB_XXTENATIONS_F", "HB_XXTENATIONS.png", "FREESIZE", '48cm', '29cm', 690.00, 10)
HB_BIGFOOT_M = TShirt("HB_BIGFOOT_M", "HB_BIGFOOT.png", "M", '43cm', '29cm', 550.00, 10)
HB_BIGFOOT_L = TShirt("HB_BIGFOOT_L", "HB_BIGFOOT.png", "L", '47cm', '30cm', 550.00, 10)
HB_BIGFOOT_XL = TShirt("HB_BIGFOOT_XL", "HB_BIGFOOT.png", "M", '51cm', '31cm', 550.00, 10)
HB_HYPE_F = TShirt("HB_HYPE_F", "HB_HYPE.png", "FREESIZE", '48cm', '29cm', 690.00, 10)
HB_SCOTTISH_L = TShirt("HB_SCOTTISH_L", "HB_SCOTTISH.png", "L", '47cm', '30cm', 550.00, 10)
HB_SCOTTISH_XL = TShirt("HB_SCOTTISH_XL", "HB_SCOTTISH.png", "XL", '51cm', '31cm', 550.00, 10)
HB_PUG_M = TShirt("HB_PUG_M", "HB_PUG.png", "M", '43cm', '29cm', 550.00, 10)
HB_PUG_L = TShirt("HB_PUG_L", "HB_PUG.png", "L", '47cm', '30cm', 550.00, 10)
HB_PUG_XL = TShirt("HB_PUG_XL", "HB_PUG.png", "XL", '51cm', '31cm', 550.00, 10)
HB_BULLDOG_M = TShirt("HB_BULLDOG_M", "HB_BULLDOG.png", "M", '43cm', '29cm', 550.00, 10)
HB_BULLDOG_XL = TShirt("HB_BULLDOG_XL", "HB_BULLDOG.png", "XL", '51cm', '31cm', 550.00, 10)





# Hoodie ###################

HB_CANDY_GRAY_M = Hood("HB_CANDY_GRAY_M", "HB_CANDY_GRAY.png", "M", "43cm", "28cm", 790.00, 10)
HB_CANDY_GRAY_L = Hood("HB_CANDY_GRAY_M", "HB_CANDY_GRAY.png", "L", "52cm", "29cm", 790.00, 10)
HB_CANDY_PINK_M = Hood("HB_CANDY_PINK_M", "HB_CANDY_PINK.png", "M", "50cm", "28cm", 790.00, 10)
HB_CANDY_PINK_L = Hood("HB_CANDY_PINK_L", "HB_CANDY_PINK.png", "L", "52cm", "29cm", 790.00, 10)
HB_HOODIES_BLACK_M = Hood("HB_HOODIES_BLACK_M", "HB_HOODIES_BLACK.png", "M", "54cm", "22.5cm", 890.00, 10)
HB_HOODIES_BLACK_L = Hood("HB_HOODIES_BLACK_L", "HB_HOODIES_BLACK.png", "L", "56cm", "23.5cm", 890.00, 10)
LITTLE_HELP_XL = Hood("LITTLE_HELP_XL", "LITTLE_HELP.png", "XL", "46cm", "26cm", 790.00, 10)
LITTLE_HELP_XXL = Hood("LITTLE_HELP_XXL", "LITTLE_HELP.png", "XXL", "48cm", "25cm", 790.00, 10)
HB_Broken_L = Hood("HB_Broken_L", "HB_Broken.png", "L", "46cm", "28cm", 890.00, 10)
HB_Broken_XL = Hood("HB_Broken_XL", "HB_Broken.png", "XL", "50cm", "29cm", 890.00, 10)


# Pants #######################


SHADOW_PANTS_L = Pants("SHADOW_PANTS_L", "SHADOW_PANTS.png", "L", "28cm", "30cm", "48cm", "13cm", 590.00, 90)
SHADOW_PANTS_XL = Pants("SHADOW_PANTS_XL", "SHADOW_PANTS.png", "XL", "32cm", "34cm","48cm", "14cm", 590.00, 10)
SHADOW_PANTS_XXL = Pants("SHADOW_PANTS_XXL", "SHADOW_PANTS.png", "XXL", "50cm", "29cm","48cm", "14cm", 590.00, 10)
HB_MOLLY_PANTS_BLACK_M = Pants("HB_MOLLY_PANTS_M", "HB_MOLLY_PANTS_BLACK.png", "M", "28cm", "32cm", "48cm", "16cm", 590.00, 10)
HB_MOLLY_PANTS_BLACK_L = Pants("HB_MOLLY_PANTS_L", "HB_MOLLY_PANTS_BLACK.png", "L", "30cm", "34cm", "48cm", "17cm", 590.00, 10)
HB_MOLLY_PANTS_BROWN_M = Pants("HB_MOLLY_PANTS_BROWN_M", "HB_MOLLY_PANTS_BROWN.png", "M", "28cm", "32cm", "48cm", "16cm", 590.00, 10)
HB_MOLLY_PANTS_BROWN_L = Pants("HB_MOLLY_PANTS_BROWN_L", "HB_MOLLY_PANTS_BROWN.png", "M", "30cm", "34cm", "48cm", "17cm", 590.00, 10)
CORONA_PANTS_BLACK_M = Pants("CORONA_PANTS_BLACK_M", "CORONA_PANTS_BLACK.png", "M", "28cm", "30cm", "43cm", "12cm", 590.00, 10)
CORONA_PANTS_BLACK_L = Pants("CORONA_PANTS_BLACK_L", "CORONA_PANTS_BLACK.png", "L", "32cm", "34cm", "44cm", "12cm", 590.00, 10)
CORONA_PANTS_BLACK_XL = Pants("CORONA_PANTS_BLACK_XL", "CORONA_PANTS_BLACK.png", "XL", "34cm", "36cm", "46cm", "13cm", 590.00, 10)
HB_BLISSONIC_BLACK_M = Pants("HB_BLISSONIC_BLACK_M", "HB_BLISSONIC_BLACK.png", "M", "30cm", "32cm", "46cm", "14cm", 590.00, 10)
HB_BLISSONIC_BLACK_L = Pants("HB_BLISSONIC_BLACK_L", "HB_BLISSONIC_BLACK.png", "L", "32cm", "34cm", "44cm", "12cm", 590.00, 10)

# Jeans ####################

ALLMATCH_M = Jeans("ALLMATCH", "ALLMATCH_M.png", "M", "30cm", "39.5cm", "8.5cm", "41cm", 590.00, 10)
ALLMATCH_L = Jeans("ALLMATCH", "ALLMATCH_L.png", "L", "32cm", "40cm", "8.5cm", "42cm", 590.00, 10)
ALLMATCH_XL = Jeans("ALLMATCH", "ALLMATCH_XL.png", "XL", "34cm", "40cm", "8.5cm", "44cm", 590.00, 10)
LEVI_JEAN_M = Jeans("LEVI.JEAN", "LEVI.JEAN_M.png", "M", "30cm", "40cm", "10cm", "42cm", 690.00, 10)
LEVI_JEAN_L = Jeans("LEVI.JEAN", "LEVI.JEAN_L.png", "L", "32cm", "42cm", "11cm", "42cm", 690.00, 10)
LEVI_JEAN_XL = Jeans("LEVI.JEAN", "LEVI.JEAN_XL.png", "XL", "34cm", "44cm", "11cm", "42.5cm", 690.00, 10)
LKTM_M = Jeans("LKTM", "LKTM_M.png", "M", "30cm", "39cm", "12.5cm", "38cm", 590.00, 10)
LKTM_L = Jeans("LKTM", "LKTM_L.png", "L", "32cm", "41cm", "13cm", "38.5cm", 590.00, 10)
LKTM_XL = Jeans("LKTM", "LKTM_XL.png", "XL", "33cm", "42cm", "13.5cm", "38.5cm", 590.00, 10)
LKTM_2XL = Jeans("LKTM", "LKTM_2XL.png", "2XL", "34cm", "43cm", "13.5cm", "39cm", 590.00, 10)


# # ========== Bags

NEWKID_BAG_M_GRAY = Bags("NEWKID_BAG_C_GRAY", "NEWKID_BAG_C_GRAY.png", "M", "12cm", "15cm", "15cm", "51cm", 450.00, 10)
NEWKID_BAG_M_BLUE = Bags("NEWKID_BAG_C_BLUE", "NEWKID_BAG_C_BLUE.png", "M", "12cm", "15cm", "15cm", "51cm", 450.00, 10)
NEWKID_BAG_M_WHITE = Bags("NEWKID_BAG_C_WHITE ", "NEWKID_BAG_C_WHITE.png", "M", "12cm", "15cm", "15cm", "51cm", 450.00, 10)
NEWKID_BAG_L_GRAY = Bags("NEWKID_BAG_C_GRAY ", "NEWKID_BAG_C_GRAY.png", "L", "16cm", "20cm", "20cm", "69cm", 650.00, 5)
NEWKID_BAG_L_BLUE = Bags("NEWKID_BAG_C_BLUE", "NEWKID_BAG_C_BLUE.png", "L", "16cm", "20cm", "20cm", "69cm", 650.00, 5)
NEWKID_BAG_L_WHITE = Bags("NEWKID_BAG_C_WHITE ", "NEWKID_BAG_C_WHITE.png", "L", "16cm", "20cm", "20cm", "69cm", 650.00, 5)

# ========== Hats

BROKEN_CAP = Hats("BROKEN_CAP", "BROKEN_CAP.png", "M", "25in", 450.00, 10)
ALONE_CAP = Hats("ALONE_CAP", "ALONE_CAP.png", "M", "25in", 450.00, 10)
MADEBY_CAP = Hats("MADEBY_CAP", "MADEBY_CAP.png", "M", "25in", 450.00, 10)

#=================== Method ======================

class AddProduct:
    def __init__(self):
        self.__add_product = []
        
    def TShirt(self, name_product, picture, size, chest, long, price, stock):
        self.__name_product = name_product
        self.__picture = picture
        self.__size = size
        self.__chest = chest
        self.__long = long
        self.__price = price
        self.__stock = stock
        self.__add_product.append(self.__name_product, self.__picture, self.__size, self.__chest, self.__long, self.__price, self.__stock)
        
    def Hood(self, name_product, picture, size, chest, long, price, stock):
        self.__name_product = name_product
        self.__picture = picture
        self.__size = size
        self.__chest = chest
        self.__long = long
        self.__price = price
        self.__stock = stock
        self.__add_product.append(self.__name_product, self.__picture, self.__size, self.__chest, self.__long, self.__price, self.__stock)
        
    def Pants(self, name_product, picture, size, waist_first_stretch, waist_back_stetch, hip, legs, price, stock):
        self.__name_product = name_product
        self.__picture = picture
        self.__size = size
        self.__waist_first_stretch = waist_first_stretch
        self.__waist_back_stetch = waist_back_stetch
        self.__hip = hip
        self.__legs = legs
        self.__price = price
        self.__stock = stock
        self.__add_product.append(self.__name_product, self.__picture, self.__size, self.__waist_first_stretch, self.__waist_back_stetch, self.__hip, self.__legs, self.__price, self.__stock)

    def Jeans(self, name_product, picture, size, waist, length, thigh_tip, hips, price, stock):
        self.__name_product = name_product
        self.__picture = picture
        self.__size = size
        self.__waist = waist
        self.__length = length
        self.__thigh_tipp = thigh_tip
        self.__hips = hips
        self.__price = price
        self.__stock = stock
        self.__add_product.append(self.__name_product, self.__picture, self.__size, self.__waist, self.__length, self.__thigh_tipp, self.__hips, self.__price, self.__stock)

    def Hats(self, name_product, picture, size, round_cap, price, stock):
        self.__name_product = name_product
        self.__picture = picture
        self.__size = size
        self.__round_cap = round_cap
        self.__price = price
        self.__stock = stock
        self.__add_product.append(name_product, picture, size, self.__round_cap, price, stock)

    def Bags(self, name_product, picture, size, width, height, thickness, line_length, price, stock):
        self.__name_product = name_product
        self.__picture = picture
        self.__size = size
        self.__width = width
        self.__height = height
        self.__thickness = thickness
        self.__line_length = line_length
        self.__price = price
        self.__stock = stock
        self.__add_product.append(self.__name_product, self.__picture, self.__size, self.__width, self.__height, self.__thickness, self.__line_length, self.__price, self.__stock)
        
    def AddToDataBase(self):
        pass
    
class ModifyProduct:
    def __init__(self):
        #ทุกรายการสินค้าจะมีปุ่ม Modify ของมันเอง โดยจะนำ PK ไปตรวจสอบว่านี่เป็น PK ของ Row ไหน แล้วจะเอาข้อมูลทั้งหมดของ Row นั้นมาแสดงเพื่อให้แก้ไขได้
        pass
    
    def modify_product(self,name_product):
        pass
    
    def delete_product(self):
        #เราจะสามารถลบสินค้าที่เราเลือกได้ แล้วหลังจากนั้นสินค้าก็จะโดนลบออกไปจาก Database และหายไปจาก Menu ด้วย
        pass
    
class addmenu:
    def __init__(self, name_menu):
        self.__name_menu = name_menu # กรณีกดปุ่มเลือก Tshirt ส่งค่า "Tshirt" มาใน self.__name_menu
        # โค้ดต่อจากนี้คือ การอ่านไฟล์ที่มีชื่อตามที่ได้รับมาจาก self.name_menu+".txt" มาใส่ในตัวแปร ???
        #for i in ???:
         #   self.__showitem = i
            # ลูปมาแสดงผลเลย โดยใช้ Get key, value ทีละ self.__showitem อาจจะเอามาแค่ รูป ชื่อ ราคา (ตามหน้าเว็บจริง)
        