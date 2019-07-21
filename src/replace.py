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