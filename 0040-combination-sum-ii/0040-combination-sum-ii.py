class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # Sort the array to handle duplicates
        res = []

        def backtrack(start, comb, target):
            if target == 0:
                res.append(list(comb))
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates
                
                # Include the current candidate and move to the next index
                comb.append(candidates[i])
                backtrack(i + 1, comb, target - candidates[i])
                comb.pop()  # Backtrack after exploring this path
        
        backtrack(0, [], target)
        return res
