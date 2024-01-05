#Count minimum number of fountains to be activated to cover the entire garden
#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fountainActivation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY locations as parameter.
#

def fountainActivation(locations):
    n = len(locations)
    min_fountains = float('inf')
    for i in range(1, 2**n):
        activated = []
        for j in range(n):
            if (i >> j) & 1:
                activated.append(j)
        if is_covered(activated, locations):
            min_fountains = min(min_fountains, len(activated))
    return min_fountains
 
def is_covered(activated, fountains):
    n = len(fountains)
    coverage = [0] * n
    for i in activated:
        left = max(0, i - fountains[i])
        right = min(n - 1, i + fountains[i])
        for j in range(left, right + 1):
            coverage[j] = 1
    return all(coverage)
