from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os


load_dotenv()

groq_api_key = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    max_retries=2,
    api_key=groq_api_key
)

messages = [
    ("system", "You are a helpful translator. Translate the user sentence to French."),
    ("human", "I love programming."),
]
print(llm.invoke(messages))

