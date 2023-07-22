import os
from dotenv import load_dotenv
from langchain.llms import OpenAI

load_dotenv()
api_key = os.environ.get('OPENAI_API_KEY')


llm = OpenAI(openai_api_key=api_key)

# generate allows user to pass in a list of messages vs. llm() which allows for single message
result = (llm.generate(['Here is a fun fact about Python programming:', 'Who let the dogs out?']))

print(result.generations[1])