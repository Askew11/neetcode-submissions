class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Number to amount
        hashmap = {}
        # ans variable
        ans =[]
        # Go through every number in list
        for num in nums:
            # if number is in hashmap update count if not add it
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        # Check which numbers have the highest amount and add to ans k times
        for i in range(0, k):
            # Current highest Value
            highestKey = max(hashmap, key=hashmap.get)
            ans.append(highestKey)
            del hashmap[highestKey]

        return ans