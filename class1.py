class Animal:
 def __init__(self, age):
  self.age = age
  self.name = None
 def get_age(self):
  return self.age
 def get_name(self):
  return self.name
 def set_age(self, newage):
  self.age = newage
 def set_name(self, newname=""):
  self.name = newname
 def __str__(self):
  return "animal:"+str(self.name)+":"+str(self.age)
anima1=Animal(3)
print(anima1.get_age())