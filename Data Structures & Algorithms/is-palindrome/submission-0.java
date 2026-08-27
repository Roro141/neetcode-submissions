class Solution {
    public boolean isPalindrome(String s) {
        //one pointer to the begining of the string
        //another at teh end
        //I can first split it on the spaces
        //then make it character array
        String input = s.replaceAll("[^A-Za-z0-9]", "").toLowerCase();
        char[] chars= input.toCharArray();
        //left pointer is at the begining of the array
        //rigth pointer at the end of the array
        int left=0;
        int right=chars.length-1;
        while(left<right)
        {
            if(chars[left]!=chars[right])
            {
                return false;
            }
            left++;
            right--;
        }
        return true;

    }
}
