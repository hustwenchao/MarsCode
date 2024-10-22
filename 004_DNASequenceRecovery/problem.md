# 问题描述

给定一段受损的 DNA 碱基序列 dna1，在每次只操作一个碱基的情况下，将其以最少的操作步骤将其还原到未受损的 DNA 碱基序列 dna2。

只可以对 DNA 碱基序列中的一个碱基进行三种操作：
1. 增加一个碱基
2. 去除一个碱基
3. 替换一个碱基

## 输入描述:

输入两段 DNA 碱基序列，每段分一行输入

第一行为第一段受损的 DNA 碱基序列 dna1

第二行为第二段未受损的 DNA 碱基序列 dna2

## 输出描述:

最小操作步骤数

**备注**:

0 <= dna1.length, dna2.length <= 500

dna1 和 dna2 由大写英文字母 A、G、C、T 组成

**示例 1**

**输入**

AGCTTAGC

AGCTAGCT

**输出**

2

**说明**

AGCTTAGC -> AGCTAGC（删除 T）

AGCTAGC -> AGCTAGCT（增加 T）


**示例 2**

**输入**

AGCCGAGC

GCTAGCT

**输出**

4

**说明**

AGCCGAGC -> GCCGAGC（删除 A）

GCCGAGC -> GCTGAGC（将 C 替换为 T）

GCTGAGC -> GCTAGC（删除 G）

GCTAGC -> GCTAGCT（增加 T）


---- DeepSeek 的解释 ----

要解决这个问题，我们可以使用动态规划来计算两个 DNA 序列之间的编辑距离（Levenshtein 距离）。编辑距离是指将一个字符串转换为另一个字符串所需的最少操作次数，操作包括插入、删除和替换。

我们可以使用一个二维数组 dp，其中 dp[i][j] 表示将 dna1 的前 i 个字符转换为 dna2 的前 j 个字符所需的最少操作次数。

动态规划的状态转移方程如下：

如果 dna1[i-1] == dna2[j-1]，则 dp[i][j] = dp[i-1][j-1]，因为不需要任何操作。

否则，dp[i][j] 可以通过以下三种操作中的最小值来计算：

插入：dp[i][j-1] + 1

删除：dp[i-1][j] + 1

替换：dp[i-1][j-1] + 1

初始条件：

dp[0][j] = j，因为将空字符串转换为 dna2 的前 j 个字符需要 j 次插入操作。

dp[i][0] = i，因为将 dna1 的前 i 个字符转换为空字符串需要 i 次删除操作。

最终答案是 dp[len(dna1)][len(dna2)]。