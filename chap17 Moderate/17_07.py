"""
Given any integer, print an English phrase that describes the
integer (e.g., "One Thousand, Two Hundred Thirty Four").

"""

def printNum(n):
    numStr = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen",
        20: "Twenty",
        30: "Thirty",
        40: "Forty",
        50: "Fifty",
        60: "Sixty",
        70: "Seventy",
        80: "Eighty",
        90: "Ninety",
    }

    scaleStr = {
        100: "Hundred",
        1000: "Thousand",
        1000000: "Million",
        1000000000: "Billion",
    }

    # 1 ~ 20
    if n in numStr:
        return numStr[n]

    # < 100
    if n < 100:
        return numStr[n // 10 * 10] + " " + numStr[n % 10]

    # > 100
    ret = ""
    for scale in [1000000000, 1000000, 1000, 100]:
        if n < scale:
            continue
        ret = printNum(n // scale) + " " + scaleStr[scale] + " " + \
            printNum(n % scale)
        n //= scale
    return ret


def test_printNum():
    assert printNum(7) == "Seven"
    assert printNum(77) == "Seventy Seven"
    assert printNum(77777) == \
        "Seventy Seven Thousand Seven Hundred Seventy Seven"
