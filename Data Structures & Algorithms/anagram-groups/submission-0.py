class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) ## mapping char count to list of anagrams
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) -  ord('a')] += 1 ## Using ASCII value ofthe characters which is what ord does
            res[tuple(count)].append(s) ## tuple allows us to make a list a key in hash map

        return res.values()