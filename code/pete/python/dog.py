class Dog:
  def __init__(self, name, coat, weight):
    self.name = name
    self.coat = coat
    self.weight = weight

  def bark(self):
    print('woof')
  
  def eat(self, amount_of_food):
    self.weight += amount_of_food
  
  def __str__(self):
    return self.name


frankie = Dog('Frankie', 'shaggy', 20)