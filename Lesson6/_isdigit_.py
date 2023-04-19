def checker(x: str):
    if x.isdigit():
        print(f"{x}: positive integer")
    elif '-' in x and x[1].isdigit() and '.' not in x:
        print(f"{x}: negative integer")
    elif '.' in x and (x[0:x.index('.')-1] + x[x.index('.')+1]).isdigit() and '-' not in x:
        print(f"{x}: positive fractional number")
    elif '-' in x and (x[1:x.index('.')-1] + x[x.index('.')+1]).isdigit() and (x[:2] != '-.' or x[:2] != '-.'):
        print(f"{x}: negative fractional number")
    elif x[:2] == '-.' or x[:2] == '.-':
        print(f"{x}: invalid value")
    else:
        print(f"{x}: invalid value")


checker("-11.7")
checker("123.122.123")
checker("-1")
checker("11r")
checker(".-814")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def checker