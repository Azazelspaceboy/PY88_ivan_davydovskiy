numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diction = {}
list(map(lambda x, y: diction.update({x: y}), numbers, list(map(lambda x: "even" if x % 2 == 0 else "odd", numbers))))
print(diction)
