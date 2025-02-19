class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_occurrence = {}  # Store the first index of each character
        max_length = -1  # Initialize max length to -1
        
        for i, char in enumerate(s):
            if char in first_occurrence:
                # Calculate the length of the substring between first and current occurrence
                length = i - first_occurrence[char] - 1
                max_length = max(max_length, length)
            else:
                first_occurrence[char] = i  # Store first occurrence of char
        
        return max_length