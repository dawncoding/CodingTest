"""
I: int h, m
O: int h, m
Constraints: 0 ≤ H ≤ 23, 0 ≤ M ≤ 59
Edge Cases: m < 45, h = 0
"""
h, m = input().split()
h = int(h)
m = int(m)

alarm_hour = h
alarm_minute = m - 45

if alarm_minute < 0:
    if alarm_hour == 0:
        alarm_hour = 23
    else:
        alarm_hour = alarm_hour - 1
    alarm_minute = 60 + alarm_minute
print(alarm_hour, alarm_minute)
