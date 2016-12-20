import tornado.ioloop
import tornado.web
import json


def params(content):
    return { k: content.get(k)[-1] for k in content }

class Test(tornado.web.RequestHandler):
    def get(self):
        print "viendo argumentos"
        print self.request.arguments
        #self.set_header('Content-Type', 'application/javascript')
        self.write(params(self.request.arguments))
        #json.dumps({ k: self.get_argument(k) for k in self.request.arguments })
        #print dir(self.request.arguments)
        #return self.request.arguments
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

if __name__ == "__main__":
    application = tornado.web.Application([(r"/", MainHandler),(r"/api/foo", Test)])
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
