from langchain_google_genai import GoogleGenerativeAI
from ..config import settings

llm = GoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.5,
    api_key=settings.GEMINI_API_KEY
)

def get_json(crew_input:str):
    message = [
        (
            "system",
            "you are great at what you do"
            "now here you are given a financial paragraph of a company so your task is to provide me a json data also all the which number represent what should be there in keys of what all number are there in the paragraph"
        ),
        ("user",{crew_input})
        
    ]
    answer_json = llm.invoke(message)
    return answer_json
    
    