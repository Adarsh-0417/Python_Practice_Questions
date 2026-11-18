class Solution:
    def print_divisors(self, n):
        arr = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                arr.append(i)

                if i != n // i:
                    arr.append(n // i)

        arr.sort()
        return arr