class Person(object):
    personName = '小明'

    def __init__(self,name):
        self.personName = name


def eatFood(self,foodName):
    print('%s在吃:%s' % (self.personName,foodName))


if __name__ == "__main__":

    #增加方法，两种方式
    # Person.set_instance_method(eatFood)
    Person.eat = eatFood

    p = Person('小刚')

    p.eat('油条')

    #增加属性
    # p.age = 18
    # print(p.age)

    #动态获取和调用方法,方式 1
    # a="eat"
    # fn=getattr(p,a)
    # fn("面包")

    # 动态获取和调用方法,方式 2
    # eval("p.eat")("薯片")




