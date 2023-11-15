import os
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage
from dotenv import load_dotenv

load_dotenv()

llm = AzureChatOpenAI(
    openai_api_version="2023-05-15",
    azure_deployment="carecoach-gpt35-16k"
)

message = HumanMessage(
    content="Translate this sentence from English to French. I love programming."
)

res = llm([message])

print(res.content, flush=True)

