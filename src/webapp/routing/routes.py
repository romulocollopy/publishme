from ..controllers.root import hello_world
from lib.routing.url import Url


routes = (
    Url('/', hello_world, path_name="hello-world"),
)
