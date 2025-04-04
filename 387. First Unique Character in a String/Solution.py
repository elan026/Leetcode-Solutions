class Solution:
    def firstUniqChar(self, s: str) -> int:
        # a = Counter(s)
        # for i in s:
        #     if a[i]==1:
        #         return s.index(i)
        # return -1
        
        a = list(set(s.strip()))
        res = []
        for i in a:
            if s.count(i)==1:
                 res.append(s.index(i))
        if len(res)==0:
            return -1
        return min(res)