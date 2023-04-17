def hey(func, x):
    for i in range(x):
        print(f"{i+1}", end="\t")
        func()
    return func


def hi():
    """HI"""
    print("hi")


def smile():
    """SMILE"""
    print("smile")


def rise():
    """RISE"""
    print("rise")


hey(hi, 3)
hey(smile, 5)
hey(rise, 10)
