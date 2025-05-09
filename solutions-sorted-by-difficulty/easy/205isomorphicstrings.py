class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
