import os
import time
from dotenv import load_dotenv
from langchain.chat_models import AzureChatOpenAI
from langchain.schema import HumanMessage, Document
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

# Load environment variables
load_dotenv()
api_key = os.environ.get("AZURE_OPENAI_API_KEY")
azure_endpoint = os.environ.get("AZURE_OPENAI_API_ENDPOINT")

# Initialize AzureChatOpenAI
azure_chat = AzureChatOpenAI(
    azure_deployment="carecoach-gpt35-16k",  # Replace with your deployment name
    api_key=api_key,
    azure_endpoint=azure_endpoint,
)

# Sample conversation
conversation_texts = [
    "hey",
    "hello",
    "what's your name?",
    "my name's Sarah and I'm working on tuning up my toyota camry",
    "cool.",
    "what's your name?",
    "my name's bob"
]
time0 = time.time()
# Convert conversation texts to Documents
conversation = [Document(page_content=text) for text in conversation_texts]
time1 = time.time()
print(f"turning texts to Documents: {time1 - time0}")
time2 = time.time()
# Set up Sentence Transformer Embeddings
embedding_function = SentenceTransformerEmbeddings()
print(f"sentence transformer embeddings setup: {time.time() - time2}")
time3 = time.time()
# Create Chroma in-memory vector store
chroma_db = Chroma.from_documents(conversation, embedding_function)
print(f"creating chroma db in-memory vector store: {time.time() - time3}")

# Function to query Chroma DB
def query_chroma_db(query):
    results = chroma_db.similarity_search(query)
    return results

# User query
user_query = "What is Sarah working on?"
time4 = time.time()
chroma_results = query_chroma_db(user_query)
print(f"getting chrombadb query results from vector store: {time.time() - time4}")

# Format Chroma results for LLM query
context_from_chroma = ". ".join([result.page_content for result in chroma_results])
llm_query = f"Based on this conversation: {context_from_chroma}. {user_query}"

# Use AzureChatOpenAI LLM to respond
time5 = time.time()
llm_response = azure_chat([HumanMessage(content=llm_query)])
print(f"time for just LLM response: {time.time() - time5}")
print("LLM Response:", llm_response)
