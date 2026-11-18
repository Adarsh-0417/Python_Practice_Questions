
class Solution:
    def primeRange(self, l, r):
        is_prime = [True] * (r + 1)

        is_prime[0] = False
        is_prime[1] = False

        for i in range(2, int(r**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, r + 1, i):
                    is_prime[j] = False

        arr = []

        for i in range(l, r + 1):
            if is_prime[i]:
                arr.append(i)

        return arr
