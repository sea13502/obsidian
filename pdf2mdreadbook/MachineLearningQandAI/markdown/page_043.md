# 第 43 页

![第43页](../images/MachineLearningQandAI_page_043.jpg)



---

 | [[page_042|« 上一页]] | [[../README|📖 回到书页]] | [[page_044|下一页 »]]

图表内容翻译：

*   Large, general dataset: 大规模通用数据集
    *   Training examples: 训练样本
    *   Extract, "make": 提取，“制造”
    *   Labels: 标签 (虚线框表示由样本提取/制造而来)
*   Model: 模型 rightarrow Pretrained model: 预训练模型
*   (1) Self-supervised pretraining: (1) 自监督预训练
*   Target-specific dataset: 特定目标数据集
    *   Training examples: 训练样本
    *   Labels: 标签
*   Pretrained model: 预训练模型 rightarrow Final model: 最终模型
*   (2) Transfer: (2) 迁移
*   (3) Training (fine-tuning) on target dataset: (3) 在目标数据集上训练（微调）

图 2-2：使用自监督学习进行预训练

迁移学习和自监督学习之间的主要区别在于我们在图 2-1 和图 2-2 的步骤 1 中如何获取标签。在迁移学习中，我们假设标签是随数据集一起提供的；它们通常由人工标注员创建。而在自监督学习中，标签可以直接从训练样本中推导出来。

自监督学习任务可以是自然语言处理上下文中的缺失词预测。例如，给定句子“It is beautiful and sunny outside”（外面美丽且阳光明媚），我们可以掩盖单词 sunny，向网络输入“It is beautiful and [MASK] outside”（外面美丽且 [MASK]），并让网络预测“[MASK]”位置的缺失单词。同样，我们可以在计算机视觉上下文中移除图像块，并让神经网络填补空白。这只是自监督学习任务的两个例子；此类学习还存在许多其他方法和范式。

总之，我们可以将前置任务上的自监督学习视为表示学习。