from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

print("Loading PDFs...")

loader = PyPDFDirectoryLoader("pdfs")
documents = loader.load()

print("Chunking PDFs...")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

vectorstore.save_local("faiss_index")

print("FAISS index saved!")