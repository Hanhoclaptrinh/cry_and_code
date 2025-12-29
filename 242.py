class Solution:
    def isAnagram(s, t):
        # neu kich thuoc 2 chuoi khac nhau -> false
        if len(s) != len(t): return False

        cnter = [0] * 26 # mang 25 ky tu

        for i in range(lne(s)):
            # dem tan suat xuat hien cua cac ky tu trong 2 chuoi
            cnter[ord(s[i]) - ord('a')] += 1
            cnter[ord(t[i]) - ord('a')] -= 1

        for cnt in cnter:
            if cnt != 0: return False

        return True