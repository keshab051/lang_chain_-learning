from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader('6th_sem_proposal_final.pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=0,
    separator=''
)
splitted_text = splitter.split_documents(docs)

#split_text(docs) . this will be used when a plan text is to be splitted 

print(splitted_text)