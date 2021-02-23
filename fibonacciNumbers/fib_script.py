# import sys

fib_nums = [1, 1]

def fib(n):
    if n < 2:
        return 1
    if n > len(fib_nums):
        return fib(n - 2) + fib(n - 1)
    elif n == len(fib_nums):
        fib_nums.append(fib_nums[n - 2] + fib_nums[n - 1])
    return fib_nums[n]

try:
    user_data = int(input("enter fibbonacci number: "))
    print("Your number is:", fib(user_data))
except:
    print("Invalid input!")