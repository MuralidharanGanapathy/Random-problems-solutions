def dividetwo(num):
    while num % 2 == 0:
        num /= 2
    return num
def dividethree(num):
    while num % 3 == 0:
        num /= 3
    return num
def dividefive(num):
    while num % 5 == 0:
        num /= 5
    return num
def grossnumber(num):
    num = dividetwo(num)
    num = dividethree(num)
    num = dividefive(num)
    if num == 1:
        return 1
    else:
        return 0
for _ in range(int(input())):
    n = int(input())
    count = 1
    i = 1
    while n > count:
        i += 1
        if grossnumber(i):
            count += 1
    print(i)
            