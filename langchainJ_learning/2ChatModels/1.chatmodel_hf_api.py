from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    # provider="hf-inference" 

)
llm = ChatHuggingFace(llm=llm)
result = llm.invoke("What is the capital city of nepal?")
print(result.content)


# from dotenv import load_dotenv
# from pathlib import Path
# import os

# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

# # Load .env from project root
# env_path = Path(__file__).resolve().parents[1] / ".env"
# load_dotenv(dotenv_path=env_path)

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
# )

# chat_model = ChatHuggingFace(llm=llm)

# response = chat_model.invoke("What is the capital city of Nepal?")
# print(response.content)