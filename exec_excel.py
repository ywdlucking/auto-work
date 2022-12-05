from openpyxl import load_workbook

workbook = load_workbook(filename="data/最终扣款人员.xlsx")

sheet = workbook.active

print(sheet['A1']._value)