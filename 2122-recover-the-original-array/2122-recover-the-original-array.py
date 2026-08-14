from collections import Counter
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        smallest, largest = nums[0], nums[-1]
        nums_counter = Counter(nums)
        knums = list(nums_counter.keys())

        for knum in knums[1:]:
            K = knum - smallest
            if K & 1 or smallest + K not in nums_counter or largest - K not in nums_counter:
                continue
            
            ans = []
            numsc = nums_counter.copy()
                        
            for num in knums:
                if numsc[num] == 0:
                    continue
                if num + K not in numsc or numsc[num + K] == 0:
                    break
            
                count = min(numsc[num], numsc[num + K])        
                numsc[num] -= count
                numsc[num + K] -= count

                ans += [num + K//2]*count
       
            if len(ans) == len(nums) // 2:
                return ans