---
comments: true
---

### 更新

#### 2022.5.9 发布PaddleOCR v2.5。发布内容包括

- [PP-OCRv3](./ppocr_introduction.md#pp-ocrv3)，速度可比情况下，中文场景效果相比于PP-OCRv2再提升5%，英文场景提升11%，80语种多语言模型平均识别准确率提升5%以上；
- 半自动标注工具[PPOCRLabelv2](https://github.com/PFCCLab/PPOCRLabel)：新增表格文字图像、图像关键信息抽取任务和不规则文字图像的标注功能；
- OCR产业落地工具集：打通22种训练部署软硬件环境与方式，覆盖企业90%的训练部署环境需求
- 交互式OCR开源电子书[《动手学OCR》](./ocr_book.md)，覆盖OCR全栈技术的前沿理论与代码实践，并配套教学视频。

#### 2022.5.7 添加对[Weights & Biases](https://docs.wandb.ai/)训练日志记录工具的支持

#### 2021.12.21 《OCR十讲》课程开讲，12月21日起每晚八点半线上授课！ 【免费】报名地址：<https://aistudio.baidu.com/aistudio/course/introduce/25207>

#### 2021.12.21 发布PaddleOCR v2.4。OCR算法新增1种文本检测算法（PSENet），3种文本识别算法（NRTR、SEED、SAR）；文档结构化算法新增1种关键信息提取算法（SDMGR），3种DocVQA算法（LayoutLM、LayoutLMv2，LayoutXLM）

#### 2021.9.7 发布PaddleOCR v2.3，发布[PP-OCRv2](#PP-OCRv2)，CPU推理速度相比于PP-OCR server提升220%；效果相比于PP-OCR mobile 提升7%

#### 2021.8.3 发布PaddleOCR v2.2，新增文档结构分析[PP-Structure](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/ppstructure/README_ch.md)工具包，支持版面分析与表格识别（含Excel导出）

#### 2021.6.29 [FAQ](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/doc/doc_ch/FAQ.md)新增5个高频问题，总数248个，每周一都会更新，欢迎大家持续关注

#### 2021.4.8 release 2.1版本，新增AAAI 2021论文[端到端识别算法PGNet](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/doc/doc_ch/pgnet.md)开源，[多语言模型](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.2/doc/doc_ch/multi_languages.md)支持种类增加到80+

#### 2020.12.15 更新数据合成工具[Style-Text](https://github.com/PFCCLab/StyleText/blob/main/README_ch.md)，可以批量合成大量与目标场景类似的图像，在多个场景验证，效果明显提升

#### 2020.12.07 [FAQ](../../doc/doc_ch/FAQ.md)新增5个高频问题，总数124个，并且计划以后每周一都会更新，欢迎大家持续关注

#### 2020.11.25 更新半自动标注工具[PPOCRLabel](https://github.com/PFCCLab/PPOCRLabel/blob/main/README_ch.md)，辅助开发者高效完成标注任务，输出格式与PP-OCR训练任务完美衔接

#### 2020.9.22 更新PP-OCR技术文章，<https://arxiv.org/abs/2009.09941>

#### 2020.9.19 更新超轻量压缩ppocr_mobile_slim系列模型，整体模型3.5M(详见PP-OCR Pipeline)，适合在移动端部署使用

#### 2020.9.17 更新超轻量ppocr_mobile系列和通用ppocr_server系列中英文ocr模型，媲美商业效果

#### 2020.9.17 更新[英文识别模型](./models_list.md#english-recognition-model)和[多语种识别模型](./models_list.md#english-recognition-model)，已支持`德语、法语、日语、韩语`，更多语种识别模型将持续更新

#### 2020.8.26 更新OCR相关的84个常见问题及解答，具体参考[FAQ](./FAQ.md)

#### 2020.8.24 支持通过whl包安装使用PaddleOCR，具体参考[Paddleocr Package使用说明](https://github.com/PaddlePaddle/PaddleOCR/blob/develop/doc/doc_ch/whl.md)

#### 2020.8.21 更新8月18日B站直播课回放和PPT，课节2，易学易用的OCR工具大礼包，[获取地址](https://aistudio.baidu.com/aistudio/education/group/info/1519)

#### 2020.8.16 开源文本检测算法[SAST](https://arxiv.org/abs/1908.05498)和文本识别算法[SRN](https://arxiv.org/abs/2003.12294)

#### 2020.7.23 发布7月21日B站直播课回放和PPT，课节1，PaddleOCR开源大礼包全面解读，[获取地址](https://aistudio.baidu.com/aistudio/course/introduce/1519)

#### 2020.7.15 添加基于EasyEdge和Paddle-Lite的移动端DEMO，支持iOS和Android系统

#### 2020.7.15 完善预测部署，添加基于C++预测引擎推理、服务化部署和端侧部署方案，以及超轻量级中文OCR模型预测耗时Benchmark

#### 2020.7.15 整理OCR相关数据集、常用数据标注以及合成工具

#### 2020.7.9 添加支持空格的识别模型，识别效果，预测及训练方式请参考快速开始和文本识别训练相关文档

#### 2020.7.9 添加数据增强、学习率衰减策略,具体参考[配置文件](./config.md)

#### 2020.6.8 添加[数据集](dataset/datasets.md)，并保持持续更新

#### 2020.6.5 支持 `attetnion` 模型导出 `inference_model`

#### 2020.6.5 支持单独预测识别时，输出结果得分

#### 2020.5.30 提供超轻量级中文OCR在线体验

#### 2020.5.30 模型预测、训练支持Windows系统

#### 2020.5.30 开源通用中文OCR模型

#### 2020.5.14 发布[PaddleOCR公开课](https://www.bilibili.com/video/BV1nf4y1U7RX?p=4)

#### 2020.5.14 发布[PaddleOCR实战练习](https://aistudio.baidu.com/aistudio/projectdetail/467229)

#### 2020.5.14 开源8.6M超轻量级中文OCR模型
