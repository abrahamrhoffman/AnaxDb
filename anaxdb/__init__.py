__version__ = "0.9.9.4"

import os
from anaxdb import Database

if not os.path.isfile("config.ini"):
    f = open("config.ini", "w+")
    template = """
                [database]
                default_folder = db
                admin_username = admin
                admin_secret = admin
                admin_email = admin@example.com
                admin_password = admin
                initial_table_name = users

                [object_storage]
                address = 1.2.3.4
                port = 9000
                access_key = supersecret
                secret_key = supersecret
                ssl_flag = False
                """
    template = template.splitlines()[1:-2]
    for ix, ele in enumerate(template):
        f.write(str("".join(ele.split())) + "\n")
    f.close()
