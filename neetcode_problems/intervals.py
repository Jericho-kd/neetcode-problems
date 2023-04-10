# 252. Meeting Intervals (easy)
def meeting_intervals(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        print(i)
        if intervals[i][0] > intervals[i-1][1]:
            continue
        else:
            return False
        
    return True
