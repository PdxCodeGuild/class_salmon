class Cat:
  def __init__(self, name, personality, color, lives):
    self.name = name
    self.personality = personality
    self.color = color
    self.lives = lives

  def meow(self):
    print('meow')

  def talk(self):
    print(f"My name is {self.name}.  I am a {self.personality} cat with {self.color} fur.")

  def jump(self):
    self.lives -= 1

garfield = Cat('Garfield', 'nonchalant', 'orange', 9) # instantiate a Cat object called garfield

heathcliff = Cat('Heathcliff', 'bad boy', 'orange', 9)

print(heathcliff.lives)
heathcliff.jump()
print(heathcliff.lives)


# garfield.meow()
# garfield.talk()
# garfield.meow()

# print()

# heathcliff.meow()
# heathcliff.talk()
# heathcliff.meow()

