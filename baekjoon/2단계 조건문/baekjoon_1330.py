"""
I: int a, b
O: string 비교 결과
Constraints: -10,000 ≤ A, B ≤ 10,000
"""

a, b = input().split()
a = int(a)
b = int(b)

if a>b:
    print('>')
elif a<b:
    print('<')
elif a==b:
    print('==')