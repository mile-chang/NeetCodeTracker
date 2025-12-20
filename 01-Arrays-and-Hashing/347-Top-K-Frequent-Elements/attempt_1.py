class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ''' Bucket Sort Approach '''
        # We use a hashmap to count the frequency of each element
        count = {}
        # We use a list of lists to group elements by their frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Get the hashmap with element counts
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # Group the elements by their frequency
        for n, c in count.items():
            freq[c].append(n)
        
        # Prepare the result list
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
