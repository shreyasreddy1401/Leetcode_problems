class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ds = []
        def F(start,k,n,d,ds):
            if len(d) == k:
                ds.append(d[:])
                return
            for i in range(start,n+1):
                d.append(i)
                F(i+1,k,n,d,ds)
                d.pop()
        F(1,k,n,[],ds)
        return ds