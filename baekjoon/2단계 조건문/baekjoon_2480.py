"""
I: int first, second, third
O: int price
C: first, second, third: 1~6
E: 

if 같은 눈 3개:
    10000+(같은 눈)*1000
elif 같은 눈이 2개만 나오는 경우:
    1000+(같은 눈)*100
elif 모두 다른 눈이 나오는 경우:
    (그 중 가장 큰 눈)*100
"""

first, second, third = map(int, input().split())

if first == second and second == third:
    price = 10000+first*1000
elif first == second and second != third:
    price = 1000+first*100
elif first == third and first != second:
    price = 1000+first*100
elif second == third and second != first:
    price = 1000+second*100
else: # 모두 다른 눈이 나오는 경우
    if first > second:
        if first > third:
            price = first*100
        else:
            price = third*100
    else: # first < second
        if second > third:
            price = second*100
        else:
            price = third*100

print(price)

