<!--{
    "tags": ["TreeDP"],
    "来源": "LeetCode",
    "难度": "简单",
    "编号": "110",
    "标题": "平衡二叉树",
    "公司": []
}-->

<summary><b>问题简述</b></summary>

```txt
给定一个二叉树，判断它是否是高度平衡的二叉树。
本题中，一棵高度平衡二叉树定义为：
    一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
```
> [110. 平衡二叉树 - 力扣（LeetCode）](https://leetcode-cn.com/problems/balanced-binary-tree/)

<!-- 
<details><summary><b>详细描述</b></summary>

```txt
```
-->

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路：树形DP</b></summary>

- 考虑对以 X 为头结点的树，为了确定其是否为平衡二叉树，需要从左右子树获取哪些信息？
- 根据定义，显然需要知道两个信息：
    1. 子树是否为平衡二叉树（`is_balanced: bool`）；
    2. 子树的高度（`height: int`）；
- 对空节点，有：
    ```python
    is_balanced = True
    height = 0
    ```

<details><summary><b>Python</b></summary>

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        from collections import namedtuple

        # 用一个结构来组织需要的信息，可以直接用 tuple，这里是为了更直观
        Info = namedtuple('Info', ['is_balanced', 'height'])

        def dfs(x):
            if not x:  # 空节点
                return Info(True, 0)
            
            l, r = dfs(x.left), dfs(x.right)
            is_balanced = abs(l.height - r.height) <= 1 and l.is_balanced and r.is_balanced
            height = max(l.height, r.height) + 1
            return Info(is_balanced, height)
        
        return dfs(root).is_balanced  # 返回需要的信息
```

</details>

