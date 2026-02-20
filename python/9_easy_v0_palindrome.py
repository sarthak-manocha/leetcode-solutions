class Solution:
    def isPalindrome(self, x: int) -> bool:
        # set to True, if x is negative, set to False because negative numbers cannot be palindromes
        check = True
        if x < 0:
            check = False
        else:
            # convert the integer to a list of its digits and check if the digits are the same from the start and end
            nums = list(str(x))
            # loop through the first half of the list of digits
            for i in range(len(nums)//2):
                # compare the digit at position i with the digit at the corresponding position from the end
                if nums[i] == nums[len(nums)-1-i]:
                    # if the digits are the same, continue checking the next pair of digits
                    pass
                else:
                    # if the digits are not the same, set check to False and break out of the loop
                    check = False
        return check

if __name__ == "__main__":
    # creating an instance of the Solution class and calling its method
    solution = Solution()

    # case1 with an integer that is a palindrome
    case1_x = 121
    
    case1_result = solution.isPalindrome(case1_x)
    print("Output:", case1_result)

    # case2 with an integer that is not a palindrome (negative number)
    case2_x = -121

    case2_result = solution.isPalindrome(case2_x)
    print("Output:", case2_result)

    # case3 with an integer that is not a palindrome
    case3_x = 10
    case3_result = solution.isPalindrome(case3_x)
    print("Output:", case3_result)

# Time complexity: O(n), where n is the number of digits in the integer x. We need to check each digit at most once.
# Space complexity: O(n), where n is the number of digits in the integer x. We need to convert the integer to a list of its digits, which takes O(n) space.