file = open("Text.txt", 'w')
o = input()
b = input()
file.write(f"{o}\n{b}\n")
file = open("Text.txt", 'a')
c = input()
d = input()
file.write(f"{c}\n{d}")
file.close()
