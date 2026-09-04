class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #one thing notice is the smaller height will judge how tall a container is
        #you want to move the pointer at the smaller height, because you are trying to maximize the area
        #we do the length between the start and end pointer to get the widt
        #the height is the shorter one, we start super wide and mvoe the smaller pointer until we find the biggest are
        i, j=0, len(heights)-1
        best_area=0
        while j>i:
            curr_area=(j-i)*min(heights[i], heights[j])
            best_area=max(curr_area, best_area)
            if(heights[i]<heights[j]):
                i+=1
            else:
                j-=1
        return best_area;