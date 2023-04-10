import neetcode_problems.intervals as interval_problems


def test_meeting_intervals():
    assert interval_problems.meeting_intervals([[0,30], [5,10], [15,20]]) == False
    assert interval_problems.meeting_intervals([[25,30], [5,10], [15,20]]) == True
    assert interval_problems.meeting_intervals([[7,10], [2,4]]) == True