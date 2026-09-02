class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #i would use a two pointer approach
        # start pointer= 0 
        # end pointer= array.length()-1
        # we compare the  number at the end + first and comapre it to the atgret
        #array[start pointer]+ array[end pointer] 
        #while start pointer < end pointer:
        #    if(start pointer + end pointer == target):
        #       return [start pointer, end pointer]
        #   if(start pointer + end pointer> target):
        #       move the end pointer left
        #   else if(start pointer +end pointer <target):
        #       move the right pointer right

        start_pointer, end_pointer = 0, len(numbers)-1

        while start_pointer < end_pointer:
            current_sum = numbers[start_pointer] + numbers[end_pointer]
            if(current_sum ==target):
                return [start_pointer + 1, end_pointer + 1] 
            elif (current_sum< target):
                 start_pointer +=1
            else:
                end_pointer -=1
        


