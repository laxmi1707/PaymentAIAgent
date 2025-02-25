import os
from dotenv import load_dotenv
from typing import List

# Load environment variables first
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_payman_tool import (
    SendPaymentTool,
    SearchPayeesTool,
    AddPayeeTool,
    AskForMoneyTool,
    GetBalanceTool
)


from langchain_community.tools.gmail.utils import get_gmail_credentials
from langchain.tools.gmail  import GmailSearch
from langchain.tools.gmail  import GmailGetMessage
from langgraph.prebuilt import chat_agent_executor
from langchain_core.messages import HumanMessage
from gmailAgent import agent_executor

# Step 1: Get Google API Credentials
creds = get_gmail_credentials(
    credentials_path="credentials.json",  # Path to your downloaded credentials
    token_path="token.json",  # This file stores authentication tokens
)

def create_payment_agent():
    # Initialize all tools
    tools = [
        SendPaymentTool(),
        SearchPayeesTool(),
        AddPayeeTool(),
        AskForMoneyTool(),
        GetBalanceTool()
    ]
    
    # Create the prompt template - Removed chat_history
    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a helpful payment processing assistant that can help with sending payments, 
        managing payees, and checking balances. You have access to various payment tools and will use them
        appropriately based on user requests.
        
        Always verify amounts and payee information before processing payments.
        If you're unsure about any details, ask for clarification."""),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    
    # Initialize the LLM
    llm = ChatOpenAI(temperature=0)
    
    # Create the agent
    agent = create_openai_functions_agent(llm, tools, prompt)
    
    # Create the agent executor
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    return agent_executor

def search_inbox_for_invoice():
    # invoke the agent executor to start using it.
    response = agent_executor.invoke({"messages": [HumanMessage(content="""My name is 'The AI Dev'. 
        Can you search in inbox email about invoice emails or email which has some amount due. 
        Read the attachments of those emails and get the amount due.
        Give me the response in format sender email , subject, amount due , sending date, amount due date
        You have right to read attachments.""")]})
    print(response["messages"])

def test_agent():
    agent = create_payment_agent()
    
    # Test cases
    test_queries = [
        "What's my current balance?",
        "Search for a payee named Test1",
        "Send $5 to Test1"
    ]
    
    for query in test_queries:
        print(f"\n\nTesting query: {query}")
        print("-" * 50)
        try:
            response = agent.invoke({"input": query})
            print("Response:", response)
        except Exception as e:
            print(f"Error processing query: {str(e)}")

def find_unpaid_invoice():
    agent = create_payment_agent()
    
    # Test cases
    test_queries = [
        "What's my current balance?",
        "Search for a payee named Test1",
        "Send $5 to Test1"
    ]
    
    for query in test_queries:
        print(f"\n\nTesting query: {query}")
        print("-" * 50)
        try:
            response = agent.invoke({"input": query})
            print("Response:", response)
        except Exception as e:
            print(f"Error processing query: {str(e)}")

if __name__ == "__main__":
    test_agent() 