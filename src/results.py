import xlrd

# Substitude absent with 0
def refine_list(sample_list):
    pass

# Giving location of the file
file_location = ('doc/results.xlsx')

# Opening the work book
wb = xlrd.open_workbook(file_location)
sheet = wb.sheet_by_index(0)

# Extracting first cell
"""
data = sheet.cell_value(0, 0)
print("first cell: ",data)
"""

# Extracting number of rows
"""
print("rows: ", sheet.nrows)
"""

# Extracting number of columns
"""
print("columns: ", sheet.ncols)
"""

# list of scores list
data = []

# Making the list
for row in range(sheet.nrows):
    single_row = []
    for col in range(sheet.ncols):
        single_row.append(sheet.cell_value(row, col))
        # print(single_row)
    data.append(single_row)

# Just for checking items in data[]
"""
for _ in data:
    print(_)
"""

# x = []
# y = []
# for line in data:
#     x.append(line[0:3])
#     y.append(line[3])
