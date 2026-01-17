class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # cause the question already sorted, and ask me to calculate the total, so we can use the two pointer (left and right)
        # when left + right is bigger than target, it' mean we need to move right point close to the left (right -1 ), to close the target.
        left, right = 0, len(numbers) - 1

        ''' no need more for loop, it' may cause  time complexity up to O(n2) '''
        while left < right:
            for i in range(len(numbers)):
                res = numbers[left] + numbers[right]
                if res > target:
                    right -= 1
                elif res < target:
                    left += 1
                else:
                    return [left + 1, right + 1]
        
        while left < right:
            res = numbers[left] + numbers[right]
            if res > target:
                right -= 1
            elif res < target:
                left += 1
            else:
                return [left + 1, right + 1]