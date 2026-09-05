class Solution:
    def isPalindrome(self, s: str) -> bool:
        #create a new string
        newStr = ''
        for c in s:
            #if its false (ie a special charcater) 
            if c.isalnum():
                #add the charcater lowercases
                newStr += c.lower()
                #comapres the string with the sam strign btu backward
        return newStr == newStr[::-1]