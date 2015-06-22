"""
Explain what the following code does: ((n & (n - 1))) == 0).

- Find if n is power of 2. If the equation is evaluated as True, it
means n and n - 1 do not have common bits. Alternatively, for n - 1,
if we add 1 to it, all its bits are flipped. The only possible
situation is n - 1 is all 1s, and n equals to power of 2.
"""
