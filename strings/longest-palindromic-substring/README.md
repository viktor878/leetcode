# Longest Palindromic Substring

Python solution for the LeetCode problem **Longest Palindromic Substring**.

## Problem

Given a string `s`, return the longest palindromic substring.

## Approach

The algorithm expands around every possible palindrome center.

For every index:

- check odd-length palindrome
- check even-length palindrome
- keep the longest substring

## Complexity

- Time: O(n²)
- Space: O(1)

## Language

Python
