class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      running_total=1
      prefix = [1 for _ in nums]
      suffix = [1 for _ in nums]
    
      for i in range(len(nums)):
        prefix[i]=running_total
        running_total= running_total*nums[i]
       
      running_total=1
      
      for i in range(len(nums)-1, -1, -1):
        suffix[i] = running_total
        running_total= running_total*nums[i]
      output =[ 1 for _ in nums]
      for i in range(len(nums)):
        output[i]= prefix[i]*suffix[i]

      return output


