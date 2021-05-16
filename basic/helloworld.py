import sys

class animal:
    def __init__(self,name):
        self.name = name
    def eat(self,food):
        print("the animal of: "+self.name+ " can eat :"+food);

# A =animal("tiger")
# A.eat("meat")

def helloMethod():
    a = 'hello world'
    print(a)

if __name__ == "__main__":

    A =animal("tiger")
    A.eat(sys.argv[1])

    # helloMethod()

