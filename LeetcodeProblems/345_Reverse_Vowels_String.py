"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"

Example 2:

Input: s = "leetcode"
Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

SOLUTION: """

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        point1 = s[0]
        point2 = s[-1]
        n = 0
        m = len(s) - 1
        word = list(s)
        print(m)
        while n < m :
            while n < m and s[n] not in vowels:
                n += 1
            
            while n < m and s[m] not in vowels:
                m -=1
            
            word[n],word[m] = word[m], word[n]
            n += 1
            m -= 1
        return "".join(word) 
            
            
            """if s[n] not in vowels:
                n += 1
                #point1 = s[n]
            else:
                point1 = s[n]
            if s[m] not in vowels:
                m -= 1
                #point2 = s[m]
            else:
                point2 = s[m]
            if point1 and point2 in vowels:
                word[n],word[m] = word[m], word[n]
                n += 1
                m -= 1  """
                  