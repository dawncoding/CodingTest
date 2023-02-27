"""
I: int T - 테스트 케이스의 개수 / int a, b
O: "Case #x: " int a+b 결과
C: 0 < A, B < 10
"""
T = int(input())
num = 1
for i in range(T):
    a, b = map(int, input().split())
    print("Case #%d:" %num, a+b)
    num += 1