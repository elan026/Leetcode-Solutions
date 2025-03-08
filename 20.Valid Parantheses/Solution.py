class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in range(len(s)):
            if s[i]=="(" or s[i]=="[" or s[i]=="{":
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                last = stack.pop()
                if(s[i] == ")" and last != "(") or (s[i] == "]" and last != "[") or (s[i] == "}" and last != "{"):
                    return False
        return not stack



        
        
        