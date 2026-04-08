class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_numbers={}
        for index,value in enumerate(nums):
            complement= target - value
            if complement in seen_numbers:
                return [seen_numbers[complement], index]
            seen_numbers[value] = index
  