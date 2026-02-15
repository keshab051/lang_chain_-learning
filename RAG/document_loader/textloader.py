from langchain_community.document_loaders import TextLoader
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()
loader = TextLoader('cricket.txt',encoding='utf-8')


model = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation"
)
model = ChatHuggingFace(llm=model)

prompt = PromptTemplate(
    template='Write a summary for the following poem. \n {poem}',
    input_variables=['poem']
)
parser = StrOutputParser()

chain = RunnableLambda(lambda X:loader)|prompt|model|parser
result = chain.invoke({})
print(result)


# or 

# docs=loader.load()

# print(docs)
# print(len(docs))
# print(type(docs))
# print(docs[0])
# print(type(docs[0]))
# print(docs[0].page_content)
