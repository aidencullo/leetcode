"""
LeetCode 520: Detect Capital

Given a string word, return true if the usage of capitals in it is right.

The usage of capitals is right when one of the following cases holds:
- All letters in this word are capitals (like "USA")
- All letters in this word are not capitals (like "leetcode")
- Only the first letter in this word is capital (like "Google")

Examples:
    Input: word = "USA"
    Output: true

    Input: word = "FlaG"
    Output: false

Constraints:
    - 1 <= word.length <= 100
    - word consists of lowercase and uppercase English letters
"""


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        Determines if the capitalization usage in a word is correct.

        Args:
            word: A string consisting of uppercase and lowercase letters

        Returns:
            True if capitalization is correct, False otherwise
        """
        if word.lower() == word:
            return True

        if word.upper() == word:
            return True

        new_word = word[0].lower() + word[1:]

        if new_word == new_word.lower():
            return True

        return False
