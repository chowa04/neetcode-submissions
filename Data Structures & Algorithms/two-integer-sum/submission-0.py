class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """output = []
        for i in nums:
            for j in nums:
                sum = i+j
                if sum == target:
                    return [i,j]
        return output
        this is only if they want the exact number not the index"""

        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return output

        