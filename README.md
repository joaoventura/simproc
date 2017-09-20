# The simple microprocessor

The "simple microprocessor" is a test-driven development approach to the implementation of a model of a very basic microprocessor in Python 3. It's purpose is to illustrate the basic components of a hardware microprocessor, such as simple instructions, memory, registers and the instruction pointer.

Here's a very simple program to add two numbers in memory positions [0] and [1].

```
    MOV 0, 5 
    MOV 1, 3
    INC 0
    DEC 1
    MOV r0, [1]
    JNZ 2
    MOV r0, [0]
```

Basically, it keeps incrementing by one the value in memory position [0] and decrementing by 1 the value in memory position [1] until value in [1] reaches zero. At that point [0] has the sum of both values.

You can find other runnable programs in samples.py, and the tests in tests.py. Check the default "assembly" program in simproc.py main function.