from handlers.foo import FooHandler
from handlers.index import IndexHandler

url_patterns = [
    (r"/foo", FooHandler),
    (r"/$", IndexHandler),
]
