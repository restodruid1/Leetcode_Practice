"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

 

Constraints:

    1 <= s.length, t.length <= 5 * 104
    s and t consist of lowercase English letters.

"""

class Solution Compare sets:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)

        if counter1 == counter2:
            return True
        else:
            return False

#Time Complexity = O(s + t)
#Space Complexity = O(s + t)

class Solution Compare lists:
    def isAnagram(self, s: str, t: str) -> bool:
        so = list(s)
        to = list(t)
        so.sort()
        to.sort()
        if so == to:
            return True
        else:
            return False

#Time Complexity = O(s + t)
#Space Complexity = O(s + t)