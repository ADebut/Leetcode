class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        cntr_lp, res = {k: v for k, v in collections.Counter(licensePlate.lower()).items() if k.isalpha()}, None
        for word in words:
            check = collections.Counter(word.lower())
            if all(k in check and v <= check[k] for k, v in cntr_lp.items()):
                if not res or len(word) < len(res): 
                    res = word
        return res