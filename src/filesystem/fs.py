import os
from utils.config import get_config

config = get_config()

def check_fs():
    if not os.path.exists(".fs/"):
        return False
    return True

def check_user():
    return os.path.exists(f".fs/users/{config['username']}/")

def check_user_home():
    return os.path.exists(f".fs/users/{config['username']}/home/")

def create_fs():
    os.makedirs(".fs/users/", exist_ok=True)

def create_user_home():
    os.makedirs(f".fs/users/{config['username']}/home/", exist_ok=True)