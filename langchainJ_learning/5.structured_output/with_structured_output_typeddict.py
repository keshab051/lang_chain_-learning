from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
load_dotenv()
model = ChatOpenAI()

# schema
#Using this annotated method, we will be able to send the whole point we want to say to llm to generate output 
#optional method = llm knows key is optional 
class Review(TypedDict):
    summary:Annotated[str,"breif summary"]
    sentiment:str
    pros:Annotated[Optional[list[str]],"extract pros is exist in the review"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this."
)
#this result is a dictionary
print(result)
print(result["summary"])
print(result["sentiment"])