saved_data = {"Petya": "HELLO", "Ivan": "EZz", "Maxim": "AZaz"}
error_msg = "Something went wrong.Try again!"
commands = ['y', 'n']


def check_name(name: str) -> str:
    while 2 > len(name) or len(name) > 11:
        print(error_msg)
        name = input("Please enter your name again: ")
    return name


def get_name() -> str:
    name = input("Enter your name: ")
    return check_name(name)


def check_password(password: str) -> str:
    while 2 > len(password) or len(password) > 11:
        print(error_msg)
        password = input("Please enter your password again: ")
    return password


def get_password() -> str:
    password = input("Enter your password: ")
    return check_password(password)


def auth():
    print(27*"-")
    name, password = get_name(), get_password()
    count = 0
    while (name, password) not in saved_data.items():
        print(error_msg)
        count += 1
        name, password = get_name(), get_password()
        if count == 3:
            command = input("Are you sure that you already in the system?\n"
                            "Type Y if you want to get back to reg, or N if you dont.\n>> ")
            while command.lower() not in commands:
                print(error_msg)
                command = input(">> ")
            if command.lower() == 'y':
                reg()
            elif command.lower() == 'n':
                count = 0
    print(f"Welcome back, {name}!")
    print((27*"-"))


def reg():
    print(27*"*")
    command = input("Are you already in the system?\nType Y, or N if you are new.\n>> ")
    while command.lower() not in commands:
        print(error_msg)
        command = input(">> ")
    if command.lower() == 'y':
        auth()
    elif command.lower() == 'n':
        name, password = get_name(), get_password()
        saved_data.update({name: password})
        print("Done")
        auth()


reg()
