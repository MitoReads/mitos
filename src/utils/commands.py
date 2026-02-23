commands = {}

def command(name):
    def wrapper(func):
        commands[name] = func
        return func
    return wrapper

def command_handler(input):
    args = input.split()
    if not args:
        return
    cmd = args[0]
    if cmd in commands:
        commands[cmd](args[1:])
    else:
        print(f"Unknown command: {cmd}")

@command("help")
def cmd_help(args):
    print("Available commands:")
    print("    help - Now you know what it does")
    print("    clear - Guess")
    print("    exit - Hmmm, what could it do?")

@command("exit")
def cmd_exit(args):
    exit(0)

@command("clear")
def cmd_clear(args):
    import os
    os.system("cls" if os.name == "nt" else "clear")