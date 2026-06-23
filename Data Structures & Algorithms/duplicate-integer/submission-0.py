class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_count = {}
        for num in nums:
            dict_count[num] = dict_count.get(num, 0) + 1
            if dict_count[num] == 2:
                return True
        return False        
        