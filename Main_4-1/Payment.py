from Call import *

class Payment:
    def __init__(self, payment_number, date_time, expiration_date, security_code): # ตรงนี้จะต้องลูปหลายชั้น เพื่อที่จะนำข้อมูลในลิสมาแสดงทั้งหมด ทีละอัน
        self.__payment_number = payment_number
        self.__date_time = date_time
        self.__expiration_date = expiration_date
        self.__security_code = security_code

    def show_payment_data(self, cart):
        self.__all_items = cart # ลูปมากกว่านี้ อันนี้เขียนแค่ไม่ให้มัน error
        self.__total = 1+1 # name, total_amount, total_price แล้วก็คำนวณสุทธิทั้งหมด
    
    def confirm_payment(self, confirm_order, select_payment_method):
        if confirm_order == True and select_payment_method != "":
            self.__delivery_data = self.create_delivery()
            Bill() # ตรงนี้จะต้องส่งข้อมูลทั้งหมดไปเพื่อที่จะลูปแสดงผลให้ครบถ้วน
        else:
            self.cancle_payment()

    def cancle_payment(self):
        print("Cancle Item In Cart")

    def payment_method(self, select_payment_method): # เมื่อกดเลือกจะให้ไปแสดงหน้ากรอกข้อมูลของประเภทนั้น ๆ
        if select_payment_method == "Visa":
            self.__visa_data = Visa()
        elif select_payment_method == "MasterCard":
            self.__visa_data = MasterCard()
        else:
            print("Please Select You Payment Method")

    def create_delivery(self):
        Delivery()

class Visa(Payment):
    def __init__(self, visa_number, payment_number, date_time, expiration_date, security_code):
        Payment.__init__(self, payment_number, date_time, expiration_date, security_code)
        self.visa_number = visa_number

    def read_visa_data(self):
        # อ่านข้อมูลในไฟล์ Visa.txt เฉพาะ User ที่เรียกใช้
        pass

    def confirm_visa_data(self):
        # กดปุ่มยืนยันข้อมูล ทำการตรวจสอบว่ากรอกข้อมู,ครบหรือไม่ รูปแบบถูกหรือไม่ จากนั้นจึงมีข้อมูลเก็บไว้
        pass

class MasterCard(Payment):
    def __init__(self, mastercard_number, payment_number, date_time, expiration_date, security_code):
        Payment.__init__(self, payment_number, date_time, expiration_date, security_code)
        self.mastercard_number = mastercard_number

    def read_mastercard_data(self):
        # อ่านข้อมูลในไฟล์ MasterCard.txt เฉพาะ User ที่เรียกใช้
        pass

    def confirm_mastercard_data(self):
        # กดปุ่มยืนยันข้อมูล ทำการตรวจสอบว่ากรอกข้อมู,ครบหรือไม่ รูปแบบถูกหรือไม่ จากนั้นจึงมีข้อมูลเก็บไว้
        pass

class Delivery:
    def __init__(self, branch, destination_address, sending_datetime, complete_datetime, complete):
        self.__branch = branch
        self.__destination_address = destination_address
        self.__sending_datetime = sending_datetime
        self.__complete_datetime = complete_datetime
        self.__complete = complete

    def read_dalivery_data(self):
        # อ่านที่อยู่ผู้สั่งซื้อสินค้าจากไฟล์ Delivery.txt  เฉพาะ User ที่เรียกใช้
        pass

    def confirm_dalivery_data(self):
        # กดปุ่มยืนยันข้อมูล ทำการตรวจสอบว่ากรอกข้อมู,ครบหรือไม่ รูปแบบถูกหรือไม่ จากนั้นจึงมีข้อมูลเก็บไว้
        pass

class Bill:
    def __init__(self, cart):  # มีตัวแปรเยอะเลยแหละ
        self.__all_items = cart # ลูปมากกว่านี้ อันนี้เขียนแค่ไม่ให้มัน error
        self.__total = 1+1 # name, total_amount, total_price แล้วก็คำนวณสุทธิทั้งหมด