class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort nums for 2 pointer method
        nums.sort()
        # Initialize answer
        answer = nums[0] + nums[1] + nums[2]
        
        # Iterate the left integer
        for left in range(len(nums) - 2):
            # 2 pointer method on middle and right integers
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                # Compute guess from 3 pointers
                guess = nums[left] + nums[middle] + nums[right]
                # Update answer if necessary
                if abs(guess - target) < abs(answer - target):
                    answer = guess
                # Guess is too small, increase guess
                if guess < target:
                    middle += 1
                # Guess is too big, decrease guess
                elif guess > target:
                    right -= 1
                # Target found, return it
                else:
                    return target
            
        return answer