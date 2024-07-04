### 使用教程
```bash
$ pip install -r requirements.txt
$ mkdocs serve
```

### 图像路径说明
- docs目录下， en后缀文件，图像路径为`../static`，多加一级，才能正确显示
- 其他目录，图像均在所在父目录下的images目录下

### 注意事项
- 图像路径只能使用markdown格式，html格式不行
    ```python
    # ✔ markdown格式
    ![](./images/498119182f0a414ab86ae2de752fa31c9ddc3a74a76847049cc57884602cb269-20240704185744623.png)

    # ❌ html格式
    <img src="" />
    ```
- 表格前后要有空行，否则不能正确渲染