from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore

embeddings = OllamaEmbeddings(model="llama3.2:1b")

file_path = "give me detail explantion pdf of perplexity.pdf"
loader = PyPDFLoader(file_path)
data = loader.load_and_split()

url ="https://ad745e47-f6e7-4539-83bd-0e4f49dc214a.us-east4-0.gcp.cloud.qdrant.io"
api_key ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzU2NDg2OTU1fQ.QH_ZSG3qqSvHU84evdJBYJPCGdaJ_4g0p0sZ-waBbAQ"

qdrant = QdrantVectorStore.from_documents(
    data,
    embeddings,
    url=url,
    prefer_grpc=True,
    api_key=api_key,
    collection_name="my_documents",
)