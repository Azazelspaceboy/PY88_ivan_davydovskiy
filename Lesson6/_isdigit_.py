def checker(x: str) -> str:
    if x.isdigit():
        return f"{x}: positive integer"
    elif (x.replace('.', '')).replace('-', '').isdigit():
        if x.count('.') > 1 or '.' == x[len(x)-1]:
            return f"{x}: invalid value"
        elif x.count('-') > 1 or '-' != x[0]:
            return f"{x}: invalid value"
        elif "-." in x or ".-" in x:
            return f"{x} invalid value"
        else:
            if '.' in x and '-' not in x:
                return f"{x}: positive fractional number"
            elif '.' in x and '-' in x:
                return f"{x}: negative fractional number"
            elif '-' in x and x.replace('-', '').isdigit():
                return f"{x}: negative integer"
    else:
        return f"{x}: invalid value"


print(checker("1234568765432"))

