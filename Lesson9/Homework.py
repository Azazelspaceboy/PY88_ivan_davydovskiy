import json as j
from dataclasses import dataclass


@dataclass
class DataStorage:
    path_to_storage = "/home/ivan/PY88_ivan_davydovskiy/Lesson8/saved_data.json"


class User:
    def __init__(self, name, password, age):
        self.name = name
        self.password = password
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age


class Storage:
    @staticmethod
    def data():
        with open(DataStorage.path_to_storage, 'r') as file_reader:
            data = j.load(file_reader)
            return data


@dataclass
class Errors:
    message = "Something went wrong"


@dataclass
class Commands:
    yes = 'y'
    no = 'n'


class Input:
    @staticmethod
    def check_name():
        name = input("Enter your name: ")
        while len(name) < 4 or len(name) > 10:
            print(Errors.message)
            name = input("Enter your name")
        return name

    @staticmethod
    def check_password():
        password = input("Enter your password: ")
        while len(password) < 5:
            print(Errors.message)
            password = input("Enter your password: ")
        return password

    @staticmethod
    def get_age():
        age = input("Enter your age: ")
        while not age.isdigit():
            print(Errors.message)
            age = input("Enter your age: ")
        return age


class AuthenticationSystem:
    @staticmethod
    def authentication():
        temp_user = User(Input.check_name(), Input.check_password(), Input.get_age())
        saved_data = Storage.data()
        while {temp_user.name: temp_user.password} not in saved_data:
            choice = input(f"{Errors.message}.\nWould you like to get back to registration(Y,N): ").lower()
            while choice not in [Commands.yes, Commands.no]:
                choice = input("Would you like to get back to registration(Y,N): ").lower()
            if choice == Commands.yes:
                RegistrationSystem.registration()
            else:
                AuthenticationSystem.authentication()


class RegistrationSystem:
    @staticmethod
    def registration():
        saved_data = Storage.data()
        temp_user = User(Input.check_name(), Input.check_password(), Input.get_age())
        while {temp_user.name: temp_user.password} in saved_data:
            choice = input(f"{Errors.message}.\nDo you have account already(Y,N): ").lower()
            while choice not in [Commands.yes, Commands.no]:
                choice = input(f"{Errors.message}.\nDo you have account already(Y,N): ").lower()
            if choice == Commands.yes:
                AuthenticationSystem.authentication()
            else:
                RegistrationSystem.registration()
        with open(DataStorage.path_to_storage, 'r') as file_reader:
            data_to_save = j.load(file_reader)
            data_to_save.append({temp_user.name: temp_user.password})
            with open(DataStorage.path_to_storage, 'w') as file_writer:
                j.dump(data_to_save, file_writer)


while True:
    option = input("Type smth to exit, 'y' if you have account, 'n' if you don't: ").lower()
    if option in [Commands.yes, Commands.no]:
        commands = {'y': AuthenticationSystem.authentication, 'n': RegistrationSystem.registration}
        (commands[option])()
        print("Welcome to system")
        break
    else:
        break
