"""
Input: int n
Output: int sum - 1부터 n까지의 합
Constraints: 1 ≤ n ≤ 10,000
"""
n = int(input())
a = 1
sum = 0

for i in range(n):
    sum += a
    a += 1

print(sum)