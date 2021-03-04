import sys

class animal:
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("an animal: "+self.name+ " can eat :"+food);

# A =animal("tiger")
# A.eat("meat")

if __name__ == "__main__":
    print ('This is main of module "hello.py"')
    print(sys.argv[1])
    print(sys.argv.__len__())
    A =animal("tiger")
    A.eat(sys.argv[1])

