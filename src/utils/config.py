import os

def check_config():
    if not os.path.exists(".config/config"):
        return False
    return True

def create_config():
    username = input("Enter your username (default: Guest): ") or "guest"
    hostname = input("Enter your hostname (default: mitos): ") or "mitos"

    os.makedirs(".config", exist_ok=True)
    with open(".config/config", "w") as f:
        f.write(f"username={username}\n")
        f.write(f"hostname={hostname}\n")
        
def get_config():
	config = {}
	with open(".config/config", "r") as f:
		for line in f:
			key, value = line.strip().split("=")
			config[key] = value
	return config