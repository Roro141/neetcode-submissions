class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Create an empty hashmap called seen
        #For each word in strs:
        #sort the word to get a key
        #if the key is not in seen:
        #create an empty list at seen[key]
        #append the original word to seen[key]
        #Return all the lists stored in seen
        seen={}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in seen:
                seen[key] = []
            seen[key].append(word)

        return list(seen.values())