class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # Store required frequencies
        countT = {}

        for char in t:
            countT[char] = 1 + countT.get(char, 0)

        # Store frequencies in the current window
        window = {}

        have = 0
        need = len(countT)

        left = 0

        # Store the best window
        res = [-1, -1]
        result = float("inf")

        # Expand using the right pointer
        for right in range(len(s)):
            char = s[right]

            window[char] = 1 + window.get(char, 0)

            # Check whether this requirement is satisfied
            if char in countT:
                if window[char] == countT[char]:
                    have += 1

            # Shrink while the window is valid
            while have == need:
                currLength = right - left + 1

                # Save the current window if it is smaller
                if currLength < result:
                    res = [left, right]
                    result = currLength

                # Remove the left character
                leftChar = s[left]
                window[leftChar] -= 1

                # Check whether the window became invalid
                if leftChar in countT:
                    if window[leftChar] < countT[leftChar]:
                        have -= 1

                left += 1

        if result == float("inf"):
            return ""

        start, end = res
        return s[start:end + 1]