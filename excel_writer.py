from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.cell import coordinate_from_string, column_index_from_string

wb = load_workbook('test.xlsx')

# grab the active worksheet
ws = wb.active

target_date = raw_input("Date: ")
target_tester = raw_input("Name: ")
holiday = raw_input("Holiday: ")

for colomn in ws.columns:
	for cell in colomn:
		if cell.value == target_tester:
			xy = coordinate_from_string(cell.coordinate)
			target_row = xy[1]
			break

for colomn in ws.columns:
	for cell in colomn:
		if cell.value == target_date:
			cell.offset(target_row-3,0).value = holiday

# Save the file
wb.save('test.xlsx')