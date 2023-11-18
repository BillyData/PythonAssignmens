from statistics import mean
my_file = open("numbers.txt", "r")
for line in my_file:
    arr = [float(num) for num in line.split(',')]
    print(f"The largest number is : {max(arr)}")
    print(f"The smallest number is : {min(arr)}")
    print(f"The mean number is : {mean(arr)}")

my_file.close()
