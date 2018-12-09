def print_menu(menu):
    for i, m in enumerate(menu, start=1):
        print(f"{i}.{m}")


def get_command(menu):

    while True:
        command = input("Input command: ")

        if command.isdigit() and (1 <= int(command) <= len(menu)):
            return command
        else:
            print("Wrong command. Try again!")
