"""
오답
a, b, c = input().split()
a = int()
b = int()
c = int()

print(a+b+c)
"""
a, b, c = map(int, input().split())
print(a+b+c)