from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from dotenv import load_dotenv 
from langchain_core.runnables import RunnableParallel ,RunnableBranch,RunnableLambda
from typing import Literal
from pydantic import BaseModel,Field
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation", 
)
model = ChatHuggingFace(llm=llm)

class feedback(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='')

parser = StrOutputParser()

parser1=PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='Classify the following feedback text into negative or positive. \n{feedback} \n{format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)

prompt2 = PromptTemplate(
    template='Write an appropriate short response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate short response to this negative feedback. \n {feedback}',
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser1

branch_chain = RunnableBranch(
    (lambda X:X.sentiment == 'positive',prompt2|model|parser),
    (lambda X:X.sentiment == 'negative',prompt3|model|parser),
    RunnableLambda(lambda X:'sentiment not found')
)

chain = classifier_chain|branch_chain

print( chain.invoke({'feedback':'this is horrible phone.'}))