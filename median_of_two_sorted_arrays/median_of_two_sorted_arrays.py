# def median_2arrays(nums1,nums2):
#   #using binary search algorithm!

#   # check which array is larger, nums2 should be larger than nums1, if not, swap em!
#   if int(len(nums1)) > int(len(nums2)):
#     nums1, nums2 = nums2, nums1

#   # determine the indices of the partition of the two arrays
#   nums1_length = int(len(nums1)) - 1
#   nums2_length = int(len(nums2)) - 1

#   min_index = 0
#   max_index = nums1_length

#   while min_index <= (max_index+1):

#   # determine the indices of the partition of the two arrays. so when we partitions these two arrays, we get 2 subarrays for each array, nums1 (1), nums1 (2) and nums2 (1), nums2 (2). i is the index of the last value of nums1 (1). j is the index of the last value of nums2 (1).

#   # now it's good to take time to understand the formulas below. when we partition nums1, we try to find the middle value (if possible), and now how to partition nums2 in relation to partitioning nums1? well the idea is to find the median of nums1 + nums2, and assuming the arrays are both sorted in a perfect way - together in ascending order, the median should be (len(nums1)+len(nums2))/2 if we are lucky and the merged array is of odd length, but if it's of even length, then we have to do this: (len(nums1)+len(nums2) + 1)/2.. or do the ceil method. now to partition our second array we subtract the value for i from this formula (the formula of how to get the median of the combined arrays). here is an example of how we get i and j values:

#   # a = [1,2]--> i = 0 --> a[0] = 1
#   # b = [1,2,3]--> j = 1 --> b[1] = 2

#   # so [1] is a (1), [2] is a (2)
#   # and [1,2] is b (1), [3] is b (2)
 
#   # try to apply it to other arrays, it works!

#     nums1_index = math.ceil((min_index + max_index)/2) - 1
#     nums2_index = math.ceil((max_index + nums2_length)/2) - nums1_index - 1
#     print(' ')
#     print(nums1_index)
#     print(nums2_index)
#     print(' ')
    

#   # we try to add nums1 (1) and nums2 (1) togther in one group, and we add nums1 (2) and nums2 (2) in the other group. so let's say we have:
#   # nums1 = [1,2,3,4]
#   # nums2 = [5,6,7,8]

#   # after "partitioning" them, i of nums1 is 1, and j of nums2 is 1. this means nums1[i = 1] = 2, so nums1(1) is [1,2], and nums1(2) is [3,4] and nums2[j = 1] = 6, so nums2 (1) is [5,6] and nums2 (2) is [7,8]. now we try to combine nums1 (1) and nums2 (1) will be [1,2,5,6] and combining nums1 (2) and nums2 (2) we get [3,4,7,8]

#   # so we figure out that last element of nums2 (1) and first element of nums1 (2) will store the median value we will need!

#   # well now we figure out that we have to make sure that (nums1 (1) + nums2 (1)) has values lower than (nums1 (2) + nums2 (2)).

#   #what does that mean for our 4 subgroups? we have to have this order nums1 (1) < nums2 (1) < nums1 (2) < nums2 (2)

#   # first we compare nums1 (2) and nums2 (1)
#   # check if las value of nums2 (1) is bigger than the first value of nums1 (2) (that means the arrays are not sorted well!)

#     if (nums1_index < nums1_length and nums2_index >= 0 and nums2[nums2_index] > nums1[nums1_index+1] ):
#       print('here?')

#   # so let's go back to our first example, where we partitioned our arrays into these two groups [1,2,5,6] and [3,4,7,8]. by this condition we see that 6>3, so ler's see what happend if we update the max_index and go back to the 2nd iteration of our while loop!
      
#       min_index = nums1_index + 2
      

#     elif (nums2_index<nums2_length and nums1_index >= 0 and nums2[nums2_index+1] < nums1[nums1_index] ):
#       print('or here')
#       max_index = nums1_index - 2

#     else:

#       if (nums1_index < 0):
#         median = nums2[nums2_index]

