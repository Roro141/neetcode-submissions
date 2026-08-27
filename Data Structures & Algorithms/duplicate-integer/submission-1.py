
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alreadySaw = set()  # declare an empty set

        for num in nums:
            if num in alreadySaw:
                return True
            alreadySaw.add(num)  # this must be inside the loop

        # if no duplicates showed up, return false
        return False