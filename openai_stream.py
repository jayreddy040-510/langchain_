import os
import time
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"), 
  api_key=os.getenv("AZURE_OPENAI_KEY"),  
  api_version="2023-05-15"
)
start_time = time.time()
response = client.chat.completions.create(
    model="carecoach-gpt35-16k",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Does Azure OpenAI support customer managed keys?"},
        {"role": "assistant", "content": "Yes, customer managed keys are supported by Azure OpenAI."},
        {"role": "user", "content": "Do other Azure AI services support this too?"}
    ],
    stream=True
)

accumulated_content = "" 
for choice in response:
    print(time.time() - start_time)
    content = choice.choices[0].delta.content
    if content is not None:
        accumulated_content += content
        print(accumulated_content, "\n", flush=True)

    if choice.choices[0].finish_reason == 'stop':
        break
