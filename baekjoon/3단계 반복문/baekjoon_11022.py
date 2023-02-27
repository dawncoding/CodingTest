"""
I: int T - 테스트 케이스 개수 / int a, b
O: "Case #x: a + b = c" 형식으로 출력
C: 0 < A, B < 10
"""
T = int(input())
case = 1
for i in range(T):
    a, b = map(int, input().split())
    print("Case #%d: %d + %d = %d" %(case, a, b, a+b))
    case += 1