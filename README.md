# 🚀 NeetCode 150 Progress Tracker

### Proficiency: 0% (1/150)
`░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░`

**Last Updated:** 2026-01-25 17:18

| Category | ID | Problem | Diff | History | Last Practice | Status | Note |
|---|:---:|---|:---:|---|:---:|---|---|
| **01-Arrays-and-Hashing** | 128 | [Longest Consecutive Sequence](./01-Arrays-and-Hashing/128-Longest-Consecutive-Sequence) | Medium | 🔴 🔴 🔴  | 2026-01-22 (3d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>convert list to set to become O(1) time complexity, n + length to avoid loop, while in for loop but still O(N), because the while loop only run once in each for loop.</details> |
|  | 238 | [Product of Array Except Self](./01-Arrays-and-Hashing/238-Product-of-Array-Except-Self) | Medium | 🔴 🔴 🟡  | 2026-01-17 (8d ago) | 🔔 Review | <details><summary>🔍 Hint</summary>See the hint to fix the question</details> |
|  | 271 | [Encode and Decode Strings](./01-Arrays-and-Hashing/271-Encode-and-Decode-Strings) | Medium | 🔴 🔴 🔴  | 2026-01-19 (6d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>Decode method need to use while loop and two pointer to get the length of each string (ex 10@hello, 3@abc)</details> |
|  | 347 | [Top K Frequent Elements](./01-Arrays-and-Hashing/347-Top-K-Frequent-Elements) | Medium | 🔴 🔴 🔴 🔴  | 2026-01-25 (0d ago) |  | <details><summary>🔍 Hint</summary>hash map + 2D list, dict.get(), dict.items(), dict[key]</details> |
|  | 36 | [Valid Sudoku](./01-Arrays-and-Hashing/36-Valid-Sudoku) | Medium | 🔴 🔴 🔴  | 2026-01-21 (4d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>collections.defaultdict(set), first check then update the value in hash set</details> |
|  | 49 | [Group Anagrams](./01-Arrays-and-Hashing/49-Group-Anagrams) | Medium | 🔴 🔴 🔴  | 2026-01-11 (14d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>| Know to use hash map to group anagrams, but dont know how to implement (ord(), tuple()). Blocker: Implementation of hash map to group anagrams. Key Insight: Group anagrams -> We can use a hash map with a tuple of character counts as the key. Method: ord(), defaultdict, tuple().</details> |
| **02-Two-Pointers** | 11 | [Container With Most Water](./02-Two-Pointers/11-Container-With-Most-Water) | Medium | 🔴 🟡  | 2026-01-20 (5d ago) | 🔔 Review | <details><summary>🔍 Hint</summary>how to calculate the container of the water, when to move the pointer? heights[left] > heights[right] or equal, move what pointer?</details> |
|  | 15 | [3Sum](./02-Two-Pointers/15-3Sum) | Medium | 🔴 🔴  | 2026-01-17 (8d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>combine index + sort + two pointers, avoid duplicates</details> |
|  | 167 | [Two Sum II - Input Array Is Sorted](./02-Two-Pointers/167-Two-Sum-II---Input-Array-Is-Sorted) | Medium | 🔴 🟡 🟢  | 2026-01-17 (8d ago) |  | <details><summary>🔍 Hint</summary>Solve the problem, but no need for loop inside the while loop.</details> |
|  | 42 | [Trapping Rain Water](./02-Two-Pointers/42-Trapping-Rain-Water) | Medium | 🔴 🔴  | 2026-01-25 (0d ago) |  | <details><summary>🔍 Hint</summary>the water trapped is height[i] - min(max_left, max_right), cause bottleneck is the shorter side</details> |
| **05-Sliding-Window** | 3 | [Longest Substring Without Repeating Characters](./05-Sliding-Window/3-Longest-Substring-Without-Repeating-Characters) | Medium | 🔴  | 2026-01-25 (0d ago) |  | <details><summary>🔍 Hint</summary>In the sliding window, when to expand, when to shrink, when to update the result?</details> |
