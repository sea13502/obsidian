# 第 37 页
 | [[page_036|« 上一页]] | [[../README|📖 回到书页]] | [[page_038|下一页 »]]
![第37页](../images/MachineLearningQandAI_page_037.jpg)



---

 | [[page_036|« 上一页]] | [[../README|📖 回到书页]] | [[page_038|下一页 »]]


---

corresponding to the category’s index, and 0 in all other positions.  
对应于类别的索引位置为1，其余所有位置均为0。

This ensures that the categorical values are represented in a way that certain machine learning algorithms can process.  
这确保了分类值以某种形式表示，使得某些机器学习算法可以处理。

For example, if we have a categorical variable Color with three categories, Red, Green, and Blue,  
例如，如果我们有一个分类变量“颜色”，包含三个类别：红色、绿色和蓝色，

the one-hot encoding would represent Red as [1, 0, 0], Green as [0, 1, 0], and Blue as [0, 0, 1].  
独热编码会将红色表示为 [1, 0, 0]，绿色为 [0, 1, 0]，蓝色为 [0, 0, 1]。

These one-hot encoded categorical variables can then be mapped into continuous embedding vectors by utilizing the learned weight matrix of an embedding layer or module.  
![[Vox_1780136183627.wav]]
这些独热编码的分类变量可以通过使用嵌入层或模块中学习到的权重矩阵，映射为连续的嵌入向量。

We can also use ==embedding methods== for dense data such as images.  
我们也可以将嵌入方法用于图像等密集数据。

For example, the last layers of a convolutional neural network may **yield** embedding vectors, as illustrated in Figure 1-1.  
例如，卷积神经网络的最后一层可能产生嵌入向量，如图1-1所示。

Figure 1-1: An input embedding (left) and an embedding from a neural network (right)  
图1-1：输入嵌入（左）和神经网络生成的嵌入（右）

To be technically correct, all ==intermediate layer outputs== of a neural network could yield ==embedding vectors==.  
从技术上讲，神经网络的所有中间层输出都可能生成嵌入向量。

Depending on the training objective, the output layer may also produce useful embedding vectors.  
根据训练目标的不同，输出层也可能产生有用的嵌入向量。

For the sake of simplicity, the convolutional neural network in Figure 1-1 associates the second-to-last layer with embeddings.  
为了简化说明，图1-1中的卷积神经网络将倒数第二层与嵌入向量关联起来。

Embeddings can have higher or lower numbers of dimensions than the original input.  
嵌入向量的维度可以高于或低于原始输入的维度。

For instance, using embeddings methods for extreme expression, we can encode data into two-dimensional dense and continuous representations for ==visualization purposes== and ==clustering analysis==, as illustrated in Figure 1-2.  ![[Vox_1780152305727.wav]]
例如，为了极端表达，我们可以将数据编码为二维的稠密且连续的表示，用于可视化和聚类分析，如图1-2所示。

---

✅ **附注说明**：
- 图1-1展示了两种嵌入方式：
  - 左边：通过独热编码 → 嵌入层 → 稠密向量（如词嵌入）
  - 右边：图像经过卷积层后提取出的特征向量作为嵌入
- 图1-2未显示，但通常用于展示降维后的可视化结果（如t-SNE图）



> 对应类别索引的位置为1，其余所有位置为0。这种表示方式能让机器学习算法处理类别型数据。
> 举个例子：如果有一个颜色变量Color，包含红、绿、蓝三个类别，那么独热编码会表示为：
> - 红：`[1, 0, 0]`
> - 绿：`[0, 1, 0]`
> - 蓝：`[0, 0, 1]`
> 这些独热编码的类别变量，可以通过嵌入层/模块中学习到的权重矩阵，映射成连续的嵌入向量。

> 我们也可以用嵌入方法处理图像这类稠密数据。比如，卷积神经网络（CNN）的最后几层，就可以输出嵌入向量，如图1-1所示。

> 从技术上讲，神经网络的所有中间层输出都可以被视为嵌入向量。根据训练目标的不同，输出层也可能产生有价值的嵌入向量。为了简化说明，图1-1中的卷积神经网络将倒数第二层作为嵌入层。

> 嵌入的维度可以比原始输入更高或更低。例如，为了可视化和聚类分析，我们可以将数据编码为二维的稠密连续表示，如图1-2所示。
