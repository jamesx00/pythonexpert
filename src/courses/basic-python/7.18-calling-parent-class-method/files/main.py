class MyStr:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return str(self.text)

    def __eq__(self, other):
        return self.text == other.text

class MyUpperStr(MyStr):
    # edit_the_code_below_this_line
    pass

print(MyStr("It's time to code!").text)
print(MyStr("It's time to code!"))
print(MyUpperStr("It's time to code!").text)
print(MyUpperStr("It's time to code!"))