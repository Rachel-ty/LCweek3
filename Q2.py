class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        ans=1
        n=len(s)
        start=0
        end=1
        while end<n:
            if s[end] in s[start:end]:
                idx=s[start:end].index(s[end])+start
                ans=max(ans,end-start)
                start=idx+1
            end+=1
        ans=max(ans,end-start)
        return ans

        