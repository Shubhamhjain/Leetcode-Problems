class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charS=set()
        l=0
        max_len=0

        for r in range(len(s)):
            while(s[r] in charS):
                charS.remove(s[l])
                l+=1

            charS.add(s[r])
            max_len = max(max_len,r-l+1)
        return max_len