"""
I: int a, b, c
O: int h, m
Constraints: 0 ≤ a ≤ 23, 0 ≤ b ≤ 59, 0 ≤ c ≤ 1,000
Edge Cases:
1. b+c >= 60 -> 2. a = 23 -> 3. 2시간 이상일 때
"""

"""
틀린 풀이
a, b = input().split()
c = int(input())
a = int(a)
b = int(b)

end_h = a
end_m = b+c

if end_m >= 60:
    share = end_m//60
    if end_h == 23:
        end_h = 0
        if share >= 2:
            end_h = end_h + share - 1
    else:
        end_h = share + a
    end_m = end_m%60

print(end_h, end_m)
"""
a, b = input().split()
c = int(input())
a = int(a)
b = int(b)

c_h = c//60
c_m = c%60

end_h = a + c_h
end_m = b + c_m

if end_m >= 60:
    end_h += 1
    end_m -= 60
if end_h >= 24:
    end_h -= 24

print(end_h, end_m)