class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ds = []
        def K(nums,d,ds):
            if len(d) == len(nums):
                ds.append(d[:])
                return
            for i in range(len(nums)):
                if nums[i] in d:
                    continue
                d.append(nums[i])
                K(nums,d,ds)
                d.pop()
        K(nums,[],ds)
        return ds
        