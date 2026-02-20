class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merging the two sorted arrays and sorting the merged array
        merged_array = nums1 + nums2
        merged_array = sorted(merged_array)
        # Finding the median of the merged array
        if len(merged_array)%2 == 0:
            # If the length of the merged array is even, return the average of the two middle elements
            return (merged_array[int((len(merged_array)-1)/2)] + merged_array[int((len(merged_array)+1)/2)])/2
        else:
            # If the length of the merged array is odd, return the middle element
            return merged_array[int((len(merged_array)-1)/2)]

if __name__ == "__main__":
    # creating an instance of the Solution class and calling its method
    solution = Solution()

    # case1 with two lists of numbers
    case1_nums1 = [1,3]
    case1_nums2 = [2]
    
    case1_result = solution.findMedianSortedArrays(case1_nums1, case1_nums2)
    print("Output:", case1_result)

    # case2 with two lists of numbers
    case2_nums1 = [1,2]
    case2_nums2 = [3,4]

    case2_result = solution.findMedianSortedArrays(case2_nums1, case2_nums2)
    print("Output:", case2_result)
    
#Time complexity: O((m+n)log(m+n)) where m and n are the lengths of the two input arrays. This is because we need to merge and sort the two arrays.
#Space complexity: O(m+n) because we create a new array to hold the merged and sorted elements from both input arrays.