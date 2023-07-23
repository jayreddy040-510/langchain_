# import os
# from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

# load_dotenv()
# api_key = os.environ.get("OPENAI_API_KEY")

chat = ChatOpenAI()

# doesn't work because needs different types
# chat('tell me a joke')

from langchain.schema import AIMessage, HumanMessage, SystemMessage

result = chat([
    SystemMessage(content="you are a conservative who hates the environment \
                and has strong feelings on global warming. also, you have \
                a penchant for cursing and referencing mainstream \
                conservative news channels"),
    HumanMessage(content="how do you feel about global warming?")
    ])


# print(result)
# generate allows user to pass in a list of convos vs. chat() which allows for single convo
result = chat.generate([
    [
        SystemMessage(content="you are a baby who has no knowledge of the \
                english language. you only respond using baby noises"),
    HumanMessage(content="how do you feel about global warming?")
    ],
    [
        SystemMessage(content="you are a surfer dude who speaks like a typical \
                      surfer dude. you are also a big fan of the beach and \
                      the ocean"),
        HumanMessage(content="how do you feel about global warming?")
    ]
])

print(result.generations)