# This problem was asked by Facebook.
#
# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters. For example, given "hello/world:here", return "here/world:hello"
#
# Follow-up: Does your solution work for the following cases: "hello/world:here/", "hello//world:here"

def reverse_string_keep_order(mystr: str) ->str:
    lstStr = mystr.split("/")
    strRev = ""
    for word in lstStr:
        strRev += reverse_word(word) + "/"
        # print(strRev)
    return strRev[:len(strRev)-1]

def reverse_word(mystr: str) ->str:
    if len(mystr) == 0:
        return ""
    else:
        return mystr[::-1]


if __name__ == "__main__":
    print(reverse_string_keep_order("hello/world:here/"))
    # print(reverse_string_keep_order("hello//world:here"))