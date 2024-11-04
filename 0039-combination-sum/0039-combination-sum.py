class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def dfs(i, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target or i >= len(candidates):
                return
            comb.append(candidates[i])
            dfs(i, comb, total + candidates[i])
            comb.pop()
            dfs(i + 1, comb, total)
        
        dfs(0, [], 0)
        return res
