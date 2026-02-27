import os
from utils.commands import command_handler
from utils.config import get_config

config = get_config()

def loop():
    while True:
        current_dir = os.path.basename(os.getcwd())
        command = input(f"[{config['username']}@{config['hostname']} {current_dir}]$ ")
        command_handler(command)
def clear():
    import os
    os.system("cls" if os.name == "nt" else "clear")