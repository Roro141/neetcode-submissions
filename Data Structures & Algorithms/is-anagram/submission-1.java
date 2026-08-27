class Solution {
    public boolean isAnagram(String s, String t) {
        //create a hash table to map each letter to to frequency
        //if the frequency of each letter of both strigns is the same they are equal
         Hashtable<Character, Integer> word1 = new Hashtable<>();
         Hashtable<Character, Integer> word2= new Hashtable<>();

         for(char ch :s.toCharArray())
         {
            //key is the letter, the val is the number at the value incrmeented by 1
            word1.put(ch, word1.getOrDefault(ch, 0) + 1);
         }
         for(char ch:t.toCharArray())
         {
            //key is the letter, the val is the number at the value incrmeented by 1
            word2.put(ch, word2.getOrDefault(ch, 0) + 1);
         }

         return word1.equals(word2);
    }
}
