class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for i in range(len(nums)):
            otherHalf = target - nums[i]
            if otherHalf in hashmap:
                return [hashmap[otherHalf], i]
            else:
                hashmap[nums[i]] = i

        


