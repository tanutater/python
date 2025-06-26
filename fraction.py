class Fraction(object):
  def __init__(self,num,denom):
    assert type(num)==int and type(denom)==int ,"ints are not used"
    self.num=num
    self.denom=denom
  def __str__(self):
    return str(self.num) + "/" + str(self.denom)
  def __add__(self,other):
    top= self.num*other.denom + other.num*self.denom
    bott=self.denom*other.denom
    return Fraction(top,bott)
  def __sub__(self,other):
    top=self.num*other.denom-self.denom*other.num
    bott=self.denom*other.denom
    return Fraction(top,bott)
  def __float__(self):
    return self.num/self.denom
  def inverse(self):
    return Fraction(self.denom, self.num)
a = Fraction(1,4)
b = Fraction(3,4)
c = a + b # c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse()))