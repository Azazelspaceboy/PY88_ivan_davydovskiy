import json as j
di = {123456: ("Max", "Rex"), 143256: ("Pex", "Meh"),
      890123: ("Sam", "Ram"), 198765: ("Shis", "Mish"),
      178901: ("Call", "Xan")}

with open("HELLO.json", "w") as file:
    j.dump(di, file)
