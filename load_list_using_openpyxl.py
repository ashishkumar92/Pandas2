import openpyxl

list_2D = [
[11, 12, 13, 14],
[21, 22, 23, 24],
[31, 32, 33, 34],
]

path_excel = r'test21.xlsx'

wb = openpyxl.load_workbook(path_excel)
sheet = wb.worksheets[0]

for row in list_2D :
    sheet.append(row)

wb.save(path_excel)
wb.close()