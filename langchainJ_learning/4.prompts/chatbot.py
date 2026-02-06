# from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id='mistralai/Mistral-7B-Instruct-v0.2',
#     task= "text-generation"
#                             )
# model = ChatHuggingFace(llm=llm)
# temp = []
# while(True):
#     user_input = input("You: ")
#     if user_input=="exit":
#         break
#     temp.append(user_input)
#     result = model.invoke(temp)
#     temp.append(result)
#     print("AI: ",result.content)


''' we are using list to store chat history, but the problem is that when the history
 become very large then our llm my get confused about which message is of human and which is of ai. 
 so langchain provide message label to distinguish between the type of messages '''

from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.2',
    task= "text-generation"
                            )
model = ChatHuggingFace(llm=llm)
temp = [SystemMessage(content = 'You are a helpful ai assistent!')]
while(True):
    user_input = input("You: ")
    temp.append(HumanMessage(content=user_input))
    if user_input=="exit":
        break
    result = model.invoke(temp)
    temp.append(AIMessage(content=result.content))
    print("AI: ",result.content)
print("history:",temp)