#       elif (nums2_index <= 0):
#         print('here yes???')
#         median = nums1[nums1_index]
#         print(median)
      
#       else:
#         median = max(nums1[nums1_index],nums2[nums2_index])
#       break

#   if ((nums1_length+1)+(nums2_length+1))%2 == 1:
#     print('yo')
#     return median

#   if nums1_index==nums1_length:
#     print("oh")
#     print(median)
#     print(nums2[nums2_index])
#     return ((median + nums2[nums2_index + 1])/2.0)
  
#   # so now we try to partition the original 2 arrays again: max_index is i=1 + j = 2, so the new i is 0 and the new j is 2, so: nums1 (1) is [1] nums1 (2) is [2,3,4], then nums2 (1) is [5,6,7] and nums2 (2) is [8]. now we check again what we did before: is 7>2, yes so we increase max_index to be 1, so we partition again. 

#   if nums2_index==nums2_length:
#     print('what')
#     return (median+nums1[nums1_index+1])/2.0
  
#   print('brmmm')
#   print(nums1[nums1_index+1])
#   print(nums2[nums2_index+1])
#   return (median + minimum(nums1[nums1_index+1],nums2[nums2_index+1]))/2.0
# # print(median_2arrays([2,3,5,8],[10,12,14,16,18,20]))
# # print(median_2arrays([1,2],[1,2,3]))

# # def median_2arrays(nums1,nums2):
# #   # binary search algorithm! we have to try to partition the arrays!

# #   #we always try to have nums1 array to be smaller than nums2 array, so let's check that:
# #   if int(len(nums1)) > int(len(nums2)):
# #     nums1, nums2 = nums2, nums1
  
# #   # the way to partition arrays is to define the lengths of the arrays
# #   nums1_length = int(len(nums1))

# # print(median_2arrays([1,2,3,4],[5,6,7,8]))
# # print(median_2arrays([1],[5,6,7,8]))
# # print(median_2arrays([1],[5]))
# # print(findMedianSortedArrays([1],[5,6,7]))
# # print(findMedianSortedArrays([1,2],[5,6,7]))
# # print(findMedianSortedArrays([1,2,3],[5,6,7]))
# # print(findMedianSortedArrays([1,2,3],[5,6,7,8]))
# # print(findMedianSortedArrays([1,2,3,4,5],[5,6,7,8,9,10]))
# print(findMedianSortedArrays([1,2,3,4,5],[5,6,7,8,9,10,11,12,14]))


import math

class Solution(object):
    def findMedianSortedArrays(self,nums1, nums2) :
        if int(len(nums1)) > int(len(nums2)):
            nums1, nums2 = nums2, nums1

        median = 0
        nums1_length = int(len(nums1))
        nums2_length = int(len(nums2))

        min_index = 0
        max_index = nums1_length
      
        while min_index <= max_index:
            nums1_index = int((min_index + max_index) / 2)
            nums2_index = int(((nums1_length + nums2_length + 1) / 2) - nums1_index)

            if (nums1_index < nums1_length and nums2_index > 0 and nums2[nums2_index - 1] > nums1[nums1_index]) :
                min_index = nums1_index + 1

            elif (nums1_index > 0 and nums2_index < nums2_length and nums2[nums2_index] < nums1[nums1_index - 1]) :
                max_index = nums1_index - 1
          
            else :
                if (nums1_index == 0) :
                    median = nums2[nums2_index - 1]

                elif (nums2_index == 0) :
                    median = nums1[nums1_index - 1]   

                else :
                    median = max(nums1[nums1_index - 1], nums2[nums2_index - 1])
                break

        if ((nums1_length + nums2_length) % 2 == 1) :
            return median
 
        if (nums1_index == nums1_length) :
            return ((median + nums2[nums2_index]) / 2.0)

        if (nums2_index == nums2_length) :
            return ((median + nums1[nums1_index]) / 2.0)
      
        return ((median + min(nums1[nums1_index], nums2[nums2_index])) / 2.0)
