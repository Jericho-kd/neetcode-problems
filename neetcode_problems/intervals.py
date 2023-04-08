# 252. Meeting Intervals (easy)
def meeting_intervals(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
