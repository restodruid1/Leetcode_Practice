"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

 

Constraints:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

 
Follow up: Could you minimize the total number of operations done?

SOLUTION: """

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or len(nums) == 0:
            return nums
        """
        nums2 = []
        for num in nums:
            if num != 0:
                nums2.append(num)
        for num in nums:
            if num == 0:
                nums2.append(num)
                print(nums2)    

        print(nums2)
        nums = nums2"""

       
        quan = 0
        #0,1,2,3,4  n=5
        for num in range(len(nums)):
            if nums[num] == 0:
                quan += 1
            elif quan > 0:
                temp = nums[num]
                nums[num] = 0
                nums[num - quan] = temp 