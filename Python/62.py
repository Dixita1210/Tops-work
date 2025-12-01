# Write a Python function to check whether a number is in a given range


n=int(input('Enter a number - '))
def is_in_range(num, start, end):
    return num in range(start, end + 1)


if is_in_range(n, 1, 10):
    print(f"{n} is in the range 1 to 10")
else:
    print(f"{n} is NOT in the range 1 to 10")


