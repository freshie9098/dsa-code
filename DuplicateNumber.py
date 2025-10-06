class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # https://leetcode.com/problems/find-the-duplicate-number/solutions/72846/my-easy-understood-solution-with-o-n-time-and-o-1-space-without-modifying-the-array-with-clear-explanation
        if not nums:
            return 0
        #Floyd's Tortoise and Hare algorithm.
        slow = nums[0]
        fast = nums[nums[0]]
        #like linkedlist cycle 2
        #first find the meeting point. 
        while(slow!=fast):
            slow = nums[slow]
            fast = nums[nums[fast]]
        #now move both one step at a time.
        slow = 0
        while(slow!=fast):
            slow = nums[slow]
            fast = nums[fast]
        return slow
