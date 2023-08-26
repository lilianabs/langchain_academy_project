import os

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def main():
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model_name=OPENAI_MODEL)
    result = llm.predict(
        "Give me 5 topics for interesting YouTube videos about Python."
    )
    print(result)
    

if __name__ == "__main__":
    main()