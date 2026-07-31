class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for num in nums:
            hashset[num] = hashset.get(num, 0) + 1
        
        for key in hashset.keys():
            if hashset[key] > 1:
                return True
        return False
        