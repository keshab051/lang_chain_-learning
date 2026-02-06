from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline


llm = HuggingFacePipeline(
    model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation',
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

model = ChatHuggingFace(llm=llm)
result=model.invoke("what is the capital city of nepal")
print(result.content)

# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# # Load model and tokenizer
# model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0'
# tokenizer = AutoTokenizer.from_pretrained(model_id)
# model = AutoModelForCausalLM.from_pretrained(model_id)

# # Create the pipeline
# pipe = pipeline(
#     "text-generation",
#     model=model,
#     tokenizer=tokenizer,
#     max_new_tokens=100,
#     temperature=0.5
# )

# # Pass the pipeline to HuggingFacePipeline
# llm = HuggingFacePipeline(pipeline=pipe)

# # Wrap it with ChatHuggingFace
# chat_model = ChatHuggingFace(llm=llm)

# # Invoke the model
# result = chat_model.invoke("what is the capital city of nepal")
# print(result.content)