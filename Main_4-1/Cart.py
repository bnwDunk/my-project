from Call import *

class Cart:
    def __init__(self):
        self.__item_list = []

    def add_to_cart_data(self,item):
        # print("in cart file : "+str(item.name_product))
        self.__item_list.append(item)

    def remove_from_cart_data(self,item):
        # อ่านข้อมูลจากฐานข้อมูล มาใส่ในตัวแปร และลูปหาข้อมูลที่ตรงกับที่จะลบ และลบข้อมูลในบรรทัดนั้นภายในฐานข้อมูล
        self.__item_list.remove(item)

    def clear_cart_data(self):
        self.__item_list = []

    def check_cart(self, cart, item):
        self.__check_list = len(cart)
        if self.__check_list <= 100:
            self.add_to_cart_data(item)
        else:
            self.over_limit_cart
    
    def over_limit_cart(self):
        print("Over Limit Cart")

class Items: # อันนี้คือที่จะแสดงหน้ารายการสินค้าทั้งหมด ไม่ใช่เอาสินค้ามาใส่ตะกร้า อันนั้นมันจะเป็น Product
    def __init__(self, cart): # ตรงนี้จะต้อลลูปหลายชั้น เพื่อที่จะนำข้อมูลในลิสมาแสดงทั้งหมด ทีละอัน
        self.__all_items = cart # ลูปมากกว่านี้ อันนี้เขียนแค่ไม่ให้มัน error

    def confirm_item(self, confirm_item): # ***** ตรงนี้น่าจะไปอยู่ที่ AuthenticateUser มากวก่าที่จะอยู่ตรงนี้ self.__my_order = Order(self.__all_items)
        if confirm_item == True:
            Order(self.__all_items)
        else:
            self.cancle_item()

    def cancle_item(self):
        print("Cancle Item In Cart")

class Order: # เป็นการสรุปรายการเพื่อยืนยันอีกครั้ง โดยจะแสดงแค่เหล่านี้เท่านั้น name, total_amount, total_price แล้วก็คำนวณสุทธิทั้งหมด
    def __init__(self, cart):
        self.__all_items = cart # ลูปมากกว่านี้ อันนี้เขียนแค่ไม่ให้มัน error

    def confirm_order(self, confirm_order):
        if confirm_order == True:
            Payment(self.__all_items)
            pass

        else:
            self.cancle_order()

    def cancle_order(self):
        print("Cancle Item In Cart")