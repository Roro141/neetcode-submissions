class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # based on the recomneded time and space complexity, maybe it a two pointer, and sorting
        # if i sort the examples [-4,-1,-1,0,1,2]
        # lets see what the hint is implying, nums[0]+nums[1]+ nums[2]=0, so if we do soem math, nums[j]+nums[k]=0-(nums[i])-> 

        # so instead we do a two pointer 1 for nums
        # so my two sum is kind of correct, we basically have a start pointer and end pointer
        #if start pointer + end pointer is greater than -(nums[i]) then we move the end pointer in 
        nums.sort()
        output=[]
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and i>0:
                continue
            target=-nums[i]
            end_pointer=len(nums)-1
            start_pointer=i+1
            while end_pointer > start_pointer:
                total=nums[end_pointer]+nums[start_pointer]
                if(total<target):
                    start_pointer +=1
                elif(total>target):
                    end_pointer -=1
                else:
                    output+=[[nums[i],nums[start_pointer], nums[end_pointer]]]
                    start_pointer+=1
                    end_pointer-=1
                    while start_pointer < end_pointer and nums[start_pointer]==nums[start_pointer-1]:
                        start_pointer+=1
                    while start_pointer < end_pointer and nums[end_pointer]==nums[end_pointer+1]:
                        end_pointer-=1
        return output

