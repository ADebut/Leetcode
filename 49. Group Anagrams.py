class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        slist = collections.defaultdict(list)
        for i in strs:
            slist[tuple(sorted(i))].append(i)
        
        return slist.values()