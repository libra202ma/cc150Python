/*

You are given a class with synchronized method A and a normal method B. If you have two threads in one instance of a program, can they both execute A at the same time? Can they execute A and B at the same time?

 */


/*

If A is not static
    If same object
        - execute A at the same time, NO
        - execute A and B at the same time, YES
    else
        - execute A at the same time, YES
        - execute A and B at the same time, YES
else   # A is static
    If same object
        - execute A at the same time, NO
        - execute A and B at the same time, NO
    else
        - execute A at the same time, YES
        - execute A and B at the same time, YES

 */
