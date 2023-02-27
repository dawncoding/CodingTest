"""
I: int n
O: *
C: 1 <= N <= 100
"""
n = int(input())
num = 1
for i in range(n):
    print("*"*num)
    num += 1