"""
I: int 시험점수
O: string 시험성적
Constraints: 시험점수 >= 0 && 시험점수 <= 100
"""

score = int(input())

if score >= 90 and score <= 100:
    print("A")
elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")