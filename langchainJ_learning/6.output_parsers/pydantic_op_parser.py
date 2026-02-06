from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "mistralai/Mistral-7B-Instruct-v0.2",
    task = "text-generation",
    # provider="hf-inference" 

)
model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description='Name of the person')
    age: int = Field(gt=20,description='Age of the person ')
    city: str = Field(description=' Name of the city the person belongs to ')

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name age and city of the fictional {place} person.\n {formate_instruction}',
    input_variables=['place'],
    partial_variables={'formate_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place','Nepali'})
# result = model.invoke(prompt)
# final_result = parser.invoke( result.content)


chain = template|model|parser
final_result = chain.invoke({'place':"Nepali"})


print(final_result)
