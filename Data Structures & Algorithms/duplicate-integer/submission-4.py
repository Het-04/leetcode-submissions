class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for a in nums:
            if a in counter:
                counter[a] += 1
            else:
                counter[a] = 1

        for key in counter.keys():
            if counter[key] > 1:
                return True 
        
        return False