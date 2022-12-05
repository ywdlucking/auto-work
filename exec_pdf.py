import pdfplumber

with pdfplumber.open("data/党建基础知识.pdf") as pdf:
  for page in pdf.pages:
    print(page.extract_text())