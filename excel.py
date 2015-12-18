import xlrd


wb = xlrd.open_workbook('ActivitySummaryReport_Ev_May.xls')

# grab the active worksheet
ws = workbook.sheet_by_name('ActivitySummaryReport')

for colomn in ws.columns:
	for cell in colomn:
		if cell.value == "Activity Date":
			xy = coordinate_from_string(cell.coordinate)
			target_column = xy[0]
			print target_column
			break

# Save the file
wb.save('ActivitySummaryReport_Ev_May.xls')