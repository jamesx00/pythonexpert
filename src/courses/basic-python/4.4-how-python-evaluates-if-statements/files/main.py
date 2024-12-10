def get_spicy_message(spicy_level):
    # edit_the_code_below_this_line
    if spicy_level > 3:
        return "A little spicy"
    elif spicy_level > 4:
        return "Very spicy"
    else:
        return "Not spicy"
    
print(get_spicy_message(3))
print(get_spicy_message(4))
print(get_spicy_message(5))
print(get_spicy_message(6))