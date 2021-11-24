'''
0 <= firstList.length, secondList.length <= 1000
firstList.length + secondList.length >= 1
0 <= starti < endi <= 10**9
endi < starti + 1
0 <= startj < endj <= 109
endj < startj + 1


https://leetcode.com/problems/interval-list-intersections/discuss/1593579/JAVA-or-Two-Pointers-or-Most-Intutive
https://leetcode.com/problems/interval-list-intersections/
'''
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersections, i, j = [], 0, 0
        len_firstList = len(firstList)
        len_secondList = len(secondList)
        condicao_1 = len_firstList >= 0 and len_firstList <= 1000
        condicao_2 = len_secondList >= 0 and len_secondList <= 1000
        condicao_3 = len_secondList + len_firstList >= 1

        if condicao_1 and condicao_2 and condicao_3:

            while i < len(firstList) and j < len(secondList):
                if firstList[i][0] >= 0 \
                        and firstList[i][0] < firstList[i][1] \
                        and firstList[i][1] <= 10 ** 9 \
                        and secondList[j][0] >= 0 \
                        and secondList[j][0] < secondList[j][1] \
                        and firstList[i][1] <= 10 ** 9 :

                    if firstList[i][1] >= secondList[j][0] and firstList[i][0] <= secondList[j][1]:
                        intersections.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])
                    if firstList[i][1] < secondList[j][1]:
                        i += 1
                    else:
                        j += 1
        return intersections


if __name__ == '__main__':
    solution = Solution()
    firstList = [[4, 6], [7, 8], [10, 17]]
    secondList = [[5, 10]]
    intersections = solution.intervalIntersection(firstList, secondList)
    print(intersections)