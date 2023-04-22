import json as j


def data_update() -> dict:
    while True:
        file = open("saved_data.json", 'r')
        data = j.load(file)
        return data


def check_name(name: str) -> str:
    while 2 > len(name) or len(name) > 11:
        print("Something went wrong")
        name = input("Enter your name again: ")
    return name


def get_name() -> str:
    name = input("Enter your name: ")
    return check_name(name)


def check_password(password) -> str:
    while len(password) < 4:
        print("Something went wrong")
        password = input("Enter your password again: ")
    return password


def get_password() -> str:
    password = input("Enter your password: ")
    return check_password(password)


def authentication():
    name, password = get_name(), get_password()
    if (name, password) in saved_data["saved_data"].items():
        return
    else:
        choice = input("Incorrect input, would you like to get back to Registration?(Y/N)\n>> ")
        while choice.lower() not in commands:
            choice = input("Incorrect input, would you like to get back to Registration?(Y/N)\n>> ")
        if choice.lower() == commands[0]:
            return registration()
        else:
            authentication()


def registration():
    name, password = get_name(), get_password()
    if name not in saved_data["saved_data"].keys():
        with open("saved_data.json", 'r+') as file:
            data = {name: password}
            save = j.load(file)
            with open("saved_data.json", 'w') as file_1:
                save["saved_data"].update(data)
                j.dump(save, file_1)
    elif name in saved_data["saved_data"].keys():
        print("User with that name already exists")
        return registration()


saved_data = data_update()
# updating data in real time


commands = ['y', 'n']
while True:
    enter = input("Y if you are new\nN if you aren't\n>> ")
    while enter.lower() not in commands:
        enter = input("Y if you are new\nN if you aren't\n>> ")
    if enter.lower() == commands[0]:
        registration()
        print("Successful registration\nWelcome to the system!")
        break
    else:
        authentication()
        print("Welcome to the system")
        break
