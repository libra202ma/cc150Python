from ffilib import ffilib

ffi, lib = ffilib("1_2")


def test_reverse():
    s = "haha"
    sc = ffi.new("char []", s)
    lib.reverse(sc)
    assert ffi.string(sc) == s[::-1]
