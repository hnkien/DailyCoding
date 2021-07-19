# find missing element in 2 list
# [4,12,9,6,3]
# [4,9,12,6]
# result = 3

def find_missing(full_set, partial_set):
    missing_items = set(full_set) - set(partial_set)
    return list(missing_items)[0]


def find_missing_xor(full_set, partial_set):
    xor_sum = 0
    for num in full_set:
        xor_sum ^= num
    for num in partial_set:
        xor_sum ^= num
    return xor_sum


print(find_missing([4,12,9,6,3], [4,9,12,6]))

print(find_missing_xor([4,12,9,6,3], [4,9,12,6]))