class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #hashmap of indexes, each index is a count
        count={}
        # the count will start at 1, for one item, to the max num items with is length of nums
        frequency=[[]for i in range(len(nums)+1)]

        for num in nums:
            #for every number it adds one to count
            #count.get(num,0) This part attempts to retrieve the value associated with the key num
            #if its not there it gives it the default 0
            count[num] = 1 + count.get(num, 0)
        #count.items access the items mapped to each count
        for num, cnt in count.items():
            #at each count index, add the number who matches that count
            frequency[cnt].append(num)
        #resultant array
        result=[]
        #loop to return the rigth items
        for i in range(len(frequency)-1, 0,-1):
            for num in frequency[i]:
                result.append(num)
                if len(result)==k:
                    return result



