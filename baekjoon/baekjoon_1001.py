"""
int(input()).split() 하면 ValueError 발생
"""

a, b = input().split()
a = int(a)
b = int(b)

print(a-b)