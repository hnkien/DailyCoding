# Room meeting Problem 1
# Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.
#
# For example,
# Given [ [0, 30], [5, 10], [15, 20] ],
# return false.


def room_meeting_1(arr):
    brr = sorted(arr, key=lambda x: x[0])
    n = len(brr)
    end_time = brr[0][1]
    i = 1
    while i<n:
        if end_time > brr[i][0]:
            return False
        else:
            end_time = brr[i][1]
            i += 1


# print(room_meeting_1([[0, 30], [5, 10], [15, 20]]))


# Room Meeting Problem 2
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...]
# find the minimum number of conference rooms required.

# Solution:
# When a room is taken, the room can not be used for anther meeting until the current meeting is over.
# As soon as the current meeting is finished, the room can be used for another meeting.
# We can sort the meetings by start timestamps and sequentially assign each meeting to a room.
# Each time when we assign a room for a meeting, we check if any meeting is finished so that the room can be reused.
# In order to efficiently track the earliest ending meeting, we can use a min heap.
# Whenever an old meeting ends before a new meeting starts, we reuse the room (i.e., do not add more room).
# Otherwise, we need an extra room (i.e., add a room).

import heapq
def room_meeting_2(arr):
    count = 0
    heap = []
    for a in arr:
        if not heap:
            count += 1
            heapq.heappush(heap, a[1])
        else:
            if a[0] >= heap[0]:
                heapq.heappop(heap)
            else:
                count += 1
            heapq.heappush(heap, a[1])

    return count


print(room_meeting_2([[0, 30], [5, 10], [15, 20], [7,15]]))
