



#
# Complete the 'conflictInfo' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY meetings as parameter.
#
from datetime import time

time = time.time(24,00)
duration = time.time('%M')
timestamp = time.strftime('%H, %M')

def conflictInfo(meetings):
    # Write your code here
    time1 = time.format(8,45)
    time2 = time.format(8,30)
    
    result = []
    for meets in meetings:
        if meets == time1 and duration < 15:
            return "error"
        elif meets > time2 and duration > 15:
            return result = timestamp, duration


if __name__ == '__main__': 

meetings_count = int(input().strip())

    meetings = []

    for _ in range(meetings_count):
        meetings_item = input()
        meetings.append(meetings_item)

    result = conflictInfo(meetings)

    fptr.write(result + '\n')

    fptr.close()
