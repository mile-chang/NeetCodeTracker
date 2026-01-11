class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' Method 1: Using hashmap + bucket sort '''
        count = {}
        # Becuase freq[i] contains a list of numbers that appear i times.
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        ''' Method 2: Using Counter from collections '''
        # count = Counter(nums)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        # Gather the top k frequent elements
        # the indexes of freq go from 0 to len(nums), so we minus 1.
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Once we have k elements, return the result
                if len(res) == k:
                    return res