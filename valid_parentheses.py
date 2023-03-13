class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        valid = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        
        bank = []
        for i in range(len(s)):
            #print(s[i])
            if s[i] in valid.keys():
                #print(s[i])
                bank.append(s[i])
            elif s[i] in valid.values():
                if bank != [] and valid[bank[-1]] == s[i]:
                    bank.pop()
                else:
                    return False

            
        return not len(bank)>0
