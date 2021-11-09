# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def sumOfLeftLeavesX(self, root: TreeNode) -> int:
        def helper(root, contabilizar=False, acumulador=[]):
            if root is None:
                return 0
            if root.left is None and root.right is None and root.val is not None and contabilizar:
                acumulador.append(root.val)
            helper(root.left, True)
            helper(root.right, False)
            return sum(acumulador)

        return helper(root)

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is not None:
            root.left.val += root.left.val
        return sum(acumulador)
        return helper(root)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        if (m >= 0 and m <= 1000) and (n <= 0 and n >= 1000) and (m + n >= 1 and m + n <= 2000):
            lista_merged = sorted(nums1.append(nums2))
            x = len(lista_merged)
            elementos_1 = lista_merged[x // 2 - 1:x // 2 + 1]
            elementos_2 = lista_merged[x // 2]
            median = float(sum(elementos_1, elementos_2)[x % 2]) if x else None
            return median

    def sumNumbers(self, root: TreeNode) -> int:

        if root is None:
            return 0

        if root.left is not None:
            root.left.val = root.val * 10 + root.left.val
            # print(" Valor à esquerda %d" %(root.left.val))
        else:
            # print('Encontrou um nulo à esquerda %d' % (root.val))
            pass
        if root.right is not None:
            root.right.val = root.val * 10 + root.right.val
            # print(" Valor à direita %d" %(root.right.val))
        else:
            # print('Encontrou um nulo à direita %d' % (root.val))
            pass

        if (root.right is None and root.left is None and root.val is not None):
            # print('%d' % (root.val))
            return root.val

        valorEsquerda = self.sumNumbers(root.left)
        valorDireita = self.sumNumbers(root.right)

        return valorEsquerda + valorDireita


if __name__ == '__main__':
    solution = Solution()

    '''
    root = TreeNode(val=0, left=TreeNode(val=1))
    print(solution.sumNumbers(root))


    leaf5 = TreeNode(val=5)
    leaf1 = TreeNode(val=1)
    leaf0 = TreeNode(val=0)
    leaf9 = TreeNode(val=9, left=leaf5, right=leaf1)
    root = TreeNode(val=4, left=leaf9, right=leaf0)
    print(solution.sumNumbers(root))



    node9 = TreeNode(val=9)
    node20 = TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7))
    #root = TreeNode(val=3, left=node9, right=node20)

    node3 = TreeNode(val=3, left=TreeNode(val=4), right=TreeNode(val=5))
    root = TreeNode(val=1, left=TreeNode(val=2), right=node3)

    soma = solution.sumOfLeftLeaves(root)
    print(soma)

    '''

    solution.findMedianSortedArrays([1, 2, 3], [4, 5, 6])


