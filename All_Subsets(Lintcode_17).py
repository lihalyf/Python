#version 1 (0, 1 select or not)
import copy
def subsets(nums):
    result = []
    if nums == None:
        return result
    
    subset = []
    nums = sorted(nums)
    dfs(nums, 0, subset, result)
    return result


def dfs(num_list, index, subset, result): # 1. recursion define
    # 2. recursion out
    if index == len(num_list):
        result = result.append(copy.deepcopy(subset)) #deep copy!!! so the result and subset uses different memory to store
        return result
    
    # 3. recursion divide
    ## select current index
    subset.append(num_list[index])
    dfs(num_list, index + 1, subset, result)
    
    ## not select current index
    subset.pop()
    dfs(num_list, index + 1, subset, result)

n = [3,1,2]
r = subsets(n)
print(r)

#version 2

def Subsets(nums):
    result = []
    if nums == None:
        return result
    
    nums = sorted(nums)
    dfs(nums, 0, [], result)
    return result
    
def dfs(num, startIndex, subset, result):
    result.append(list(subset))
    
    while startIndex < len(num):
        subset.append(num[startIndex])
        dfs(num, startIndex + 1, subset, result)
        subset.pop()
        startIndex += 1
    
    return result

n = [3,1,2]
r = Subsets(n)
print(r)