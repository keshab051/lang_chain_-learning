from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Optional,Literal
from pydantic import BaseModel,EmailStr,Field
load_dotenv()
model = ChatOpenAI()

# schema
#Using this annotated method, we will be able to send the whole point we want to say to llm to generate output 
#optional method = llm knows key is optional 
class Review(BaseModel):
    key_themes : list[str]=Field(discription = "write down all the key themes discussed in the review in a list.")
    summary : str = Field(discription ="A berif summary of the review")
    sentiment:Literal["pos","neg"] = Field(discription="sentiment of each review")
    pros:Optional[list[str]]=Field(default = None,description="extract pros that exist in the review")
    cons:Optional[list[str]]=Field(default = None,description="extract cons that exist in the review")
    name: Optional[str]=Field(default=None,discription = "write the name of the reviewer")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
)
#this result is a dictionary
print(result)
print(result["summary"])
print(result["sentiment"])