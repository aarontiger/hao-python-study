class ClassA(object):

    def test123(self):

        print('ClassA.test123() running')


class ClassB(object):
    def test456(self):
        print('ClassB.test456() runing')
        return 10000


def createInstance(module_name, class_name, *args, **kwargs):

    module_meta = __import__(module_name, globals(), locals(), [class_name])
    class_meta = getattr(module_meta, class_name)
    obj = class_meta(*args, **kwargs)
    return obj


if __name__ == "__main__":

    objectA = createInstance("oop_dynamic1", "ClassA")
    print(hasattr(objectA,'test123'))
    objectA.test123()

    # objectB = createInstance("oop_dynamic1", "ClassB")
    # retValue = eval("objectB.test456")()
    # print(retValue)