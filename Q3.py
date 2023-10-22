class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m=len(s)
        n=len(t)
        if m<n:
            return ""
        hmap=Counter(t)
        rem=defaultdict(int)
        def isValid(rem):
            cnt=0
            for i,j in rem.items():
                if i in hmap and j>=hmap[i]:
                    cnt+=1
            if cnt==len(hmap):
                return True
            return False
        min_val=inf
        start=-1
        end=-1
        l=0
        r=0
        for r,r_val in enumerate(s):
            rem[r_val]=rem[r_val]+1
            while l<=r and isValid(rem):
                if min_val>r-l+1:
                    min_val=r-l+1
                    start=l
                    end=r
                rem[s[l]]-=1
                l+=1
        return s[start:end+1]