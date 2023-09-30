# To access the shopping cart, create a Customer() instance.
# shopper = Customer('Daniel', 500)

# Then create a Product() instance.
# shampoo = Product('13 In One Shampoo', 30)

# Finally, add/remove products.
# shopper.addToCart(shampoo)

class ShoppingCart:
  def __init__(self, customer):
    self.customer = customer
    self.products = {}

  def addToCart(self, product, quantity=1):
    self.products[product] = quantity

  def removeFromCart(self, product):
    del self.products[product]

  def changeProductQuantity(self, product, new_quantity):
    self.products[product] = new_quantity

  def checkOut(self):
    total = 0
    for prod in self.products:
      total += prod.price * self.products[prod]
    inpt = input(f"Total is {round(total, 2)}. Checkout (Y/N)? ")
    if inpt.lower() == "y" and self.customer.balance >= total:
      self.customer.balance -= total
      print("Thank you for your purchase.")
    elif self.customer.balance < total:
      print("Not enough funds.")
    else:
      print("Going back.")

  def __repr__(self):
    return f"{self.products}"

class Product:
  def __init__(self, name, price):
    self.name = name 
    self.price = price
    
  def __repr__(self):
    return f"{self.name}"

class Customer:
  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.shopping_cart = ShoppingCart(self)

  def addToCart(self, product, quantity=1):
    self.shopping_cart.addToCart(product, quantity)

  def removeFromCart(self, product):
    self.shopping_cart.removeFromCart(product)

  def changeProductQuantity(self, product, new_quantity):
    self.shopping_cart.changeProductQuantity(product, new_quantity)

  def checkOut(self):
    self.shopping_cart.checkOut()
    
  def __repr__(self):
    return f"{self.name}"
