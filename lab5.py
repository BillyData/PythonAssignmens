from math import sqrt

class List:
    def __init__(self, list):
        self._list = list

    def reverse(self):
        for i in self._list[::-1]:
            yield i

    def check_prime(self):
        prime = []
        for u in self._list:
            if (u == 1):
                continue
            flag = True;
            for i in range(2, int(sqrt(u)) + 1):
                if u % i == 0:
                    flag = False;
            if (flag):
                prime.append(u)

        for u in prime:
            yield u

n = int(input("Input n : "))
s = input("Input n numbers separated by space : ")

l1 = List([int(u) for u in s.split()])

for u in l1.reverse():
    print(u, end = " ")

print()

for u in l1.check_prime():
    print(u, end = " ")

print("\n")
