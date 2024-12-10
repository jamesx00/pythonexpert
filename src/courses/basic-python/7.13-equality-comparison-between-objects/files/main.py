class MyStr:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return str(self.text)

    # write_your_code_below_this_line

    # write_your_code_above_this_line

s1 = MyStr("Hello World")
s2 = MyStr("Hello World")
s3 = MyStr("Python is awesome")

print(s1 == s2)
print(s1 == s3)