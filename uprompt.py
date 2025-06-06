Role = """你是一位专业临床试验DM,擅长解答临床实验数据问题."""
VariableIdentified = """
--后缀格式

表示变量必须以指定后缀结尾，且前缀部分必须与Domain名严格一致。

示例：规则 --LLT

满足 AELLT（Domain=AE + 后缀LLT）
不满足 XXLLT（前缀XX与Domain名无关）

*后缀格式

表示变量必须以指定后缀结尾，但前缀部分可以是任意合法字符。

示例：规则 *DTC

满足 AEDTC、SVDTC、ASDTC（均以DTC结尾）
"""

ODMTerm = """
Domain: 指按特定主题分类的一组相关数据.
Variable: 指Domain中的具体数据项或字段,用于记录特定的测量值或观察结果.
Domain 和 Vairable 的关系：一个Domain包含多个相关的Variable.
"""