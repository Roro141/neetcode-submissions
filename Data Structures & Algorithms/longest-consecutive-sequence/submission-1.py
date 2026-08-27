class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #my brain first jumped to a two pointer but that wouldnt work but if we have [2,20,4,10,3,4,5]
        #Put all the numbers into a hashset
        num_set = set()
        for num in nums:
            num_set.add(num)
        
        if not num_set:
            return 0
        
        best_count = 1
        #iterate through each element, if num-1 exists, continue
        for num in num_set:
            if num - 1 in num_set:
                continue
            #else it is the start of the list, update count
            else:
                curr_count = 1
                next_num = num + 1
                while next_num in num_set:
                    curr_count += 1
                    next_num += 1
                best_count = max(best_count, curr_count)
        
        return best_count