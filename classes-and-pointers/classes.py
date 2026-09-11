## Classes

# A class is a blueprint for creating objects. 
# It defines the data (attributes) and behavior (methods) that objects will have.

class Cookie:
  def __init__(self, color):
    self.color = color

  def get_color(self):
    return self.color

  def set_color(self, color):
    self.color = color


cookie_one = Cookie('Green')
print(cookie_one.get_color())  # Green

cookie_two = Cookie('Blue')
print(cookie_two.get_color())  # Blue

cookie_two.set_color("White")
print(cookie_two.get_color())  # White
