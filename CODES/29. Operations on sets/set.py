"""
          unique | order | changing specific el. | new elements
LISTS         N      Y             Y                   Y 
TUPLES        N      Y             N                   N
DICT          Y      N             Y                   Y
SETS          Y      N             N                   Y

        SETS have BONUS operations: | & - ^
        | - UNION
        & - intersection
        - - difference
        ^ - XOR eXlusive OR (removing intersection from union)
"""

A = {-2, 10, 40, 20}
B = {-2, 10}

print(B.issubset(A))

