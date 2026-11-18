def minCost(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    min_cost = float('inf')

    for v in vowels:
        cost = 0

        for ch in s:
            cost += abs(ord(ch) - ord(v))

        min_cost = min(min_cost, cost)

    return min_cost
