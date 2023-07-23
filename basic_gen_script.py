from langchain.llms import OpenAI

llm = OpenAI()

# generate allows user to pass in a list of messages vs. llm() which allows for single message
result = (llm.generate(['Here is a fun fact about Python programming:', 'Who let the dogs out?']))

print(result.generations[1])