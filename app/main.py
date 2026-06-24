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
    else:
        print(f"{cmd_name}: not found")


def main():
    while True:
        user_input = input("$ ").strip()

        tokens = user_input.split()
        command = tokens[0].lower()
        args = tokens[1:]

        # if command == "exit":
        #     break

        if command in COMMANDS:
            COMMANDS[command]["action"](*args)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
