import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = []
        s = s.lower()
        alphabet = set(string.ascii_lowercase)
        numbers = {'0','1','2','3','4','5','6','7','8','9'}

        for char in s:
            if (char in alphabet or char in numbers):
                clean_s.append(char)
        pt1 = 0 
        pt2 = len(clean_s) - 1
        
        for i in range(len(clean_s)):
            if (clean_s[pt1] != clean_s[pt2]):
                return False
            pt1 += 1
            pt2 -= 1

        return True