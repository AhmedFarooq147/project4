def in_range(n, low, high):
    if n >= low and n <= high:
        return True
    return False

n = int(input("enter the value of n : "))
low = int(input("enter the value of low : "))
hi = int(input("enter the value of hi : "))

in_range(n,low,hi)