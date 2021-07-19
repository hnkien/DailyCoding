def lengthOfLongestSubstring(s: str) -> int:
    l = len(s)
    if l == 0:
        return 0
    elif l == 1:
        return 1
    else:
        # print("Len: ", l)
        i = 0
        max_at = [1] * l

        max_substr_len = 1

        while i < l-max_substr_len+1:
        # while i < l:
            temp_list = []
            temp_list.append(s[i])
            j = i+1
            while j<l:
                if s[j] in temp_list:
                    max_at[i] = j-i
                    break
                else:
                    max_at[i] += 1
                    temp_list.append(s[j])
                j += 1

            if max_substr_len < max_at[i]:
                max_substr_len = max_at[i]

            # print("max at ", i, " : ", max_at[i] )

            i += 1

        return max_substr_len

print (lengthOfLongestSubstring("abcbdabdc"))