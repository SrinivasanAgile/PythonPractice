from Class import *

Srini = User("Srini", "Srini@xyz.com", "secret1", "DevOps")
Srini.get_info()

Vasan = User("Vasan", "Vasan@xyz.com", "secret2", "DevOps-Engg")
Vasan.get_info()


Srini.change_title("Developer")
Srini.get_info()
