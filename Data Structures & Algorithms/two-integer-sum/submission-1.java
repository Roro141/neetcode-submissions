class Solution {
    public int[] twoSum(int[] nums, int target) {
       //you can try and fidn the difference so target-nums[j]
       Map<Integer,Integer> diffMap= new HashMap<>();
       for(int i=0;i<nums.length;i++)
       {
        //num is the value at the current index
         int num=nums[i];
         //difference of tagret - current value
         int diff = target- num;
         //the key of teh hasmap is going to be difference betweent he target and the value at teh current index
         //so if the difference exsists already
         if(diffMap.containsKey(diff))
         {
            //return the index of where the diff is, and the current index
            //it creates a new itn array with the two indexes
            return new int[] {diffMap.get(diff),i};
         }
         //else put the value:and the index
         diffMap.put(num,i);
       }
       return new int[] {};
    }
}
