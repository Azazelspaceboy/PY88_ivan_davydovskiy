def checker(x: str):
    if x.isdigit():
        print(f"{x}: positive integer")
    elif '-' in x and x[1].isdigit() and '.' not in x:
        print(f"{x}: negative integer")
    elif '.' in x and (x[0:x.index('.')-1] + x[x.index('.')+1]).isdigit():
        print(f"{x}: positive fractional number")
    elif '-' in x and (x[1:x.index('.')-1] + x[x.index('.')+1]).isdigit():
        print(f"{x}: negative fractional number")
    else:
        print(f"{x}: invalid value")


checker("-11.7")
checker("11.2")
checker("-1")
checker("11r")


