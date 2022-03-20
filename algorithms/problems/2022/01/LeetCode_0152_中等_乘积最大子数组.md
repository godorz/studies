## 乘积最大子数组（LeetCode-0152, 中等）
<!--{
    "tags": ["动态规划"],
    "来源": "LeetCode",
    "编号": "0152",
    "难度": "中等",
    "标题": "乘积最大子数组"
}-->

<summary><b>问题简述</b></summary>

```txt
给定整型数组，求乘积最大的非空连续子数组，返回乘积；
```

<details><summary><b>详细描述</b></summary>

```txt
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:
    输入: [2,3,-2,4]
    输出: 6
    解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
    输入: [-2,0,-1]
    输出: 0
    解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
```

</details>

<!-- <div align="center"><img src="../../../_assets/xxx.png" height="300" /></div> -->

<summary><b>思路：动态规划</b></summary>

- 延续连续子数组最大和的思路，定义 `dp[i]` 表示以 `nums[i]` 结尾的连续最大乘积；
- 区别在于非0值乘以负数时，最大值会变最小值，最小值变最大值；
- 因此可以考虑定义两个 dp：`dp_max[i]` 和 `dp_min[i]` 分别表示最大和最小乘积（详见代码）；
- 本题同样可以使用“滚动变量”的方式降低空间复杂度；

<details><summary><b>Python</b></summary>

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ret = dp_max = dp_min = nums[0]
        for x in nums[1:]:
            tmp_mx = dp_max  # 临时变量
            dp_max = max(x, dp_max * x, dp_min * x)
            dp_min = min(x, dp_min * x, tmp_mx * x)
            ret = max(ret, dp_max)
        
        return ret
```

</details>

