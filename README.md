### 使用教程
```bash
$ pip install -r requirements.txt
$ mkdocs serve
```

### 图像路径说明
- docs目录下， en后缀文件，图像路径为`../static`，多加一级，才能正确显示
- 其他目录，图像均在所在父目录下的images目录下

### 注意事项
- 图像路径
    ```python
    # ✔ markdown格式
    ![](./images/1.png)

    # html格式需要多加一级才能正常渲染
    <img src="../images/1.png" />
    ```
- 表格前后要有空行，否则不能正确渲染
- 无序列表在标题行下面，可以正确渲染。在文本行下面不行，需要空出一行