from handlers.foo import FooHandler
from handlers.index import IndexHandler
from handlers.login import LoginHandler
url_patterns = [
    (r"/foo", FooHandler),
    (r"/$", IndexHandler),
    (r"/login", LoginHandler),
]
