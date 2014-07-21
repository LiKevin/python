__author__ = 'k22li'

import tornado.web
import tornado.ioloop

class MainTornadoHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('hello world!')

application =  tornado.web.Application([(r"/", MainTornadoHandler),])


if __name__=="__main__":

    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

