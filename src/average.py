# Author: Nima Daryabar
"""
    A list will be passed to ielts_scores() function and
    band score will be calculated for each list of scores
    and result will be added at the end of list and the final list
    with results and scores is returned
"""
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
        lst.append(score)
        # Just for check first 5 lists
        # print(score)
        # print(lst)
        # print()
        # if(_ == 5):
            # break
    return ielts_list