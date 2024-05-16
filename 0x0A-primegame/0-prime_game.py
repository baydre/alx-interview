#!/usr/bin/python3
"""
alx-interview: Prime Game

the goal is to determine
who the winner of each game is...
"""


def sieve(n):
    """
    Helper function to perform
    the Sieve of Eratosthenes
    and return primes up to n.
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p] is True:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_numbers = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_numbers


def isWinner(x, nums):
    """
    returns: name of the player that won the most rounds
    """
    if not nums or x <= 0:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        turn = 0  # 0 for Maria, 1 for Ben
        remaining_numbers = set(range(1, n + 1))
        prime_index = 0

        while True:
            while prime_index < len(primes) \
                    and primes[prime_index] not in remaining_numbers:
                prime_index += 1

            if prime_index == len(primes) or primes[prime_index] > n:
                break

            prime = primes[prime_index]
            multiples = set(range(prime, n + 1, prime))
            remaining_numbers -= multiples

            if not remaining_numbers.intersection(primes):
                break

            turn = 1 - turn

        if turn == 1:  # Maria made the last move
            maria_wins += 1
        else:  # Ben made the last move
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
