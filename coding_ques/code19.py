def sumPrimes(L, R):
    is_prime = [True] * (R + 1)

    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(R**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, R + 1, i):
                is_prime[j] = False

    total = 0

    for i in range(L, R + 1):
        if is_prime[i]:
            total += i

    return total
