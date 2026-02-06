from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    # provider="hf-inference" 

)
model = ChatHuggingFace(llm=llm)
# 1st prompt
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompts
template2= PromptTemplate(
    template='Write a 5 line summary on 5 point on the following \n{text}',
    input_variables=['topic']
)
prompt1 = template1.invoke({'topic':'Black hole'})
result1 = model.invoke(prompt1)
prompt2 = template2.invoke({'text':'result1'})
result2= model.invoke(prompt2)
print(result2.content)