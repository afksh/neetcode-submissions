from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for string in strs:
            letter_counts = frozenset(Counter(string).items())
            anagrams[letter_counts].append(string)
        return list(anagrams.values())