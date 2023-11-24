s = input("Enter a list of integers separated by space : ")

lst = s.split()

lst = [int(num) for num in lst]

print(f"The total number of items in the list : {len(lst)}")
print(f"The last element of the list is {lst[-1]}")
print(f"The reversed order of the list is : {[num for num in reversed(lst)]}")

print("Check if there is element 5 in the list...\n")
if (lst.count(5) > 0):
    print("Yes\n")
else:
    print("No\n")

print(f"The number of elements 5 in the list is : {lst.count(5)}")

lst = lst[1:len(lst) - 1]
print(f"List after the first and last element removed : {lst}")

print(f"The largest element in the list is : {max(lst)}")
print(f"The smallest element in the list is : {min(lst)}")
