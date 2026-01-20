# 🚀 NeetCode 150 Progress Tracker

### Proficiency: 0% (1/150)
`░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░`

**Last Updated:** 2026-01-20 21:57

| Category | ID | Problem | Diff | History | Last Practice | Status | Note |
|---|:---:|---|:---:|---|:---:|---|---|
| **01-Arrays-and-Hashing** | 128 | [Longest Consecutive Sequence](./01-Arrays-and-Hashing/128-Longest-Consecutive-Sequence) | Medium | 🔴 🔴  | 2026-01-11 (9d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>Blocker: When is sequence start and how to efficiently check existence. (n - 1, n + 1)<br>Key Insight: Consecutive sequence -> we can use a set to check for existence in O(1) time.<br>Method: set()<br></details> |
|  | 238 | [Product of Array Except Self](./01-Arrays-and-Hashing/238-Product-of-Array-Except-Self) | Medium | 🔴 🔴 🟡  | 2026-01-17 (3d ago) |  | <details><summary>🔍 Hint</summary>See the hint to fix the question</details> |
|  | 271 | [Encode and Decode Strings](./01-Arrays-and-Hashing/271-Encode-and-Decode-Strings) | Medium | 🔴 🔴 🔴  | 2026-01-19 (1d ago) |  | <details><summary>🔍 Hint</summary>Decode method need to use while loop and two pointer to get the length of each string (ex 10@hello, 3@abc)</details> |
|  | 347 | [Top K Frequent Elements](./01-Arrays-and-Hashing/347-Top-K-Frequent-Elements) | Medium | 🔴 🔴 🔴  | 2026-01-11 (9d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>Know to use bucket sort and hash map, but dont know how to implement (items(), get()).<br>Blocker: Implementation of bucket sort and hash map.<br>Key Insight: Frequent elements -> We can use a hash map to count. then we can use bucket sort to group elements by frequency.<br>Method: hash, bucket sort<br></details> |
|  | 36 | [Valid Sudoku](./01-Arrays-and-Hashing/36-Valid-Sudoku) | Medium | 🔴 🔴  | 2026-01-06 (14d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>Use collections.defaultdict(set) to create each row, column, and 3x3 square hash sets.</details> |
|  | 49 | [Group Anagrams](./01-Arrays-and-Hashing/49-Group-Anagrams) | Medium | 🔴 🔴 🔴  | 2026-01-11 (9d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>| Know to use hash map to group anagrams, but dont know how to implement (ord(), tuple()). Blocker: Implementation of hash map to group anagrams. Key Insight: Group anagrams -> We can use a hash map with a tuple of character counts as the key. Method: ord(), defaultdict, tuple().</details> |
| **02-Two-Pointers** | 11 | [Container With Most Water](./02-Two-Pointers/11-Container-With-Most-Water) | Medium | 🔴 🟡  | 2026-01-20 (0d ago) |  | <details><summary>🔍 Hint</summary>how to calculate the container of the water, when to move the pointer? heights[left] > heights[right] or equal, move what pointer?</details> |
|  | 15 | [3Sum](./02-Two-Pointers/15-3Sum) | Medium | 🔴 🔴  | 2026-01-17 (3d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>combine index + sort + two pointers, avoid duplicates</details> |
|  | 167 | [Two Sum II - Input Array Is Sorted](./02-Two-Pointers/167-Two-Sum-II---Input-Array-Is-Sorted) | Medium | 🔴 🟡 🟢  | 2026-01-17 (3d ago) |  | <details><summary>🔍 Hint</summary>Solve the problem, but no need for loop inside the while loop.</details> |
|  | 42 | [Trapping Rain Water](./02-Two-Pointers/42-Trapping-Rain-Water) | Medium | 🔴  | 2026-01-11 (9d ago) | 🔥 Retry | <details><summary>🔍 Hint</summary>Move the shorter side (bottleneck). <br>Update the wall, and fill the hole. <br>If it's a new high, it becomes a wall. If it's lower, it's a hole for water.</details> |
