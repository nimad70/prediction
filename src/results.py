# Author: Nima Daryabar
"""
    The purpose of the code is getting a list (e.g a list of IELTS scores),
    if there is any 'absent' item in the list turn them to 0 and it will
    calculate the score and put them in the end of the lists and at the end,
    implement Decision Tree Regression on it.
    So user can enter it's scores and it will guess it's score.
    Just for Fun :D
"""
import xlrd


# Replacing 'absent' with 0
# List with 0 instead of 'absent' will be returned
def refine_list(sample_list):
    # Search through every list in the list 
    # and replacing 'absent' with 0
    for lst in sample_list:
        for _, item in enumerate(lst):
            # print(_, "  ", item)
            if item == 'ABSENT':
                lst[_] = 0
    return sample_list
    

# Calculate average for each list
def ielts_scores(ielts_list):
    # Iterate through the list to calculate average for each item(list)
    for _, lst in enumerate(ielts_list):
        sum = 0
        # print(_ , lst)
        # Adding items in the list
        for item in lst:
            sum += item
            # print(sum)
        # print("lenght of list is: ", len(lst))
        # Calculate Score by dividing sum into lenght of list(i.e 4)
        score = sum / len(lst)
        print(score)
        print()
        # Just for check first 5 lists
        if(_ == 5):
            break
        



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

# List with 0 as 'absent' values
refined_data_list = refine_list(data)

# ielts_scores_list = 
ielts_scores(refined_data_list)

# x = []
# y = []
# for line in data:
#     x.append(line[0:3])
#     y.append(line[3])
