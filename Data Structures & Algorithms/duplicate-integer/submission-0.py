class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numb = {}
        for n in nums:
            if n in numb:
                numb[n] += 1
            else:
                numb[n] = 1
        for value in numb.values():
            if value > 1:
                return True
        return False
         