# # Exercise 1.1
# import math
# # I use binary search to solve this problem


# def binary_search(s):

#     l = 0
#     r = s

#     while (r > l + 1):
#         mid = l + math.floor((r - l) / 2)
#         res = mid * (1 + mid) / 2
#         if (res <= s):
#             l = mid
#         elif (res > s):
#             r = mid

#     return l


# s = int(input("Please enter s : "))
# print(binary_search(s))

# Exercise 1.2

# s = int(input("Enter the s :"))

# for i in range(0, s):
#     for j in range(0, i + 1):
#         print("*", end='')
#     if (i != s - 1):
#         print("\n")

# Fibonacci
import time
start_time = time.time()


# def Fibonacci(n):
#     if (n == 1 or n == 2):
#         return 1
#     return Fibonacci(n - 1) + Fibonacci(n - 2)


# n = int(input("Please input n : "))

# lst = [0, 1]

# for i in range(2, n + 1):
#     sum = lst[i - 1] + lst[i - 2]
#     lst.append(sum)
# print(lst[n])
# print(Fibonacci(n))

n = input("please enter n : ")
k = int(input("please enter k : "))


def super_digit(x):
    if (len(str(x)) == 1):
        return x
    sum = 0
    for i in range(0, len(str(x))):
        sum += int(str(x)[i])
    return super_digit(sum)


s = ""
for i in range(0, k):
    s += n

print(super_digit(int(s)))

end_time = time.time()
print(end_time - start_time)
