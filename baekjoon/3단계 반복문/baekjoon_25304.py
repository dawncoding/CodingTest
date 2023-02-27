"""
I: sum_price - 영수증에 적힌 총 금액 / kind - 영수증에 적힌 구매한 물건의 종류의 수 / num, price 한 물건의 개수와 가격
O: 
Constraints: 1 <= sum_price <= 1,000,000,000, 1 <= kind <= 100, 1 <= price <= 1,000,000, 1 <= num <= 10
Edge Cases:
"""
sum_price = int(input())
kind = int(input())
result = 0 # sum_price와 비교할 계산 결과를 나타내는 변수

for i in range(kind): # 물건의 종류의 개수만큼 반복문 실행
    price, num = map(int, input().split()) # 물건의 가격과 개수 입력
    result += price * num
    
if result == sum_price:
    print("Yes")
else:
    print("No")