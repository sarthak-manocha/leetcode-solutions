class Solution:
    def CountVowels(self, s: str) -> int:
        # initialising a counter variable to keep track of the number of words ending with a vowel
        count = 0
        # looping through each word in the string
        for w in s.split():
            # checking if the last character of the word is a vowel
            if w[-1] in 'aeiou':
                # incrementing the counter if it is a vowel
                count += 1
        # returning the final count of words ending with a vowel
        return count

if __name__ == "__main__":
    # creating an instance of the Solution class and calling its method
    solution = Solution()
    
    # input string for testing
    s = "we are learning python"

    result = solution.CountVowels(s)
    print("Number of words ending with a vowel:", result)

# Time Complexity: O(n), where n is the number of characters in the input string. 
# This is because we need to iterate through each word in the string to check if it ends with a vowel.

# Space Complexity: O(1), as we are using a constant amount of extra space to store the count variable, 
# regardless of the size of the input string.