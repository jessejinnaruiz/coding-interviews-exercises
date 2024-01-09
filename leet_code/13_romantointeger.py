# class Solution:
def romanToInt(s: str) -> int:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    special_values = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 500, "CM": 900}
    counter = 0
    s_list = list(s.strip())
    print(s_list)
    found_specials = []

    # in the case when a whole string is not in the special values list, then...
    if s not in special_values:
        # either there are no special values found at all, in which case, do the below code.
        if s not in special_values: 
            # separate every individual string in the list and then find their associated value
            for element in s_list:
                # then count of the values and return it.
                counter = counter + values[element]

            return counter
        # or else, a second scenario is that there are some special values in the string, so we have to find them.
        else:
            # if the string is contained in the special values dict and its not a substring of s, then just return that value
            if len(s) == len(special_values.get(s)):
                return special_values.get(s)
            else:
                # there is a special value in the string, s, so we locate it and put it into a new array
                found_specials.append(special_values.get(s))
                #not sure what to do to finish this...
                print("FOUND SPECIALS....")
                print(found_specials)
                counter = counter
    else:
        # else assume that its not found
        return "Not found"

        
test2 = "LVIII"
test3 = "MCMXCIV"
print(romanToInt("III"))
print(romanToInt(test2))
print(romanToInt(test3))