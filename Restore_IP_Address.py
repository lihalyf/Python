"""
426. Restore IP Addresses
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example
Given "25525511135", return

[
  "255.255.11.135",
  "255.255.111.35"
]
Order does not matter.
"""

class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        if s == None:
            return None
        result =[]
        self.dfs(s, [], result, 0)
        dic = {}
        for r in result:
            if r in dic:
                continue
            dic[r] = 1
        return dic.keys()
        
    def dfs(self, s, subset, result, level):
        if len(s) == 0:
            if level == 4:
                string = "".join(subset)
                return result.append(string)
            else:
                return
        
        for i in range(1, 4):
            prefix = s[:i]
            if int(prefix) > 255:
                continue
            if len(prefix) > 1 and prefix[0] == '0':
                continue
            if level == 3:
                subset.append(prefix)
            else:
                subset.append(prefix + '.')
            self.dfs(s[i:], subset, result, level + 1)
            subset.pop()
        
    
