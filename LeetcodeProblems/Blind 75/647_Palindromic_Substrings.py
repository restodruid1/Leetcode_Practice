"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

 

Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.




"""

class Solution:
    def countSubstrings(self, s: str) -> int:

        def expand_from_center(left, right):
            counter = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                counter += 1

            return counter

        ans = 0
        for i in range(len(s)):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            ans += odd
            ans += even

        return ans 

#Time Complexity = O(n^2)
#Space Complexity = O(1)

