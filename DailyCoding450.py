# 450
# This problem was asked by Google. (is also #142)
#
# You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.
#
# For example, (()* and (*) are balanced. )*( is not balanced.

def check_balancing(str):
    s1 = []
    s2 = []
    s3 = []
    b1 = b2 = b3 = True

    for x in str:
        if x == "(":
            if b1:
                push(s1, x)
            if b2:
                push(s2, x)
            if b3:
                push(s3, x)
        elif x == ")":
            if pop(s1) is None:
                b1 = False
            if pop(s2) is None:
                b2 = False
            if pop(s3) is None:
                b3 = False
        else:
            if b1:
                push(s1, "(")
            if pop(s2) is None:
                b2 = False

    if b1 and check_empty(s1):
        # print("s1 is empty")
        return True
    if b2 and check_empty(s2):
        # print("s2 is empty")
        return True
    if b3 and check_empty(s3):
        # print("s3 is empty")
        return True

    # print(s1)
    # print(s2)
    # print(s3)
    return False


def check_empty(stack):
    return len(stack) == 0


# Adding items into the stack
def push(stack, item):
    stack.append(item)
    # print("pushed item: " + item)


# Removing an element from the stack
def pop(stack):
    if check_empty(stack):
        return None
    return stack.pop()


print(check_balancing("(()*"))
print(check_balancing("(*)"))
print(check_balancing(")*("))



###########################
# Solutions from Daily
# https://www.dailycodingproblem.com/solution/450?token=8da594094867e4e705d565ca74d7c95133524a72289d08d84f8f21a28baf8f3e0e54cf4a
#
# Solution 1: Brute force
# def balanced(s, count=0):
#     if not s and count == 0:
#         return True
#
#     c = count
#     for i, char in enumerate(s):
#         if char == '(':
#             c += 1
#         elif char == ')':
#             c -= 1
#         elif char == '*':
#             return balanced(s[i + 1:], c) or balanced(s[i + 1:], c + 1) or balanced(s[i + 1:], c - 1)
#
#         if c < 0:
#             return False
#
#     return c == 0
#
# Solution 2:
# def balanced(s):
#     low = 0
#     high = 0
#     for char in s:
#         if char == '(':
#             low += 1
#             high += 1
#         elif char == ')':
#             low = max(low - 1, 0)
#             high -= 1
#         elif char == '*':
#             low = max(low - 1, 0)
#             high += 1
#
#         if high < 0:
#             return False
#     return low == 0

