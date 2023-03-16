class Items:
  def __init__(self, name_product, total_price, total_amount):
    self.name_product = name_product
    self.total_price = total_price
    self.total_amount = total_amount

class Cart:
  def __init__(self, items):
    self.items = items

class Order:
  def __init__(self, cart, total_amount, total_price):
    self.cart = []
    self.total_amount = total_amount
    self.total_price = total_price






