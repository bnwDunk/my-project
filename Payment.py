class Payment:
    def __init__(self, payment_number, date_time, expiration_date, security_code):
        self.payment_number = payment_number
        self.date_time = date_time
        self.expiration_date = expiration_date
        self.security_code = security_code

class Visa(Payment):
    def __init__(self, visa_number, payment_number, date_time, expiration_date, security_code):
        Payment.__init__(self, payment_number, date_time, expiration_date, security_code)
        self.visa_number = visa_number

class MasterCard(Payment):
    def __init__(self, mastercard_number, payment_number, date_time, expiration_date, security_code):
        Payment.__init__(self, payment_number, date_time, expiration_date, security_code)
        self.mastercard_number = mastercard_number

class Bill:
    def __init__(self, parcel_number, delivery_price, total):
        self.parcel_number = parcel_number
        self.delivery_price = delivery_price
        self.total = total

class Delivery:
    def __init__(self, branch, destination_address, sending_datetime, complete_datetime, complete):
        self.branch = branch
        self.destination_address = destination_address
        self.sending_datetime = sending_datetime
        self.complete_datetime = complete_datetime
        self.complete = complete