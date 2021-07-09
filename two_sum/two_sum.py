# time O(n^2)

def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i] + nums[j] == target:
        return [i, j]

print(twoSum(nums=[2,7,11,15], target=9))

# O(n)

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for index, number in enumerate(nums):
            partner = target - number
            if partner in d:
                return [d[partner],index]
            d[number] = index
