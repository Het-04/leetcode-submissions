class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        y = max(nums) 
        hash_map = {}
        begin = set()
        for i, x in enumerate(nums):
            hash_map[x] = i
        for k,v in hash_map.items():
            if k-1 not in hash_map:
                begin.add(k)
        longest = 0
        for x in begin:
            sequence = 0
            for i in range(y+2):
                if x+i in hash_map:
                    sequence += 1
                else:
                    break
            if sequence > longest:
                longest = sequence
        return longest
        



        
        
        
        