def expand (s, left, right):

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return s[left+1:right]

def get_pal(s):

    result = ""

    for i in range (len(s)):

        center_odd = expand(s, i, i)
        center_even = expand(s, i, i+1)

        if len(center_odd) > len(result):
            result = center_odd

        if len(center_even) > len(result):
            result = center_even

    return result

print(get_pal("baabaaa"))