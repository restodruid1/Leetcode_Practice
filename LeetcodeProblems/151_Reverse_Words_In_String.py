"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

 

Constraints:

    1 <= s.length <= 104
    s contains English letters (upper-case and lower-case), digits, and spaces ' '.
    There is at least one word in s.

SOLUTION: """

class Solution:
    def reverseWords(self, s: str) -> str:
        
        n , m = 0, len(s) - 1

        while s[n] == " ":  #Trim whitespace 
            n += 1
        while s[m] == " ":  #Trim whitespace
            m -= 1
        
        newString = s[n:m+1]    #String with no leading or trailing whitespace
        
        words = newString.split()   #Split the string into separate words
        
        words.reverse()            #Reverse the words in the list

        return ' '.join(words)      #Join the elements with whitespace in between


# Time complexity = O(n)?
# Space complexity = O(n)?
