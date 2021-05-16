class CustomError(Exception):
    message = ''
    code = 0

    def __init__(self, code, message):
        super().__init__(code, message)
        self.message = message
        self.code = code

def method1(num):
    if num <0:
        raise CustomError(-1,"数字不能小于0")
    else:
        print(num)

def mehtod2():
    try:
       method1(-100)
    except CustomError as ce:
       print("error code:"+str(ce.code))
       print("error message:" + ce.message)

mehtod2()