class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_ = 0
        start = 0
        dict_ = {}
        for i in range(len(s)):
            if s[i] in dict_  and start <= dict_[s[i]]:
                start = dict_[s[i]] + 1    
            else:
                max_ = max(i- start + 1, max_)
            dict_[s[i]] = i
        return max_