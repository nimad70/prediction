import xlrd

# Giving location of the file
file_location = ('doc/results.xlsx')

# Opening the work book
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)

# Extracting first cell
""" data = sheet.cell_value(0, 0)
print("first cell: ",data) """

# Extracting number of rows
"""print("rows: ", sheet.nrows)"""

# Extracting number of columns
"""print("columns: ", sheet.ncols)"""


