# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        i = 0
        j = 0
        l = []
        l1 = len(nums1)
        l2 = len(nums2)
        while (i<l1) and (j<l2):
            if nums1[i] < nums2[j]:
                l.append(nums1[i])
                i += 1
            elif nums1[i] == nums2[j]:
                l.append(nums1[i])
                l.append(nums2[j])
                i += 1
                j += 1
            else:
                l.append(nums2[j])
                j += 1
        if i==l1:
            while j<l2:
                l.append(nums2[j])
                j += 1
        if j==l2:
            while i<l1:
                l.append(nums1[i])
                i += 1
        if (l1+l2) % 2 == 1:
            print("Odd")
            return float(l[int((l1+l2-1)/2)])
        else:
            print("Even")
            print(l[int((l1+l2)/2 -1 )])
            print(l[int((l1 + l2) / 2)])
            return float((l[int((l1+l2)/2 -1 )]+l[int((l1+l2)/2)])/2)

if __name__ == '__main__':
    a = Solution()
    print(a.findMedianSortedArrays([1,2], [3,4]))