class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ds = []
        def K(nums,start,d,ds):
            ds.append(d[:])
            for i in range(start,len(nums)):
                if i != start and nums[i] == nums[i-1]:
                    continue
                d.append(nums[i])
                K(nums,i+1,d,ds)
                d.pop()
        K(nums,0,[],ds)
        return ds
        