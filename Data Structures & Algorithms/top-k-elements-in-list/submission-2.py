class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for i in range(len(nums) + 1)]
        counter = {}

        for num in nums:
            counter[num] = counter.get(num,0) + 1

        for numb,count in counter.items():
            buckets[count].append(numb)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for numb in buckets[i]:
                result.append(numb)
                if len(result) == k:
                    return result
