# Author: Nima Daryabar
"""
    The purpose of the code is getting a list (e.g a list of IELTS scores),
    if there is any 'absent' item in the list turn them to 0 and it will
    calculate the score and put them in the end of the lists and at the end,
    implement Decision Tree Regression on it.
    So user can enter it's scores and it will guess it's score.
    Note that we don't need to use decision tree to predict an ielts band score 
    cause you simply can add them together and then divid them into 4 but 
    I just want to show you how you can use decision tree regression using a data set
    and in future I'll promise i will use more rational data and do something more 
    Just for Fun :D
"""
import xlrd
from sklearn import tree
from replace import refine_list
from average import ielts_scores


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

# List with final score which is appended at the end of lists
ielts_scores_list = ielts_scores(refined_data_list)
# for _ in ielts_scores_list:
#     print(_)


# Training data for Decision Tree Regression
X = []
y = []
for _, lst in enumerate(ielts_scores_list):
    # print(_ , lst)
    X.append(lst[0:4])
    y.append(lst[4])

# Decision Tree Regression. tarining data set
clf = tree.DecisionTreeRegressor()
clf = clf.fit(X, y)

user_scores = []
print("Enter your scores please")
speaking_score = float(input("Speaking score: "))
listening_score = float(input("Listening score: "))
reading_score = float(input("Reading score: "))
writing_score = float(input("Writing score: "))

user_scores = [speaking_score, listening_score, reading_score, writing_score]
# print(user_scores)

# print(clf.predict([user_scores]))

# Predicting the IELTS band score
print()
band_score = clf.predict([user_scores])
print(f"result: {float(band_score)}")
