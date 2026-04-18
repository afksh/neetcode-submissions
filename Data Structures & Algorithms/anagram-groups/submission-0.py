class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Strategy: Create a frozen dictionary of character counts in each word
        # and use them as keys to a dictionary mapping that frozen dictionary to
        # a list of seen words from the input that match that character count

        anagrams = {}
        for string in strs:
            letter_counts = {}
            for letter in string:
                letter_counts[letter] = letter_counts.get(letter, 0) + 1
            hashable_letter_counts = set()
            for key, val in letter_counts.items():
                hashable_letter_counts.add((key, val))
            hashable_letter_counts = frozenset(hashable_letter_counts)
            anagrams[hashable_letter_counts] = anagrams.get(hashable_letter_counts, []) + [string]
        return list(anagrams.values())