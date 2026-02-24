from utils.console import clear, loop
from utils.config import *
from filesystem.fs import *

if not check_config():
    create_config()

if not check_fs():
    create_fs()
    create_user_home()

clear()
loop()