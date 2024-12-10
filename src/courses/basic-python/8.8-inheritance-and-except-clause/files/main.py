error_message = "You cannot divide by zero!"
error_message_2 = "You cannot divide a number with a string!"

def divide_the_number(num1, num2):
    try:
        return num1 / num2
    # edit_the_code_below_this_line
    except (TypeError, ZeroDivisionError) as e:
    # edit_the_code_above_this_line
        if type(e) == ZeroDivisionError:
            print(error_message)
        if type(e) == TypeError:
            print(error_message_2)