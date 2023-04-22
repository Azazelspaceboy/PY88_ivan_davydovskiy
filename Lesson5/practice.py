def fac(x: int = 1) -> int:
    output = 1
    y = x
    for i in range(x):
        output *= y
        y -= 1
    return output


def re_fac(x: int) -> int:
    if x == 1:
        return 1
    else:
        return x * re_fac(x-1)


arr_1 = [1, 1, 2, 3, 2, 5, 5]
out = {}


def count(arr: list) -> None:
    for i in arr:
        out.update({i: arr.count(i)})


count(arr_1)
print(out)
print(re_fac(6))


def swap(d: dict) -> None:
    for i in d:
        dict_2.update({d[i]: i})


dict_1 = {1: "A", 2: "B", 3: "C"}
dict_2 = {}
swap(dict_1)
print(dict_2)
