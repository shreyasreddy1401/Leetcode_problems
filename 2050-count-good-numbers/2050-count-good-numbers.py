class Solution:
    mod = int(1e9 + 7)

    def solve(self, x, n):
        if n == 0:
            return 1

        if n % 2 == 0:
            return self.solve((x * x) % self.mod, n // 2)
        else:
            return (x * self.solve(x, n - 1)) % self.mod

    def countGoodNumbers(self, n):
        even = n // 2 + n % 2
        odd = n // 2
        first = self.solve(5, even)
        second = self.solve(4, odd)

        ans = (first * second) % self.mod
        return ans

