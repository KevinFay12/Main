import openpyxl
wb = openpyxl.load_workbook('exampleFile.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')
sheet['A1']
