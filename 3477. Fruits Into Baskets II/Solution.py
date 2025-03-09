class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        """
        :type fruits: List[int]
        :type baskets: List[int]
        :rtype: int
        """
        a=[]
        i=0
        while(i<=len(fruits)-1):
            for j in baskets:
                if fruits[i] <= j:
                    a.append(fruits[i])
                    baskets.remove(j)
                    break
            i+=1
        return len(fruits)-len(a)
