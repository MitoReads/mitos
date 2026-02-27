import os
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

@command("cd")
def cmd_cd(args):
    if not args:
        print("Usage: cd <directory>")
        return

    from filesystem.fs import resolve_path
    try:
        new_path = resolve_path(args[0])
        os.chdir(new_path)
    except Exception as e:
        print("Directory not found")

@command("ls")
def cmd_ls(args):
    from filesystem.fs import resolve_path

    try:
        target = resolve_path(args[0]) if args else os.getcwd()

        if not os.path.isdir(target):
            print("Not a directory")
            return

        entries = os.listdir(target)
        entries.sort()

        for entry in entries:
            full_path = os.path.join(target, entry)

            if os.path.isdir(full_path):
                print(f"{entry}/")
            else:
                print(entry)

    except Exception as e:
        print("Error listing directory")

@command("clear")
def cmd_clear(args):
    import os
    os.system("cls" if os.name == "nt" else "clear")