class Solution {
    public int lengthOfLongestSubstring(String s) {
        //first easiest to iterate througb if it is a charcater array
        char[] arr= s.toCharArray();
        //maybe same approach to the longest substrign of numbers
        //so we create a set or something to add a charcater until we reach a duplicat ehcarcter, and create a set of charcetr we alreaysaw
        //as well a two pointer approach
        HashSet<Character> seen= new HashSet<>();
        //left pointer start of string, rigth pointer rigth next to next
        //if the character at the pointers are the same
        //move the left pointer and the rigth pointer to the left
        //if it isnt the same, add to the alreadySaw set
        //continue
        int l= 0;
        int maxLength=0;
        for(int r=0;r<arr.length;r++)
        {
            char rightChar= arr[r];
            //removing the duplicate when we fidn one and then moving the window
            while (seen.contains(rightChar)) {
                seen.remove(arr[l]);
                l++;
            }
            if (!seen.contains(rightChar)) {
                seen.add(rightChar);
            }

            maxLength = Math.max(maxLength, r - l + 1);
        }
        
        return maxLength;

    }
}
