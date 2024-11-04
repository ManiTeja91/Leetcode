class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k = 0
        arr = []
        i = 0
        while i < n:
            if nums[i] in arr and nums[i] != '_':
                nums.remove(nums[i])
                nums.append('_')     
            elif nums[i] == '_':
                i = i+1
            else:
                arr.append(nums[i])
                k += 1
                i += 1

        return k

        
