---
comments: true
hide:
  - navigation
  - toc
---

<div align="center">
 <img src="https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/doc/PaddleOCR_log.png" align="middle" width = "600"/>
  <p align="center">
      <a href="https://discord.gg/z9xaRVjdbD"><img src="https://img.shields.io/badge/Chat-on%20discord-7289da.svg?sanitize=true" alt="Chat"></a>
      <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache%202-dfd.svg"></a>
      <a href="https://github.com/PaddlePaddle/PaddleOCR/releases"><img src="https://img.shields.io/github/v/release/PaddlePaddle/PaddleOCR?color=ffa"></a>
      <a href=""><img src="https://img.shields.io/badge/python-3.7+-aff.svg"></a>
      <a href=""><img src="https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg"></a>
      <a href="https://pypi.org/project/PaddleOCR/"><img src="https://img.shields.io/pypi/dm/PaddleOCR?color=9cf"></a>
      <a href="https://github.com/PaddlePaddle/PaddleOCR/stargazers"><img src="https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?color=ccf"></a>
  </p>
</div>


## 简介
PaddleOCR 旨在打造一套丰富、领先、且实用的 OCR 工具库，助力开发者训练出更好的模型，并应用落地。

## 🚀 社区
PaddleOCR 由 [PMC](https://github.com/PaddlePaddle/PaddleOCR/issues/12122) 监督。Issues 和 PRs 将在尽力的基础上进行审查。欲了解 PaddlePaddle 社区的完整概况，请访问 [community](https://github.com/PaddlePaddle/community)。

⚠️注意：[Issues](https://github.com/PaddlePaddle/PaddleOCR/issues)模块仅用来报告程序🐞Bug，其余提问请移步[Discussions](https://github.com/PaddlePaddle/PaddleOCR/discussions)模块提问。如所提Issue不是Bug，会被移到Discussions模块，敬请谅解。

## 📣 近期更新
- **📚直播和OCR实战打卡营预告**：《PP-ChatOCRv2赋能金融报告信息智能化抽取，新金融效率再升级》课程上线，破解复杂版面、表格识别、信息抽取OCR解析难题，直播时间：6月6日（周四）19：00。并于6月11日启动【政务采购合同信息抽取】实战打卡营。报名链接：https://www.wjx.top/vm/eBcYmqO.aspx?udsid=197406
- **🔥2024.5.10 上线星河零代码产线(OCR 相关)**：全面覆盖了以下四大 OCR 核心任务，提供极便捷的 Badcase 分析和实用的在线体验：
  - [通用 OCR](https://aistudio.baidu.com/community/app/91660) (PP-OCRv4)。
  - [通用表格识别](https://aistudio.baidu.com/community/app/91661) (SLANet)。
  - [通用图像信息抽取](https://aistudio.baidu.com/community/app/91662) (PP-ChatOCRv2-common)。
  - [文档场景信息抽取](https://aistudio.baidu.com/community/app/70303) (PP-ChatOCRv2-doc)。

  同时采用了 **[全新的场景任务开发范式](https://aistudio.baidu.com/pipeline/mine)** ,将模型统一汇聚，实现训练部署的零代码开发，并支持在线服务化部署和导出离线服务化部署包。

<details>
<summary>更多</summary>

- **🔥2023.8.7 发布 PaddleOCR [release/2.7](https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.7)**
    - 发布[PP-OCRv4](./doc/doc_ch/PP-OCRv4_introduction.md)，提供 mobile 和 server 两种模型
      - PP-OCRv4-mobile：速度可比情况下，中文场景效果相比于 PP-OCRv3 再提升 4.5%，英文场景提升 10%，80 语种多语言模型平均识别准确率提升 8%以上
      - PP-OCRv4-server：发布了目前精度最高的 OCR 模型，中英文场景上检测模型精度提升 4.9%， 识别模型精度提升 2%
      可参考[快速开始](./doc/doc_ch/quickstart.md) 一行命令快速使用，同时也可在飞桨 AI 套件(PaddleX)中的[通用 OCR 产业方案](https://aistudio.baidu.com/aistudio/modelsdetail?modelId=286)中低代码完成模型训练、推理、高性能部署全流程
- 🔨**2022.11 新增实现[4 种前沿算法](doc/doc_ch/algorithm_overview.md)**：文本检测 [DRRG](doc/doc_ch/algorithm_det_drrg.md),  文本识别 [RFL](doc/doc_ch/algorithm_rec_rfl.md), 文本超分[Text Telescope](doc/doc_ch/algorithm_sr_telescope.md)，公式识别[CAN](doc/doc_ch/algorithm_rec_can.md)
- **2022.10 优化[JS 版 PP-OCRv3 模型](./deploy/paddlejs/README_ch.md)**：模型大小仅 4.3M，预测速度提升 8 倍，配套 web demo 开箱即用
- **💥 直播回放：PaddleOCR 研发团队详解 PP-StructureV2 优化策略**。微信扫描[下方二维码](#开源社区)，关注公众号并填写问卷后进入官方交流群，获取直播回放链接与 20G 重磅 OCR 学习大礼包（内含 PDF 转 Word 应用程序、10 种垂类模型、《动手学 OCR》电子书等）
- **🔥2022.8.24 发布 PaddleOCR [release/2.6](https://github.com/PaddlePaddle/PaddleOCR/tree/release/2.6)**
  - 发布[PP-StructureV2](./ppstructure/README_ch.md)，系统功能性能全面升级，适配中文场景，新增支持[版面复原](./ppstructure/recovery/README_ch.md)，支持**一行命令完成 PDF 转 Word**；
  - [版面分析](./ppstructure/layout/README_ch.md)模型优化：模型存储减少 95%，速度提升 11 倍，平均 CPU 耗时仅需 41ms；
  - [表格识别](./ppstructure/table/README_ch.md)模型优化：设计 3 大优化策略，预测耗时不变情况下，模型精度提升 6%；
  - [关键信息抽取](./ppstructure/kie/README_ch.md)模型优化：设计视觉无关模型结构，语义实体识别精度提升 2.8%，关系抽取精度提升 9.1%。
- 🔥**2022.8 发布 [OCR 场景应用集合](./applications)**：包含数码管、液晶屏、车牌、高精度 SVTR 模型、手写体识别等**9 个垂类模型**，覆盖通用，制造、金融、交通行业的主要 OCR 垂类应用。

> [更多](./doc/doc_ch/update.md)

</details>

## 🌟 特性
支持多种 OCR 相关前沿算法，在此基础上打造产业级特色模型[PP-OCR](./doc/doc_ch/ppocr_introduction.md)、[PP-Structure](./ppstructure/README_ch.md)和[PP-ChatOCRv2](https://aistudio.baidu.com/community/app/70303)，并打通数据生产、模型训练、压缩、预测部署全流程。

<div align="center">
    <img src="https://raw.githubusercontent.com/tink2123/test/master/ppocrv4.png">
</div>

## 效果展示
### 超轻量PP-OCRv3效果展示

![](./static/images/PP-OCRv3-pic001.jpg)

#### PP-OCRv3中文模型
<div align="center">
    <img src="./static/images/PP-OCRv3-pic001.jpg" width="800">
    <!-- <img src="./static/images/imgs_results/PP-OCRv3/ch/PP-OCRv3-pic002.jpg" width="800">
    <img src="./static/imgs_results/PP-OCRv3/ch/PP-OCRv3-pic003.jpg" width="800"> -->
</div>

#### PP-OCRv3英文数字模型
<div align="center">
    <img src="./static/imgs_results/PP-OCRv3/en/en_1.png" width="800">
    <img src="./static/imgs_results/PP-OCRv3/en/en_2.png" width="800">
    <img src="./static/imgs_results/PP-OCRv3/en/en_3.png" width="800">
</div>

#### PP-OCRv3多语言模型
<div align="center">
    <img src="./static/imgs_results/PP-OCRv3/multi_lang/japan_2.jpg" width="800">
    <img src="./static/imgs_results/PP-OCRv3/multi_lang/korean_1.jpg" width="800">
</div>


### 超轻量PP-OCRv2效果展示
<div align="center">
    <img src="./static/imgs_results/PP-OCRv2/PP-OCRv2-pic001.jpg" width="800">
    <img src="./static/imgs_results/PP-OCRv2/PP-OCRv2-pic002.jpg" width="800">
    <img src="./static/imgs_results/PP-OCRv2/PP-OCRv2-pic003.jpg" width="800">
</div>


### 通用PP-OCR server 2.0 效果展示
<div align="center">
    <img src="./static/imgs_results/ch_ppocr_mobile_v2.0/00006737.jpg" width="800">
    <img src="./static/imgs_results/ch_ppocr_mobile_v2.0/00009282.jpg" width="800">
    <img src="./static/imgs_results/ch_ppocr_mobile_v2.0/00015504.jpg" width="800">
</div>

### 英文识别模型效果展示
<div align="center">
    <img src="./static/imgs_results/ch_ppocr_mobile_v2.0/img_12.jpg" width="800">
</div>

### 多语言识别模型效果展示
<div align="center">
    <img src="./static/imgs_results/french_0.jpg" width="800">
    <img src="./static/imgs_results/korean.jpg" width="800">
</div>

## 许可证书
本项目的发布受<a href="https://github.com/PaddlePaddle/PaddleOCR/blob/master/LICENSE">Apache 2.0 license</a>许可认证。
