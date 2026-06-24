import shutil
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


def do_run_executable(command, *args):
    print(f"Program was passed {len(args)} args (including program name).")
    print(f"Arg #0 (program name): {command}")

    for i, arg in enumerate(args):
        print(f"Arg #{i + 1}: {arg}")


def main():
    while True:
        user_input = input("$ ").strip()

        tokens = user_input.split()
        command = tokens[0].lower()
        args = tokens[1:]

        if command in COMMANDS:
            COMMANDS[command]["action"](*args)
        elif shutil.which(command):
            do_run_executable(command, *args)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
