# 57
# This problem was asked by Amazon.
#
# Given a string s and an integer k, break up the string into multiple texts such that each text has a length of k or less. You must break it up so that words don't break across lines. If there's no way to break the text up, then return null.
#
# You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.
#
# For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10, you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"]. No string in the list has a length of more than 10.

# Solution 1
# def break_string(s, k):
#     list_words = s.split()
#     list_result = []
#     l = len(list_words)
#     i = 0
#     while i < l:
#         j = i
#         list_append_word = []
#         while j < l:
#             a_word = list_words[j]
#             if len(a_word) > k:
#                 return None
#             else:
#                 if check_length(list_append_word, a_word) <= k:
#                     list_append_word.append(a_word)
#                     j += 1
#                 else:
#                     break
#         i = j
#         list_result.append(list_append_word)
#     return list_result
#
#
# def check_length(list_append_word, a_word):
#     n = len(list_append_word)
#     l1 = 0
#     for word in list_append_word:
#         l1 += len(word)
#     l1 += n
#     l1 += len(a_word)
#     return l1


def break_string(s, k):
    i = j = 0
    m = 0
    l = len(s)
    list_result = []

    while m < l:
        words = ''
        if s[j] == ' ':
            m += 1
        else:
            words += s[j]
            m += 1
        i = m
        j = m
        print(words)
        list_result.append(words)

    return list_result


print(break_string("hello world", 10))
# print(break_string("the quick brown fox jumps over the lazy dog", 10))
# print(break_string("Cong Hoa Xa Hoi Chu Nghia Viet Nam", 7))
