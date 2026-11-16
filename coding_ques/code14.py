def CardsPyramid(n):
    if n == 0:
        return -1

    result = (n * (3 * n + 1)) // 2

    return result % 1000007
