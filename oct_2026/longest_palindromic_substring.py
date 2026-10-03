class Solution:
    def expand(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r +=1
        return s[l+1:r]
        
    def longestPalindrome(self, s: str) -> str:
        longest_substring = ""
        for i in range(len(s)):
            odd = self.expand(s,i,i)
            even = self.expand(s,i,i+1)
            print(odd,even)
            if len(odd) > len(longest_substring):
                longest_substring = odd
            if len(even) > len(longest_substring):
                longest_substring = even
        return longest_substring
