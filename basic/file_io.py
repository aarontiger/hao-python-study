
def readFile(fileName):

    with open(fileName, 'r') as f:
        print(f.read())


def writeFile(fileName):
    #覆盖模式
    #f = open(fileName, 'w')
    #追加写入模式
    f = open(fileName, 'a')
    f.write('Hello, world!keep eye on my mind')
    f.close()

writeFile("./haohao/test22.txt")
readFile("./haohao/test22.txt")