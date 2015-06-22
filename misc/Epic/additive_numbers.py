from math import sqrt

def getAllAdditiveNumbers(start, end):
    # the number is determined by T0, T1
    for T0 in range(1, int(sqrt(end))):
        for T1 in range(0, int(sqrt(end))):
            num = T0 * 10 ** len(str(T1)) + T1
            while True:
                T2 = T0 + T1
                num = num * 10 ** len(str(T2)) + T2
                if start < num < end:
                    print(num, '\t')
                elif num > end:
                    break
                T0 = T1
                T1 = T2


if __name__ == '__main__':
    getAllAdditiveNumbers(1000, 9999)
