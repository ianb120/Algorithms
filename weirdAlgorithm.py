# weird algorithm
# even numbers are divided by two
# odd numbers are multiplied by 3 and add 1

# number input
n = 3

while n != 1:
    # even nums
    if n %2 == 0:
        n = n // 2
    
    # odd nums
    else:
        n = (n * 3) + 1
    
    print(n)
