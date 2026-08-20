class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        h_val = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                if counter >= h_val:
                    h_val = counter
            else:
                counter = 0
        return h_val

        