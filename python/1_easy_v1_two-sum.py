class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # looping through list to get 1st number
        for i in range(0, len(nums)):
            # calculating 2nd number by subtracting 1st number from target
            tmp = target - nums[i]
            # checking if 2nd number is in list and getting its index
            ind = nums.index(tmp) if tmp in nums else -1

            # checking if 2nd number is not the same as 1st number and if it is in list, then returning their index
            if ind != i and ind != -1:
                # returning list of index of 1st and 2nd number
                return [i, ind]

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

 # Time Complexity: O(n^2) - because of the loop and the index() method which both have a time complexity of O(n)
 # Space Complexity: O(1) - because we are not using any extra space to store