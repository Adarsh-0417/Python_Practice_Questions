def countsetbits(n):
    return bin(n).count('1')
n=int(input())
print(countsetbits(n))