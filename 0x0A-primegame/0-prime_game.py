#!/usr/bin/python3
""" Prime game """


def isWinner(x, nums):
    """Determines the winner"""
    if x < 1 or not nums:
        return None
    maria_wins, ben_wins = 0, 0
    n = max(nums)
    prime = [True for _ in range(1, n + 1, 1)]
    prime[0] = False
    for i, is_prime in enumerate(prime, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            prime[j - 1] = False
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, prime[0: n])))
        ben_wins += primes_count % 2 == 0
        maria_wins += primes_count % 2 == 1
    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
