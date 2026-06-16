# 无需安装额外库
def load_text(file_path):
    """加载文本文件"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # 尝试其他编码
        with open(file_path, 'r', encoding='gbk') as f:
            return f.read()

# 使用示例（使用下载的示例文件）
text = load_text('data/article.txt')
print(f"文件长度: {len(text)} 字符")
print(f"内容预览: {text[:200]}...")