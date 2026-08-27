class Solution {
    public int longestConsecutive(int[] nums) {
         Set<Integer> numSet = new HashSet<>();
        for (int num : nums) numSet.add(num);
        // for each number in the set i need to see if the set contaisn num-1
        //if it does then that number is nto the begining of a sequence
        //if it doesnt we will check if the set contains num+1, then so on until we reach the end of that array
        //we need to have a variable that is clauclating the current length of the sequency
        int maxLength=0;
        for(int num:numSet)
        {
            if(!numSet.contains(num-1))
            {
                int currNum= num;
                int length =1;
                while (numSet.contains(currNum + 1)) {
                    currNum += 1;
                    length++;
                }

                maxLength = Math.max(maxLength,length);
            }
        }
        return maxLength;
    }
}
