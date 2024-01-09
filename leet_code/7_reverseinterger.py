# class Solution:
def reverse( x: int) -> int:

    
    # print(rev)
    if x == 0:
        return 0
    elif x < 0:
        x = abs(x)
        rev = list(str(x))
        rev.reverse()
        joined = "".join(rev)
        return int(joined) * -1
    elif x > 0:
        rev = list(str(x))
        rev.reverse()
        joined = "".join(rev)
        return int(joined)
    else:
        "Not possible"

print(reverse(-123))


# to_rev = list(str(123))
# print(to_rev)
# rev_done = to_rev.reverse()
# print(rev_done)