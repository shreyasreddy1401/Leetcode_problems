class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ds = []
        d = []
        def F (nums,start,d,ds):
            if start == len(nums):
                ds.append(d[:])
            else:
                F(nums,start+1,d+[nums[start]],ds)
                F(nums,start+1,d,ds)
        F(nums,0,d,ds)
        return ds