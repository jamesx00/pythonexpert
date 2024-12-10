class A:
    def method(self):
        return "A"

class B:
    def method(self):
        return "B"
    
class C:
    def method(self):
        return "C"

# edit_the_code_below_this_line
class D(A, B, C):
    pass

print(D.__mro__)
print(D().method())