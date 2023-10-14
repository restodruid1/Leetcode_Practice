"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r

Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s

Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d

 

Constraints:

    1 <= word1.length, word2.length <= 100
    word1 and word2 consist of lowercase English letters.

SOLUTION: """
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedWord = ""
        indexWord1 = 0
        indexWord2 = 0
        sizeWord1 = len(word1)
        sizeWord2 = len(word2)
        while sizeWord1 > 0 and sizeWord2 > 0:
            mergedWord += word1[indexWord1]
            mergedWord += word2[indexWord2]
            indexWord1 += 1
            indexWord2 += 1
            sizeWord1 -= 1
            sizeWord2 -= 1
        
        if sizeWord1 == 0:
            #append rest of word2
            restWord2 = word2[indexWord2 : ]
            for letter in restWord2:             
                mergedWord += letter
        elif sizeWord2 == 0:
            restWord1 = word1[indexWord1 : ]
            #append rest of word1
            for letter in restWord1:             
                mergedWord += letter

        return mergedWord
