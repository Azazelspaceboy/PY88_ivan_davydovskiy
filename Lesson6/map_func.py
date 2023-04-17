numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diction = {}
something = list(map(lambda x: "even" if x % 2 == 0 else "odd", numbers))
print(something)


def some_activity(x, y):
    for i in range(len(numbers)):
        diction.update({x[i]: y[i]})


some_activity(numbers, something)
print(diction)
