from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we need a hashmap to keep track of the frequency of each number
        count = Counter(nums)

        #frequency map with the same length as the input array
        freq = [[] for i in range(len(nums) + 1)]

        #populate the frequency buckets
        for num, c in count.items():
            freq[c].append(num)

        #create an empty list to store the result
        result = []

        #start from the highest frequency and move downward
        for c in range(len(freq) - 1, 0, -1):

            #look at each number in the current frequency bucket
            for num in freq[c]:
                result.append(num)

                #stop once we have k numbers
                if len(result) == k:
                    return result

