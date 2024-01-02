# Exercise 1.1
import math


class Triangle(object):
    def __init__(self, a, b, c):
        if a < 1 or b < 1 or c < 1 or a + b <= c or a + c <= b or b + c <= a:
            raise Exception("Invalid Triangle")
        self.firstEdge = a
        self.secondEdge = b
        self.thirdEdge = c

    def check_triangle(self):
        self.p = (self.firstEdge + self.secondEdge + self.thirdEdge) / 2
        self.a = math.pow(
            self.p
            * (self.p - self.firstEdge)
            * (self.p - self.secondEdge)
            * (self.p - self.thirdEdge),
            1 / 2,
        )


a1 = int(input("Please enter edge a for 1st triangle : "))
b1 = int(input("Please enter edge b for 1st triangle : "))
c1 = int(input("Please enter edge c for 1st triangle : "))
tri1 = Triangle(a1, b1, c1)
tri1.check_triangle()
print("Exercise 1.3")
print(f"Area of the triangle : {tri1.a}")
a2 = int(input("Please enter edge a for 2st triangle : "))
b2 = int(input("Please enter edge b for 2st triangle : "))
c2 = int(input("Please enter edge c for 2st triangle : "))
tri2 = Triangle(a2, b2, c2)
tri2.check_triangle()
print(f"Area of the second triangle : {tri2.a}")

if tri1 != 0 and tri2 != 0:
    if tri1.a == tri2.a:
        print(
            f"Area of triangle 1 ({tri1.a}) and area of triangle 2 ({tri2.a}) is equal"
        )
    elif tri1.a < tri2.a:
        print(
            f"Area of triangle 1 ({tri1.a}) is smaller than area of triangle 2 ({tri2.a})"
        )
    elif tri1.a > tri2.a:
        print(
            f"Area of triangle 1 ({tri1.a}) is bigger than area of triangle 2 ({tri2.a})"
        )
else:
    if tri1.a == 0:
        print("First triangle is invalid")
    if tri2.a == 0:
        print("Second triangle is invalid")
