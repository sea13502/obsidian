# 第 42 页

![第42页](../images/MachineLearningQandAI_page_042.jpg)



---

 | [[page_041|« 上一页]] | [[../README|📖 回到书页]] | [[page_043|下一页 »]]

### 🔹 图 2-1：传统迁移学习的预训练过程

> **Figure 2-1: Pretraining with conventional transfer learning**  
> 图2-1：使用传统迁移学习进行预训练

> 📌 **图示结构说明**： 整个流程分为三个阶段，用数字标注：

#### ✅ (1) Pretraining（预训练）

- 输入：**大型通用数据集**（如 ImageNet）
- 包含：训练样本 + 标签
- 模型初始化：随机权重
- 输出：**预训练模型**

> 💡 这一步是关键：利用大规模标注数据让模型学会通用特征（如边缘、纹理、物体轮廓）。

#### ✅ (2) Transfer（迁移）

- 将预训练模型作为起点，迁移到新的任务上
- 新任务使用**目标特定的数据集**（如鸟种分类）

> 🔁 思路：“先学通用知识，再学专业技能”

#### ✅ (3) Training (fine-tuning) on target dataset（在目标数据集上微调）

- 使用新数据集的训练样本和标签
- 对预训练模型进行**微调**（fine-tuning）
- 输出：**最终模型**

> ⚠️ 注意：通常只更新最后一层（输出层），前面的卷积层保持不变或缓慢更新。

---

### 🔹 正文第一句

> **Self-supervised learning is an alternative approach to transfer learning in which the model is pretrained not on labeled data but on unlabeled data.**  
> 自监督学习是一种替代迁移学习的方法，其模型不是在标注数据上预训练，而是在未标注数据上预训练。

> ✅ 解释：
> 
> - **传统迁移学习**：依赖大量标注数据（如 ImageNet）
> - **自监督学习**：可以利用海量无标签数据（如互联网上的图片、文本）
> - 两者都属于“预训练 + 微调”范式，但数据来源不同

---

### 🔹 第二句

> **We consider an unlabeled dataset for which we do not have label information, and then we find a way to obtain labels from the dataset’s structure to formulate a prediction task for the neural network, as illustrated in Figure 2-2.**  
> 我们考虑一个没有标签信息的未标注数据集，然后找到一种方法，从数据集的结构中获取“伪标签”，从而为神经网络构建一个预测任务，如图2-2所示。

> 💡 关键思想：
> 
> - 虽然没有真实标签，但可以通过**数据本身的结构**生成“代理任务”（pretext task）
> - 例如：
>     - 遮住图像的一部分 → 让模型预测缺失区域（掩码重建）
>     - 打乱句子顺序 → 让模型恢复正确顺序（语言建模）
>     - 给出两个视角的图像 → 判断是否来自同一对象（对比学习）

> 🎯 目标：让模型学会有用的表示，而不依赖人工标注。

---

### 🔹 第三句

> **These self-supervised training tasks are also called pretext tasks.**  
> 这些自监督训练任务也被称为“代理任务”（pretext tasks）。

> ✅ 定义澄清：
> 
> - **Pretext Task（代理任务）**：为了学习有用表示而设计的临时任务，本身不一定是最终目标。
> - 例如：你在学习英语时，可能通过“填空题”来练习语法，这个“填空”就是代理任务。
> - 最终目标可能是“写作文”或“对话”，但“填空”帮助你掌握语言规则。

> 🧩 类比：
> 
> - 自监督学习中的“代理任务”就像“填空”
> - 最终任务（如图像分类）才是“写作文”

---

### ✅ 总结要点

|概念|内容|
|---|---|
|**传统迁移学习**|用标注数据预训练 → 微调到新任务|
|**自监督学习**|用无标签数据 + 代理任务预训练 → 微调到新任务|
|**代理任务（pretext task）**|从数据结构中构造的“假任务”，用于生成监督信号|
|**优势**|大幅减少对标注数据的依赖，适合大规模无标签数据场景|

---

### 🔄 两种方法对比表

|特性|传统迁移学习|自监督学习|
|---|---|---|
|数据类型|必须有标签|可以无标签|
|预训练方式|直接分类任务|构造代理任务（如重建、对比）|
|应用场景|ImageNet 等标注数据集|Web 图片、社交媒体文本等无标签数据|
|典型模型|ResNet、BERT（基于标注数据）|MAE、SimCLR、BYOL（基于无标签数据）|

---

### 📚 补充知识：什么是“proxy task”？

> “Proxy task” 是指**用来间接学习目标任务所需能力的任务**。它不是最终目标，但能帮助模型学到通用特征。

#### 常见的 proxy task 示例：

|任务|说明|
|---|---|
|**Masked Autoencoding**|遮住图像/文本部分，预测缺失内容（如MAE、BERT）|
|**Rotation Prediction**|预测图像旋转角度（如90°、180°）|
|**Colorization**|黑白图像上色 → 学习颜色语义|
|**Contrastive Learning**|判断两幅图是否来自同一对象（如SimCLR）|

> 💡 所有这些任务都能让模型学会“看懂世界”，即使没有人类标签。

---

### ✅ 总结一句话：

> **自监督学习通过设计“代理任务”（pretext tasks），从无标签数据中提取有用信息，实现无需人工标注的预训练，是当前大模型（如LLM、ViT）成功的关键技术之一。**

---

如果您希望我继续分析 **Figure 2-2** 或讲解具体的自监督学习算法（如MAE、SimCLR），欢迎继续提问！