# 安装：pip install pdfplumber
# 说明：pdfplumber 对各种 PDF 兼容性更好，能避开 pypdf 新版常见的
#       KeyError: 'bbox' 等字体解析问题。
import pdfplumber

def load_pdf(file_path):
    """加载PDF并返回文本列表"""
    documents = []
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""   # 空页返回 None，统一成 ""
            documents.append({
                'content': text,
                'page': i + 1
            })
    return documents

# 使用示例（使用下载的示例文件）
docs = load_pdf('data/sample_document.pdf')
print(f"加载了 {len(docs)} 页")
print(f"第1页内容: {docs[0]['content'][:100]}...")