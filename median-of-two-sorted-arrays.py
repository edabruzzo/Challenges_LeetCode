import heapq
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        minheap, maxheap = [], []

        '''
        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -106 <= nums1[i], nums2[i] <= 106
        '''
        m = len(nums1)
        n = len(nums2)

        condicoes_satisfeitas_1 = False
        condicoes_satisfeitas_2 = False
        condicoes_satisfeitas_3 = False

        condicoes_satisfeitas_1 = (m >=0
                                 and m <= 1000
                                 and n >= 0
                                 and n<=1000
                                 and m+n >=1 and m+n <=2000)

        for index in range(len(nums1)):
            if nums1[index] >= -10**6 and nums1[index]<=10**6:
                condicoes_satisfeitas_2 = True

        for index in range(len(nums2)):
            if nums2[index] >= -10 ** 6 and nums2[index] <= 10 ** 6:
                condicoes_satisfeitas_3 = True

        condicoes_satisfeitas = (condicoes_satisfeitas_1
                                 and condicoes_satisfeitas_2
                                 and condicoes_satisfeitas_3)

        if condicoes_satisfeitas:
            p1, p2 = 0, 0

            while p1 < len(nums1) or p2 < len(nums2):

                if p1 == len(nums1):
                    heapq.heappush(minheap, nums2[p2])
                    p2 += 1
                elif p2 == len(nums2):
                    heapq.heappush(minheap, nums1[p1])
                    p1 += 1
                elif nums1[p1] < nums2[p2]:
                    heapq.heappush(minheap, nums1[p1])
                    p1 += 1
                else:
                    heapq.heappush(minheap, nums2[p2])
                    p2 += 1
                if len(minheap) > len(maxheap):
                    heapq.heappush(maxheap, -heapq.heappop(minheap))

            return (minheap[0] - maxheap[0]) / 2 if len(minheap) == len(maxheap) else -maxheap[0]



if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([],[0]))