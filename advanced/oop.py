import sys

class Animal:
    def __init__(self,name):
        self.name = name
        print("created an animal object:"+name);
    def eat(self,food):
        print("an animal: "+self.name+ " can eat :"+food);

class Cat(Animal):
    def __init__(self,name):
        #注意super的写法
        super(Cat, self).__init__(name)
        print("create a cat object")
    def catchMouce(self,size):
        print("the cat{} catch a {} mouce".format(self.name,size))

if __name__ == "__main__":
    print ('This is main of module "oop.py"')
    C =Cat("tom")
    C.catchMouce("big")
    print(hasattr(C,"catchMouce"))
    print(hasattr(C, "eat"))
    print(hasattr(C, "sleep"))
    #动态获取和调用方法
    fn=getattr(C,"eat")
    fn("jerry")

