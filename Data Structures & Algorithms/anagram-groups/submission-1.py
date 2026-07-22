class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a dictionary:
        # character-count fingerprint -> list of words
        my_groups = {}

        # Process every word
        for word in strs:
            count = [0] * 26

            # Count every character in the current word
            for char in word:
                index = ord(char) - ord('a')
                count[index] += 1

            # Convert the list into a tuple so it can be a dictionary key
            key = tuple(count)

            # Create a new group when this key is seen for the first time
            if key not in my_groups:
                my_groups[key] = []

            # Add the current word to its group
            my_groups[key].append(word)

        # Collect only the dictionary values
        result = []

        for group in my_groups.values():
            result.append(group)

        return result