"""
I: int t 테스트 케이스 개수 / int a, b 계산할 테스트 케이스
O: a+b
C: 0 < A, B < 10
"""

"""
틀린 풀이
testcase = int(input())
i=1

while i == testcase:
    a, b = map(int, input().split())
    print(a+b)
    i += 1
"""
testcase = int(input())

for i in range(testcase):
    a, b = map(int, input().split())
    print(a+b)
