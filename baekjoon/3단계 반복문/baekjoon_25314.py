"""
I: int n
O: 
Constraints: 4 <= n <= 1,000 / n은 4의 배수
"""

n = int(input())
share = n//4 # long 반복 횟수 구하기

for i in range(share):
    print("long", end=" ")

print("int")