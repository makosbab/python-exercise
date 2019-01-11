def reg(func):
  return func() + 10

def f():
  return 5

x = reg(f)



class B():
  def __init__(self, val):
    self.value = val

  @property
  def dyn(self):
    return self.value // 2

class A():
  def __init__(self):
    self.a = [B(1), B(2), B(3)]

a = A()
print (a.a[2].dyn)