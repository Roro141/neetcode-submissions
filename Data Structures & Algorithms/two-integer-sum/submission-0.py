class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      #Brute force application, create a nested for loop checkign for every comboniation

      #plan is to get the difference between target and nums[i]
      # create an empty hash map
      values={}

    # enumarate works the same as for num: nums in java
      for i, num in enumerate(nums):
        # gets the difference

        difference =target-num

        #if the difference is already in value, it returnrs the indices, and the current index
        if difference in values:
            return [values[difference],i]
        #else it gets the new index
        values[num] =i

    
