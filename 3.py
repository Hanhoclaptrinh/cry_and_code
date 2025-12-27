class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        charSet = set()
        left = 0
        maxLen = 0

        for right in range(n):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            charSet.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen