# edit_the_code_below_this_line
def add_list_item(value, the_list=[]):
    the_list.append(value)
    return the_list
    # edit_the_code_above_this_line

first_result = add_list_item(1)
second_result = add_list_item(2)
print(first_result)
print(second_result)