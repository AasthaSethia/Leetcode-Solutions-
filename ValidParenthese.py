class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if (s[i]=='(' or s[i] =='{'or s[i]== '['):
                stack.append(s[i])
                continue;
            if (len(stack)==0):
                return False
            if (s[i]==')'):
                x=stack.pop();
                if (x =='{' or x =='['):
                    return False
            elif (s[i]=='}'):
                x=stack.pop();
                if (x =='(' or x =='['):
                    return False
            elif (s[i]==']'):
                x=stack.pop();
                if (x =='{' or x =='('):
                    return False
        if (len(stack) == 0 ): 
            return True
        else: 
            return False
