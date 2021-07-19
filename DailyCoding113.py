# This problem was asked by Google.
#
# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
#
# Follow-up: given a mutable string representation, can you perform this operation in-place?

def reverse_string(mystr: str) ->str:
    # way 1
    # revstr = ""
    # for i in mystr:
    #     revstr = i + revstr
    # return revstr

    # way 2
    # return mystr[::-1]

    # way 3
    return ''.join(reversed(mystr))

if __name__ == "__main__":
    print(reverse_string("hello world here"))