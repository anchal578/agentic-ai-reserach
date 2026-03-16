import os

from langchain import OpenAI, LLMChain
from langchain.prompts import PromptTemplate

# Set up OpenAI API Key
os.environ["OPENAI_API_KEY"] = 'your-openai-api-key'

# Create a prompt template
prompt_template = PromptTemplate(
    input_variables=["user_input"],
    template="You are a research assistant. Respond to the following query: {user_input}"
)

# Initialize OpenAI model
llm = OpenAI(model="text-davinci-003")

# Create a chain with the prompt and LLM
chain = LLMChain(prompt=prompt_template, llm=llm)

# Sample user input
user_query = "What are the latest advancements in AI research?"

# Get a response from the model
response = chain.run(user_input=user_query)

print(response)