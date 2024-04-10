class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        origin = nums[0]
        for i in range(len(nums)):
            #print(i, nums)
            for j in range(len(nums)-i-1):
                #print(j, -i-1)
                if nums[j]**2 <= nums[-i-1]**2:
                    pass
                elif nums[j]**2 > nums[-i-1]**2:
                    nums[j], nums[-i-1] = nums[-i-1], nums[j]
                    #print('swap', nums)
    
            nums[-i-1] = nums[-i-1]**2

        return nums
# 128 / 137 testcases passed