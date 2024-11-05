class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        d = []
        ds = []
        def F(nums,start,d,ds):
            if start == len(nums):
                ds.append(d) if d not in ds else None
                return
            F(nums,start+1,d+[nums[start]],ds)
            F(nums,start+1,d,ds)
        F(sorted(nums),0,d,ds)
        return sorted(ds)
        