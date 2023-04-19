from datetime import datetime


def decorator(func):
    time1 = datetime.now()

    def wrap():
        print(func())

    time2 = datetime.now()
    print(time2 - time1)
    return wrap()


def func1():
    return "Hello"


def func2():
    return "Bye"


decorator(func1)
decorator(func2)
