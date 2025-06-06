from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pydantic_core.core_schema import dict_schema

pdf_path = ""
loader = PyMuPDFLoader(
    pdf_path,
    mode="single"
)

docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, length_function=len
)

texts = text_splitter.split_documents(docs)
print(len(texts))

for doc in texts:
    doc.page_content = doc.page_content.replace("\t", " ")
