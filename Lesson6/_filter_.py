def reverse(x: str) -> str:
    if len(x) == 1:
        return x
    return reverse(x[-1]) + reverse(x[:-1])


words = ("run", "gun", "level")
some = tuple(filter(lambda x: x == reverse(x), words))
print(some)
