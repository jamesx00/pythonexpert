class MyStr:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return str(self.text)

    def __eq__(self, other):
        return self.text == other.text

class MyUpperStr(MyStr):
    # write_your_code_below_this_line