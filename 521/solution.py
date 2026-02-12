"""
LeetCode 521: Longest Uncommon Subsequence I
Difficulty: Easy

Given two strings a and b, return the length of the longest uncommon subsequence
between a and b. If no such uncommon subsequence exists, return -1.

An uncommon subsequence between two strings is a string that is a subsequence of
exactly one of them.

Examples:
- Input: a = "aba", b = "cdc"
  Output: 3
  Explanation: "aba" is a subsequence of "aba" but not "cdc"

- Input: a = "aaa", b = "bbb"
  Output: 3
  Explanation: The longest uncommon subsequences are "aaa" and "bbb"

- Input: a = "aaa", b = "aaa"
  Output: -1
  Explanation: Every subsequence of a is also a subsequence of b
"""
import math

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1
