from pymongo import MongoClient
from ..config import settings
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import MongoDBAtlasVectorSearch

collection = None
client = None

def connect_to_mongo():
    global collection, client
    try:
        client = MongoClient(settings.MONGO_URI)
        collection = client['mongoVector']['vectorstore']
        print("Connected to MongoDB")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

def storeEmbeddings():
    loader = TextLoader('saveTempData/latest-news.txt')
    docs = loader.load()
    text_spiliter = RecursiveCharacterTextSplitter(chunk_size=600, chunk_overlap=20)
    splits = text_spiliter.split_documents(docs)
    
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001",google_api_key=settings.GEMINI_API_KEY)
    store = [] 

    for split in splits:
        store.append(split.page_content)
        
    client = MongoClient(settings.MONGO_URI)
    collection = client['mongoVector']['vectorstore']

    collection.delete_many({})
    
    docsearch = MongoDBAtlasVectorSearch.from_documents(
    splits, embeddings, collection=collection, index_name="vectorSearch"
    )
    
    print(docsearch)
    print("Embeddings saved to MongoDB vector base")