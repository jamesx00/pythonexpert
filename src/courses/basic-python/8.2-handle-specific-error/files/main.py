error_message = "You cannot divide by zero!"

def divide_the_number(num1, num2):
    try:
        return num1 / num2
    # edit_the_code_below_this_line
    except:
        print(error_message)