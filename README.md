# Python Demo 项目

这个项目用于保存相互独立的 Python Demo。每个 Demo 都放在 `demos` 目录中，
并通过文件名说明使用的技术和实现的功能。

## 文件结构

```text
Python/
|-- demos/
|   |-- __init__.py
|   |-- gradio_hello.py
|   `-- gradio_pixel.py
|-- main.py
|-- requirements.txt
`-- README.md
```

## 命名规则

Demo 文件统一使用：

```text
技术_功能.py
```

例如：

- `gradio_hello.py`：使用 Gradio 实现 Hello World 网页。
- `gradio_pixel.py`：使用 Gradio 和 Pillow 处理图片。
- `pandas_excel.py`：使用 Pandas 读取 Excel。
- `requests_api.py`：使用 Requests 调用 API。

文件名使用小写英文和下划线，不使用空格。

## 当前 Demo

### Gradio Hello World

文件：`demos/gradio_hello.py`

功能：

- 在网页中输入名字。
- 点击提交后显示问候语。
- 输入为空时显示 `Hello, World!`。

安装依赖：

```powershell
python -m pip install -r requirements.txt
```

通过默认入口启动：

```powershell
python main.py
```

也可以直接启动该 Demo：

```powershell
python demos/gradio_hello.py
```

### 图片处理

文件：`demos/gradio_pixel.py`

功能：

- 从本地上传图片。
- 支持像素化、灰度化、黑白化和反色。
- 调整像素块大小和黑白阈值。
- 在网页中预览并下载处理结果。

启动：

```powershell
python demos/gradio_pixel.py
```
