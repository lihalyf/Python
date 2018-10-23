# -*- coding: utf-8 -*-
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        result = []
        if nums == None:
            return result
            
        nums = sorted(nums)
            
        self.dfs(nums, 0, [], result)
        return result
        
    def dfs(self, S, startIndex, subset, result):
        result.append(list(subset)) #深度拷贝
        
        for i in range(startIndex, len(S)):
            if i!= 0 and S[i] == S[i - 1] and i > startIndex: #同一层开始的相同值，取最左边的，跳过相邻的相同值
                continue
            
            subset.append(S[i]) #取当前值
            self.dfs(S, i + 1, subset, result)
            subset.pop() #不取当前值，回溯
        
        return result

