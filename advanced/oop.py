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
        print("create a cat object："+name)
    def catch(self,foodName):
        print("the cat: {} catch：  {}".format(self.name,foodName))

if __name__ == "__main__":
    print ('This is main of module "oop.py"')
    C =Cat("汤姆")
    C.catch("杰瑞")

    # print(isinstance(C,Animal))

    # userName="haoshuhu"
    # print(userName)
    # print(isinstance(userName,Animal))


