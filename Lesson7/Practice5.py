import openpyxl as o
with open("text.csv", 'r') as reader1:
    file = reader1.read()


def field_tr(x: str):
    amount_of_words = x.count(',')
    amount_of_n = x.count("\n")
    amount_of_columns = int(amount_of_words/amount_of_n)
    for i in range(1, amount_of_n+1):
        for j in range(1, amount_of_columns+2):
            field.append(sheet.cell(row=i, column=j))


def get_data(f: str) -> list:
    data = []
    summ = ''
    for i in file.replace('\n', '/'):
        if i == '/' or i == ',':
            data.append(summ)
            summ = ''
        else:
            summ += i
    return data


data_to_write = get_data(file)
wb = o.Workbook()
sheet = wb.active
field = []
field_tr(file)
for i in range(len(field)):
    a = field[i]
    a.value = data_to_write[i]


wb.save("/home/ivan/PY88_ivan_davydovskiy/Lesson7/smth.xlsx")