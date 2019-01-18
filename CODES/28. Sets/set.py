"""
          unique | order | changing specific el. | new elements
LISTS         N      Y             Y                   Y 
TUPLES        N      Y             N                   N
DICT          Y      N             Y                   Y
SETS          Y      N             N                   Y

        SETS have BONUS operations: | & - ^ 
"""

A = {40, -2, 20, 13, 40, 20}

A.remove(200)
print(A)
