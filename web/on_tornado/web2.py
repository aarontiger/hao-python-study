#测试通过2021/03/04

import tornado.ioloop
import tornado.web

class BejingHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("I'm at BeiJing get")

class TianjinHandler(tornado.web.RequestHandler):
    def post(self):
        self.write("I'm at TianJin post")

def make_app():
    return tornado.web.Application([
        (r"/beijing", BejingHandler),
        (r"/tianjin", TianjinHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
