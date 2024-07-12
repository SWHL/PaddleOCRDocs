### 使用教程

```bash
pip install -r requirements.txt
mkdocs serve
```

### 注意事项

- 图像路径。
  - 中文文档：

    ```python
    # ✔ markdown格式
    ![](./images/1.png)

    <img src="./images/1.png" />
    ```

  - 英文文档：只能使用markdown格式来插入图像（正常路径即可）。因为i18n插件原因，html格式不能正确渲染。

- 表格前后要有空行，否则不能正确渲染
- 无序列表在标题行下面，可以正确渲染。在文本行下面不行，需要空出一行

### TODO

- [ ] Deploy部分文档统一补充
- [x] 文档顶部评论功能统一添加
- [ ] 文档中涉及到配置文件路径更正
- [x] whl文档移入博客部分
- [x] [推理文档](https://github.com/PaddlePaddle/PaddleOCR/blob/main/doc/doc_ch/inference_ppocr.md)如何处理？
- [x] 代码块添加行号
- [ ] 删除重复图像
- [ ] 压缩较大图像
