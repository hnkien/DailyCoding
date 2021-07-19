# This problem was asked recently by Google.
#
# Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)

    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list


print(merge([[1, 3, 5, 7], [2, 4, 6], [1, 2, 4, 8, 10, 12]]))
