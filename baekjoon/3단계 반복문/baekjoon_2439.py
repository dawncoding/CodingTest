n = int(input())
num = 1
space = n-1
for i in range(n):
    print(" "*space+"*"*num)
    num += 1
    space -= 1