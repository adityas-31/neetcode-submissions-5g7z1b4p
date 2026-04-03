class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a dict out of the two strings
        #iterate through both dicts in the same loop - deduct for every character
        #if counts are 0 at the end then they are anagrams
        dict_s = dict()
        dict_t = dict()
        for i in s:
            dict_s[i] = 0
        for i in s:
            dict_s[i] += 1 
        for i in t:
            dict_t[i] = 0
        for i in t:
            dict_t[i] += 1 
        print("dict_s = " , dict_s)
        print("dict_t = " , dict_t)
        if len(s) != len(t):
            return False
        else:
            if dict_s == dict_t:
                return True
            else:
                return False
            