class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Strategy
        # Count characters in each string using a dictionary,
        # then compare the two dictionaries for equality

        s_counts = {}
        t_counts = {}
        for s_char in s:
            s_counts[s_char] = s_counts.get(s_char, 0) + 1
        for t_char in t:
            t_counts[t_char] = t_counts.get(t_char, 0) + 1
        return s_counts == t_counts
            