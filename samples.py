"""
 Sample programs for the simple microprocessor

"""

"""
Adds the values in memory positions 0 and 1 and sets r0.
It keeps INC [0] and DEC [1] until value in [1] is zero.
"""
add_values = """
    MOV 0, 5 
    MOV 1, 3
    INC 0
    DEC 1
    MOV r0, [1]
    JNZ 2
    MOV r0, [0]
"""


"""
Sets in r0 the maximum value of memory positions 0 and 1
It copies the values in [0] and [1] to [2] and [3] to keep the originals.
Then it keeps decreasing values in [2] and [3] until one of them reaches zero
The first to reach zero is the minimum, while the other is the maximum.
"""
max_value = """
    MOV 0, 8 
    MOV 1, 5
    MOV 2, [0]
    MOV 3, [1]
    DEC 2
    DEC 3
    MOV r0, [2]
    JZ 11
    MOV r0, [3]
    JZ 13
    JMP 4
    MOV r0, [1]
    JMP 14
    MOV r0, [0]
"""
