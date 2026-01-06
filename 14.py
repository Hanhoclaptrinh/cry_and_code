class Solution:
    def longestCommonPrefix(self, strs):
        if not str: return ""

        pr=strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(pr):
                pr=pr[:-1]
                if not pr: return ""
        return pr