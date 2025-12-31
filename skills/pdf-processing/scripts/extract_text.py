# scripts/extract_text.py
import PyPDF2

def extract_pdf_text(pdf_path: str) -> str:
    """提取PDF文件中的文本，忽略页眉/页脚（假设页眉/页脚为每页前2行和后2行）"""
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            # 忽略页眉（前2行）和页脚（后2行）
            lines = page_text.split("\n")
            filtered_lines = lines[2:-2] if len(lines) > 4 else lines
            text += "\n".join(filtered_lines) + "\n"
    return text

# 测试：python extract_text.py ./sample.pdf
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python extract_text.py <pdf_path>")
        sys.exit(1)
    pdf_path = sys.argv[1]
    print(extract_pdf_text(pdf_path))
