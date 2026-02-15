from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = '''def hello_world():
    print("Hello, World!")

# Call the function
hello_world()'''

splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON ,
    chunk_size=50,
    chunk_overlap=0
)

print(splitter.split_text(text))