class Myclass:
    i = 12345

print(Myclass.i)

class Complex:
    def __init__(self,realpart,imagepart):
        self.r = realpart
        self.i = imagepart

x = Complex(3.0,-4.5)
print(x.r, x.i)


