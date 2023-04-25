import json as j


class User:
    def __init__(self, name: str, password: str):
        self.name = name
        self.password = password


class Storage:
    def __init__(self):
        self.saved_data = {}
        self.__data_update()

    def __data_update(self):
        with open("saved_data.json", 'r') as file_reader:
            data = j.load(file_reader)
            self.saved_data.update(data)


def check_name(name: str) -> str:
    while 3 > len(name) or len(name) > 10:
        print("Something went wrong\nTry again")
        name = input("Enter your name again: ")
    return name


def get_name() -> str:
    name = input("Enter your name: ")
    return check_name(name)


def check_password(password: str) -> str:
    while len(password) < 5:
        print("Something went wrong\nTry again")
        password = input("Enter your password again: ")
    return password


def get_password() -> str:
    password = input("Enter your password: ")
    return check_password(password)


def authentication():
    print("***Authentication***")
    name, password = get_name(), get_password()
    while (name, password) not in class_data:
        print("Something went wrong\nTry again!")
        choice = input("Would you like to get back for registration(Y,N): ")
        while choice.lower() not in commands:
            print("Wrong command\nTry again!")
        if choice.lower() == commands[0]:
            registration()
            break
        else:
            authentication()
            break


def registration():
    print("***Registration***")
    name, password = get_name(), get_password()
    while name in names:
        print("User with that name already exists\n")
        choice = input("Do you have an account(Y,N): ")
        while choice.lower() not in commands:
            print("Wrong command try again")
            choice = input("Do you have an account(Y,N): ")
        if choice.lower() == commands[0]:
            authentication()
            break
        else:
            registration()
    with open("saved_data.json", 'r') as file_read:
        data_to_save = j.load(file_read)
        data_to_save.update({name: password})
        with open("saved_data.json", 'w') as file_write:
            j.dump(data_to_save, file_write)


commands = ['y', 'n']
data_base = Storage().saved_data
users = list(map(lambda x: User(x, data_base[x]), data_base.keys()))
class_data = list(map(lambda x: (users[x].name, users[x].password), [i for i in range(len(users))]))
names = [class_data[i][0] for i in range(len(class_data))]


while True:
    som = input("Do you have an account(Y,N): ")
    while som.lower() not in commands:
        print("wrong command try again: ")
        som = input("Do you have an account(Y,N): ")
    if som.lower() == commands[0]:
        authentication()
        print("Welcome to the system")
        break
    else:
        registration()
        print("Welcome to the system")
        break

