# encoding:utf-8
import os
import tornado.wsgi
import sae

# 配置模板和静态文件地址
settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "js_path": os.path.join(os.path.dirname(__file__), "js"),
    "css_path": os.path.join(os.path.dirname(__file__), "css"),
    # "gzip" : True,
    # "debug": True,
}


# 主页面
class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.render("index1.html")

# 生成app
def make_app():
    app = tornado.wsgi.WSGIApplication(
        [(r"/", MainHandler,)],
        **settings
    )
    return app

app = make_app()
application = sae.create_wsgi_app(app) # 运行
