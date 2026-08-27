from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = defaultdict(list)
        for word in strs:
            # Sort the word to create a canonical key for anagrams
            sorted_word_tuple = tuple(sorted(word))
            anagram_groups[sorted_word_tuple].append(word)
        return list(anagram_groups.values())
