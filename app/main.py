import os
import shutil
import subprocess
import sys

COMMANDS = {}


def command(name: str):
    def decorator(func):
        COMMANDS[name] = {"action": func}
        return func

    return decorator


@command("exit")
def do_exit():
    sys.exit()


@command("echo")
def do_echo(*args):
    print(*args)


@command("type")
def do_type(*args):
    cmd_name = args[0]

    if cmd_name in COMMANDS:
        print(f"{cmd_name} is a shell builtin")
    elif pth := shutil.which(cmd_name):
        print(f"{cmd_name} is {pth}")
    else:
        print(f"{cmd_name}: not found")


@command("pwd")
def do_pwd():
    print(os.getcwd())


@command("cd")
def do_cd(*args):
    pth = args[0]

    if pth == "~":
        pth = os.environ["HOME"]

    try:
        os.chdir(pth)
    except Exception:
        print(f"cd: {pth}: No such file or directory")


def main():
    while True:
        user_input = input("$ ").strip()

        tokens = user_input.split()
        command = tokens[0].lower()
        args = tokens[1:]

        if command in COMMANDS:
            COMMANDS[command]["action"](*args)
        elif shutil.which(command):
            subprocess.run(tokens)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
