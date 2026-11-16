def findsumofremainders(n,div):
    total = 0
    for i in range(1,n+1):
        total += i%div
    return total