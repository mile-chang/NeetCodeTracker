class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we can create hash map named count to count the frequency of each integer in nums
        # Second we create Nested List named freq, index represent frequency, freq[i] represent integers,
        # for example nums = [1,2,2,3,3,3,3], freq[1] = [1], freq[2] = [2], freq[4] = [3]
        # Finally we traverse this bucket from end to start, then append into res list
        # until the length of res is equal to k.
        # Time complexity = O(N), Space complexity = O(N)

        # First count the frequency of each integer in nums
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Second create Nested List named freq to store frequency and integers
        # if nums has 6 elements, the maximum possible frequency is 6, so we need +1 for index
        freq = [[] for i in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        # Finally traverse freq from end to start to get the top k frequent elements
        res = []
        # because of range, we need to -1
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                # first put n in res, then determine if we already have k elements
                res.append(n)
                if len(res) == k:
                    return res