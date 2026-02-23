from utils.console import clear, loop
from utils.config import *

if not check_config():
    create_config()

clear()
loop()