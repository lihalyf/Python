def hw4():
    nums = [1, 2, 3, 4, 5]
    result = []
    dfs(nums, 5, 1, [], result)
    return len(result)
    
def dfs(S, k, level, subset, result):
    if k == 0:
        return result.append(list(subset))   
    for i in range(len(S)):
        if S[i] in subset or level == S[i]:
            continue
        subset.append(S[i])
        dfs(S, k - 1, level + 1, subset, result)
        subset.pop()
r = hw4()
print(r)
        