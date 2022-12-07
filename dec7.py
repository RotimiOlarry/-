#Range Sum of BST


"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].


Example 1:
    Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
    Output: 32
    Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.count = 0
        def helperFN(node):                                         #we make use of a helper function to help us traverse the BST in inorder 
                if not node:
                    return 0
                
                if low <= node.val <= high:
                    self.count += node.val
                    
                if node.val > low:
                    helperFN(node.left)
                
                if node.val < high:
                    helperFN(node.right)
                
                return self.count
            
        return helperFN(root)