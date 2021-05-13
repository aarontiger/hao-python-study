import types

class Person(object):
  personName = '小明'
  def __init__(self,name):
    self.personName = name


def eatFood(self):
  print('%s在吃东西' % self.personName)

Person.eat = eatFood

p = Person('小刚')
p.eat()