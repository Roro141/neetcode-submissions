class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # for thsi question i think it would be best to get  frequency count of the letters then comapre them
        if len(s) !=  len(t):
            return False

        freq_s={}
        freq_t={}
        for letter in s:
            if letter in freq_s:
                freq_s[letter]+=1
            else:
                freq_s[letter]=1

        for letter in t:
            if letter in freq_t:
                freq_t[letter]+=1
            else:
                freq_t[letter]=1
        
        if freq_s == freq_t:
            return True
        return False
        