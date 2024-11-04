class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort the array to handle duplicates
        res = []

        def F(ds, arr, start, n, k):
            if k == 0:
                res.append(list(ds))
                return
            
            for i in range(start, n):
                # Skip duplicates by ensuring we don't pick the same element twice at the same level
                if i > start and arr[i] == arr[i - 1]:
                    continue
                # If the current element exceeds the target, break the loop (since the array is sorted)
                if arr[i] > k:
                    break
                # Add the current element and call the function recursively
                ds.append(arr[i])
                F(ds, arr, i + 1, n, k - arr[i])
                ds.pop()  # Backtrack to explore other combinations

        F([], candidates, 0, len(candidates), target)
        return res
