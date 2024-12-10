def get_discount(employee, years=None):
    # edit_the_code_below_this_line
    if employee == True and years > 5:
        return 20
    elif employee == True and years <= 5:
        return 10
    else:
        return 5
    # edit_the_code_above_this_line