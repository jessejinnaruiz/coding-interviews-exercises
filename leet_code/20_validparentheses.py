# class Solution:
def isValid(s: str) -> bool:
    list_str = list(s)
    print(list_str)
    print(list_str.index(")"))
    print(list_str.index("("))

    
    #second test for the correct ordering of the brackets.
    s1 = ")"
    s2 = "}"
    s3 = "]"

    if s1 in list_str:
        if list_str.index(s1) > list_str.index("("):
            return True
        else:
            return False
    elif s2 in list_str:
        if list_str.index(s2) < list_str.index("{"):
            return False
        elif list_str.index(s2) > list_str.index("{"):
            return True
    elif s3 in list_str:
        if list_str.index(s3) < list_str.index("["):
            return False
        elif list_str.index(s3) > list_str.index("["):
            return True
    else:
        return True      
    #first check the count of the brackets in the string. If its an odd count, 
    #then return False because there should always be an even count of each type of bracket.
    for element in list_str:
        if list_str.count(element) % 2 != 0:
            return False
        else: 
            continue

test1 = "()[]{}"
test2 = "([)]"


print(isValid(test1))
print(isValid(test2))