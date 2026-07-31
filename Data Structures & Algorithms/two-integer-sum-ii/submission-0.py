class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i = 0
        j = n-1

        while i < j:
            sum1 = numbers[i] + numbers[j]
            if sum1 > target:
                j -= 1
            elif sum1 < target:
                i += 1 
            else:
                return [i+1,j+1]
             