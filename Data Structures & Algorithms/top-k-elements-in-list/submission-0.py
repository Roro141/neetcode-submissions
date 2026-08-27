class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        
        # count frequency
        for num in nums:
            mp[num] = mp.get(num, 0) + 1
        
        # convert to list of [num, freq]
        values = [[num, freq] for num, freq in mp.items()]
        
        # sort by frequency (highest first)
        values.sort(key=lambda x: x[1], reverse=True)
        
        # take top k numbers
        return [num for num, freq in values[:k]]
