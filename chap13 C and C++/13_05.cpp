/*

What is the significance of the keyword "volatile" in C?

Intended to prevent the compiler from applying certain optimizations
which it might have otherwise applied because ordinarily it is assumed
variables cannot change values "on their own".

Because the value can change unexpectedly, the compiler will therefore
reload the value each time from memory.

Thus made available of,

- allow access to memory mapped devices.
- allow uses of variables between setjmp and longjmp.
- allow uses of sig_atomic_t variables in signal handlers.

*/
