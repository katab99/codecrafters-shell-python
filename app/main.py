import sys


def get_command(user_input):
    return user_input.split()[0]


def run_echo(user_input):
    return user_input[5:]


def main():
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        command = get_command(user_input)

        if command == "exit":
            break
        if command == "echo":
            print(run_echo(user_input))
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
