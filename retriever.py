from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from llm import *

embeddings = OllamaEmbeddings(model="llama3.2:1b")

url ="https://ad745e47-f6e7-4539-83bd-0e4f49dc214a.us-east4-0.gcp.cloud.qdrant.io"
api_key ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIiwiZXhwIjoxNzU2NDg2OTU1fQ.QH_ZSG3qqSvHU84evdJBYJPCGdaJ_4g0p0sZ-waBbAQ"

question = input("Enter your question: ")

qdrant = QdrantVectorStore.from_existing_collection(
    embedding=embeddings,
    url=url,
    api_key=api_key,
    collection_name="my_documents",
)

response =  qdrant.similarity_search(
    query=question,
    k=5)
# for score in response:
#     print(  score)

prompt = f"""

Question: {question},
context: {response}
Only return the summary based on the provided content.
"""

print(completion_llm(prompt))
# for i in completion_llm(prompt):
#     print(i, end="", flush=True)
