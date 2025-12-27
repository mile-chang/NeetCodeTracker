class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # When we see "top k frequent", we can think of using a hashmap to count frequencies
        count = {}
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Second step: sort the elements based on their frequency
        # We can use the sort function or bucket sort approach
        # sort function will cost O(N log N), bucket sort will cost O(N)
        # Here, we use bucket sort approach
        
        # Create buckets where index represents frequency
        # the element can appear at most len(nums) times, so we create len(nums) + 1 buckets
        freq = [[] for i in range(len(nums) + 1)]
        
        # we use items() to get both element and its count
        # For bucket sort we reverse the element and count
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        # Prepare the result list
        res = []
        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # Once we have k elements, we can return the result
                if len(res) == k:
                    return res