# AIProject

这是一个用于学习 Python、Gradio、通义千问 API 和 LangChain 记忆机制的示例项目。项目中的脚本相对独立，适合按章节逐个运行、观察输出并修改练习。

## 项目结构

```text
AIProject/
|-- chapter/
|   |-- api_1.py          # 通义千问流式输出示例
|   |-- api_2.py          # 封装普通对话函数
|   |-- api_3.py          # 文档生成助手示例
|   |-- guessgame.py      # 带对话记忆的猜数字游戏
|   |-- memory_1.py       # 使用消息列表实现简单记忆
|   |-- memory_2.py       # 使用类封装对话记忆
|   `-- memory_3.py       # LangChain 摘要 + 滑动窗口记忆
|-- gradio/
|   |-- __init__.py
|   |-- gradio_hello.py   # Gradio Hello World 页面
|   `-- gradio_pixel.py   # Gradio 图片处理页面
|-- main.py               # 通义千问基础调用入口
|-- requirements.txt      # 基础依赖
|-- .env                  # 本地环境变量，不建议提交
`-- README.md
```

## 环境准备

建议使用 Python 3.10 或更高版本。

创建并激活虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

安装基础依赖：

```powershell
python -m pip install -r requirements.txt
```

如果要运行 `chapter` 目录下的通义千问或 LangChain 示例，还需要安装相关依赖：

```powershell
python -m pip install dashscope python-dotenv langchain-classic langchain-community
```

## 配置 API Key

通义千问相关示例需要配置 `DASHSCOPE_API_KEY`。可以在项目根目录新建或修改 `.env` 文件：

```env
DASHSCOPE_API_KEY=你的DashScope API Key
```

部分脚本会通过 `python-dotenv` 自动读取 `.env`；如果脚本没有显式调用 `load_dotenv()`，也可以在 PowerShell 中临时设置：

```powershell
$env:DASHSCOPE_API_KEY="你的DashScope API Key"
```

## 运行示例

运行基础 API 调用：

```powershell
python main.py
```

运行通义千问流式输出：

```powershell
python chapter\api_1.py
```

运行封装后的对话函数：

```powershell
python chapter\api_2.py
```

运行代码文档生成助手：

```powershell
python chapter\api_3.py
```

运行带记忆的多轮对话示例：

```powershell
python chapter\memory_1.py
python chapter\memory_2.py
python chapter\memory_3.py
```

运行猜数字游戏：

```powershell
python chapter\guessgame.py
```

运行 Gradio Hello World：

```powershell
python gradio\gradio_hello.py
```

运行 Gradio 图片处理页面：

```powershell
python gradio\gradio_pixel.py
```

Gradio 启动后会在终端显示本地访问地址，通常类似：

```text
http://127.0.0.1:7860
```

## 示例说明

### API 示例

- `api_1.py`：演示 `Generation.call(..., stream=True)` 的流式输出。
- `api_2.py`：把通义千问调用封装成 `chat_with_qwen()` 函数。
- `api_3.py`：定义 `DocumentAssistant` 类，根据传入代码生成技术文档。
- `main.py`：演示最基础的 DashScope API 调用流程。

### 记忆示例

- `memory_1.py`：用普通列表保存完整消息历史，实现最基础的多轮记忆。
- `memory_2.py`：用 `ChatWithMemory` 类封装消息历史、清空历史、统计消息数等能力。
- `memory_3.py`：使用 LangChain 的 `ConversationSummaryBufferMemory`，演示“旧对话摘要 + 最近对话原文保留”的记忆策略。
- `guessgame.py`：通过保存完整对话历史，让 AI 在猜数字游戏中记住前面的猜测。

### Gradio 示例

- `gradio_hello.py`：输入名字并返回问候语。
- `gradio_pixel.py`：上传图片后进行像素化、灰度化、黑白化和反色处理。

## 常见提示

### PyTorch was not found

如果看到：

```text
[transformers] PyTorch was not found.
```

这表示当前环境没有安装 PyTorch。只使用 tokenizer、配置或普通 API 调用时可以暂时忽略；如果要在本地运行 Hugging Face 模型，需要额外安装 `torch`。

### langchain-community DeprecationWarning

如果看到：

```text
DeprecationWarning: langchain-community is being sunset
```

这是 LangChain 生态迁移提示，说明未来推荐使用对应的独立集成包。当前示例主要用于学习记忆机制，通常不影响运行。

### HF Hub unauthenticated requests

如果看到：

```text
Warning: You are sending unauthenticated requests to the HF Hub.
```

表示访问 Hugging Face Hub 时没有配置 `HF_TOKEN`。公开资源仍可访问，但可能有速率限制。

## 命名建议

新增示例文件时建议使用小写英文和下划线：

```text
技术_功能.py
```

例如：

- `api_stream.py`
- `memory_summary.py`
- `gradio_chat.py`

这样方便从文件名直接看出示例用途。
