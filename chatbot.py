from dotenv import load_dotenv
import os
import mesop as me
import mesop.labs as mel
from swarmauri.standard.llms.concrete.GroqModel import GroqModel
from swarmauri.standard.agents.concrete.SimpleConversationAgent import SimpleConversationAgent
from swarmauri.standard.conversations.concrete.Conversation import Conversation

load_dotenv()

# Fetch the API key from environment variables or define it directly (Not recommended for production)
API_KEY = os.getenv('API_KEY')

# Initialize the GroqModel
llm = GroqModel(api_key=API_KEY)

# Create a SimpleConversationAgent with the GroqModel
agent = SimpleConversationAgent(llm=llm, conversation=Conversation())

# Define the function to be executed for the mesop interface
def converse(input: str, history: list[mel.ChatMessage]):
    result = agent.exec(input)
    yield result

@me.page(
    security_policy=me.SecurityPolicy(
        allowed_iframe_parents=["https://google.github.io"]
    ),
    path="/chat",
    title="Swarmauri Agent",
)
def page():
    mel.chat(converse, title="Swarmauri Agent", bot_user="Groq")