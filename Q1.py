class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        n=len(s)
        rem=defaultdict(list)
        vis=set()
        for i in range(n):
            rem[s[i]].append(i)
        for lst in rem.values():
            c=t[lst[0]]
            if c in vis:
                return False
            else:
                vis.add(c)
                for idx in lst:
                    if t[idx]!=c:
                        return False
        return True
        