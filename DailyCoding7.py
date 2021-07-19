# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, … z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message ‘111’ would give 3, since it could be decoded as ‘aaa’, ‘ka’, and ‘ak’.
#
# You can assume that the messages are decodable. For example, ‘001’ is not allowed.
#

def check_mapping(s):
    tmp = int(s)
    if (tmp >=1) and (tmp<=26):
        return True
    else:
        return False

def number_of_way(s, l):
    if l > 1:
        # first_charactor = s[0]
        first_two_charactor = s[0:2]
        if check_mapping(first_two_charactor):
            return number_of_way(s[1:], l-1) + number_of_way(s[2:], l-2)
        else:
            return 1
    else:
        return 1


print(number_of_way("111", 3))
print(number_of_way("1111", 4))
print(number_of_way("123456", 6))
print(number_of_way("123", 3))
print(number_of_way("456", 3))
