class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        return self.Pow(x, n)
    def Pow(self,x,n):
        ans = 1
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.Pow(x*x,n//2)
        else:
            return x*self.Pow(x,n-1)