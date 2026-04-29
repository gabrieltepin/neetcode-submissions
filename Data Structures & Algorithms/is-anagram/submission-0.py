class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ls = len(s)
        Lt = len(t)
        if (Ls != Lt): 
            return False

        chars_s = dict()
        chars_t = dict()
        for i,_ in enumerate(s):
            chars_s[s[i]] = chars_s.get(s[i], 0) + 1
            chars_t[t[i]] = chars_t.get(t[i], 0) + 1
        for k in chars_t.keys():
            if (chars_t[k] != chars_s.get(k,0)): 
                return False
        
        return True