Embedding vectors, or embeddings for short, encode relatively high-dimensional data into
relatively low-dimensional vectors.

We can apply embedding methods to create a continuous dense (non-sparse) vector from a
(sparse) one-hot encoding. One-hot encoding is a method used to represent categorical data as
binary vectors, where each category is mapped to a vector containing 1 in the position

嵌入向量（行业内简称“嵌入”），核心作用是**将高维的原始数据，编码为维度更低的稠密向量**。

我们可以通过嵌入方法，从（高度稀疏的）独热编码中，生成连续的、非稀疏的稠密向量。**独热编码**是类别型数据的基础表示方法：它将每个类别映射为一个二进制向量，该类别对应的向量位置取值为1，其余所有位置均为0。

![第36页|621](../images/MachineLearningQandAI_page_036.jpg)