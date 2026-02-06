from langchain_huggingface import HuggingFaceEmbeddings,HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model = "sentence-transformers/all-MiniLM-L6-v2",
)

querry = " what is the capital of nepal? "

result = embeddings.embed_query(querry)
print(str(result))