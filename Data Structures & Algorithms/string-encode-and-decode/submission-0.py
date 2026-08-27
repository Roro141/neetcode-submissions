class Solution:

    def encode(self, strs: List[str]) -> str:
            #strs = ["Hello","World"] -> "HelloWorld"
            #use an intger to get the count of each dilimiter
            #first go throguh each string in the array
            #use soem length formua to get the length f the string
            #have a result string tht we wil return after goign through the whole array
            #each strign will be comverted to (length)$word
            #add that to the result string

            result=""
            for word in strs:
                length=len(word)
                encoded_word=str(length)+ "$" +word
                result= result + encoded_word

            return result

    def decode(self, s: str) -> List[str]:
        #create a result array, and index counter as well

        #use a while loop to go through the string
        #use a two pointer approach to get the length of the string
        #i will stay at the beginning
        #j will find the delimiter, in this case a $
        #use another while loop to keep iterating j until it gets the $

        result = []
        i = 0

        while i < len(s):
                j = i

                while s[j] != "$":
                        j += 1

                #the length is the string from i to j, converted to an integer
                length = int(s[i:j])

                #add the word after the $ to the result array
                result.append(s[j + 1:j + 1 + length])

                #update i to the beginning of the next encoded word
                i = j + 1 + length

        return result

