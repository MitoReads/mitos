import os
from utils.config import get_config

config = get_config()
FS_ROOT = os.path.abspath(".fs")
USER_HOME = os.path.join(FS_ROOT, "users", config["username"], "home")


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

def resolve_path(path: str) -> str:
    if not path or path.strip() == "":
        return os.getcwd()

    if path.startswith("~"):
        path = path.replace("~", USER_HOME, 1)

    elif path.startswith("/"):
        path = os.path.join(FS_ROOT, path.lstrip("/"))

    else:
        path = os.path.join(os.getcwd(), path)

    resolved = os.path.abspath(os.path.normpath(path))

    if not resolved.startswith(FS_ROOT):
        raise PermissionError("Access outside filesystem root is not allowed")

    return resolved