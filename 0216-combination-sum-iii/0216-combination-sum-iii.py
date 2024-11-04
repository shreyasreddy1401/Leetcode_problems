class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        arr = [1,2,3,4,5,6,7,8,9]
        ans=[]
        start = 1

        def F(k,arr,ds,start,n):
            if k == 0 and n == 0:
                ans.append(ds[:])
                return 
            for i in range(start,10):
                if i > n: break
                ds.append(i)
                F(k-1,arr,ds,i+1,n-i)
                ds.pop()
            return

        F(k,arr,[],start,n)
        return ans
 
               