#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'evenSubarray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. INTEGER k
#

def evenSubarray(numbers, k):

    result = 0
    
    # Find sum of all subarrays and
    # increment result if sum is even
    for i in range(0, k, 1):
        sum = 0
        for j in range(i, k, 1):
            sum = sum + numbers[j]
            if (sum % 2 == 0):
                    result = result + 1
    
    return (result)
    

if __name__ == '__main__':
