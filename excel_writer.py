from datetime import datetime
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.cell import coordinate_from_string, column_index_from_string

wb = load_workbook('I:\Storage\Documents\Dev Projects\Excel\\test.xlsx', data_only=True)

# grab the active worksheet
ws = wb.active

target_row = 0
target_date = raw_input("Date: ")
target_tester = raw_input("Name: ")
holiday = raw_input("Holiday: ")


for colomn in ws.columns:
	for cell in colomn:
		if cell.value == target_tester:
			xy = coordinate_from_string(cell.coordinate)
			target_row = xy[1]
			print target_row
			print "breaking now"
			break
		
for colomn2 in ws.columns:
	for cell in colomn2:
		if cell.is_date == True:
			x = str(cell.value)
			string_date = datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime('%d/%m/%Y')
			if string_date == target_date:
				print "found it!"
				cell.offset(target_row-3,0).value = holiday

# Save the file
wb.save('I:\Storage\Documents\Dev Projects\Excel\\test.xlsx')