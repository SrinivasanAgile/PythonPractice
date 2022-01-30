from Class import *
from Post import *

Admin = User("Admin", "Srini@xyz.com", "secret1", "DevOps")
Admin.get_info()

Vasan = User("Vasan", "Vasan@xyz.com", "secret2", "DevOps-Engg")
Vasan.get_info()

Admin.change_title("Developer")
Admin.get_info()

new_post=Post("Hi, this is a practice file", Admin.name)
new_post.get_post_info()