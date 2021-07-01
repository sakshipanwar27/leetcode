class Solution(object):

    def isPrime(self, Number):
        return 2 in [Number, 2**Number % Number]

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count_prime = 0
        prime_range = filter(lambda x: x % 2 != 0 and x % 3 != 0 and x % 5 != 0, xrange(n))

        for i in prime_range:
            if self.isPrime(i):
                count_prime += 1

        return count_prime

print Solution().countPrimes(499979)