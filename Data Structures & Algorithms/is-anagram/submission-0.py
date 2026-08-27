class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters="abcdefghijklmnopqrstuvwxyz"

     #initalize hashMaps
        word1_num= {l:0 for l in letters} #hashmap that tracks the number of occrences in word1
        word2_num= {l:0 for l in letters} #hashmap that tracks the number of occrences in word2

        for l in s:
             word1_num[l]+=1
        for l in t:
            word2_num[l]+=1
        return word1_num==word2_num