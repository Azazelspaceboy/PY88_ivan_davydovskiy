import json as j
import csv as s

with open("HELLO.json") as file_read:
    di = j.load(file_read)
    print(di)

with open("text.csv", 'w') as out_file:
    writer = s.writer(out_file, delimiter=',')
    headers = [' '] + [f"person{i}" for i in range(1, len(di)+1)]
    writer.writerow(headers)
    id_ = ["id"] + [f"{i}"for i in di]
    name = ["name"] + [f"{(di[i])[0]}" for i in di]
    phone = ["phone", "+35675434567", "+1234565433456", "+1235676543267", "+234567876532345", "+34567865"]
    writer.writerow(id_)
    writer.writerow(name)
    writer.writerow(phone)
