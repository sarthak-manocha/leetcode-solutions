class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # looping through list to get 1st number
        for i in range(0, len(nums)):
            # looping though again to get the other number
            for j in range (i+1, len(nums)):
                # getting the sum of the 2 numbers
                tmp = nums[i] + nums[j]
                
                # checking if the sum matches the target value
                if (tmp == target):
                    # returning the index values of the numbers
                    return [i,j]    

if __name__ == "__main__":
    # creating an instance of the Solution class and calling its method
    solution = Solution()

    # case1 with list of numbers and target value
    case1_nums = [2, 7, 11, 15]
    case1_target = 9
    
    case1_result = solution.twoSum(case1_nums, case1_target)
    print("Output:", case1_result)

    # case2 with list of numbers and target value
    case2_nums = [3,2,4]
    case2_target = 6

    case2_result = solution.twoSum(case2_nums, case2_target)
    print("Output:", case2_result)

    # case2 with list of numbers and target value
    case3_nums = [3,3]
    case3_target = 6

    case3_result = solution.twoSum(case3_nums, case3_target)
    print("Output:", case3_result)

# Time Complexity: O(n^2) - because of the nested loops
# Space Complexity: O(1) - because we are not using any extra space to store the numbers or their indices