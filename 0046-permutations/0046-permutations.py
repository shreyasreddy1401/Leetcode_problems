class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ds = []
        def K(nums,start,d,ds):
            if start == len(nums):
                ds.append(nums[:])
                return
            for i in range(start,len(nums)):
                nums[i],nums[start] = nums[start],nums[i]
                K(nums,start+1,d,ds)
                nums[i],nums[start] = nums[start],nums[i]

        K(nums,0,[],ds)
        return ds
        