class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        val1, val2, freq1, freq2 = 0, 1, 0, 0
        
        # Step 1: Finding candidates
        for num in nums:
            if num == val1:
                freq1 += 1
            elif num == val2:
                freq2 += 1
            elif freq1 == 0:
                val1, freq1 = num, 1
            elif freq2 == 0:
                val2, freq2 = num, 1
            else:
                freq1 -= 1
                freq2 -= 1
        
        # Step 2: Verification
        result = []
        n = len(nums)
        for cand in [val1, val2]:
            if nums.count(cand) > n // 3:
                result.append(cand)
        
        return list(set(result))