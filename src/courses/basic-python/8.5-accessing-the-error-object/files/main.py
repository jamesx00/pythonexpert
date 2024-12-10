error_message = "You cannot divide by zero!"
error_message_2 = "You cannot divide a number with a string!"

def divide_the_number(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print(error_message)
    except TypeError:
        print(error_message_2)