num1 = int(input())
num2 = int(input())

# 백의 자리 수 구하기
third = num2//100

# 십의 자리 수 구하기
second = (num2%100)//10

# 일의 자리 수 구하기
first = (num2%100)%10


print(num1*first)
print(num1*second)
print(num1*third)
print(num1*num2)