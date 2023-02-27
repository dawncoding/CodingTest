"""
I: int x, y
O: int 사분면 번호
Constraints: −1000 ≤ x ≤ 1000; x ≠ 0 / −1000 ≤ y ≤ 1000; y ≠ 0
"""

x = int(input())
y = int(input())

if x>0 and y>0:
    print(1)
elif x<0 and y>0:
    print(2)
elif x<0 and y<0:
    print(3)
else:
    print(4)