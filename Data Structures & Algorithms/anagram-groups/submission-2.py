class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            count = [0] * 26
            # fill in the counting part
            for ch in s:
                count[ord(ch)-97]+=1
            key = tuple(count)
            # add s to groups[key]
            if key not in groups:
                groups[key]=[]
            groups[key].append(s)
    
        return list(groups.values())