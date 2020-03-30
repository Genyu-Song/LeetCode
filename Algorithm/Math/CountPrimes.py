# -*- coding: UTF-* -*-

'''
Count the number of prime numbers less than a non-negative number, n.
'''

class Solution:
    def countPrimes(self, n: int) -> int:
        def is_primes(i):
            for j in range(2, i):
                if i % j == 0:
                    return False
            return True

        res = 0
        for i in range(2, n):
            if is_primes(i):
                res += 1
        return res


class Solution2: # 逆向排除法
    def countPrimes(self, n: int) -> int:
        is_prime = [True for _ in range(n)]
        for i in range(2, int(pow(n, 0.5)) + 1): # 优化
            if is_prime[i]:
                j = i ** 2
                while j < n:
                    is_prime[j] = False
                    j += i
        res = is_prime[2:].count(True)
        return res

if __name__ == '__main__':
    print(Solution2().countPrimes(n=10))