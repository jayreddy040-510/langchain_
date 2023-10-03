import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()
openai_api_key = os.environ.get("OPENAI_API_KEY")
print(openai_api_key, flush=True)
chat = ChatOpenAI(openai_api_key=openai_api_key)

# doesn't work because needs different types
# chat('tell me a joke')


result = chat([
    SystemMessage(content="you are a conservative who hates the environment \
                and has strong feelings on global warming. also, you have \
                a penchant for cursing and referencing mainstream \
                conservative news channels"),
    HumanMessage(content="how do you feel about global warming?")
    ])


# generate allows user to pass in a list of
# convos vs. chat() which allows for single convo
result = chat.generate([
    [
        SystemMessage(content="you are a baby who has no knowledge of the \
                english language. you only respond using baby noises"),
    HumanMessage(content="how do you feel about global warming?")
    ],
    [
        SystemMessage(content="you are a surfer dude who speaks like a \
                      typical surfer dude. you are also a big fan of the beach\
                      and the ocean"),
        HumanMessage(content="how do you feel about global warming?")
    ]
])

print(result.generations)
