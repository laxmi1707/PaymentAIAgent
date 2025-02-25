from langgraph.prebuilt import chat_agent_executor
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from gmail import tools

# add the tools from gmail.py to the list of tools.
tools = [*tools]


# the llm, the 'brain' of our agent that picks the tool.
# We will be using the gpt-4o model from OpenAI
model = ChatOpenAI(model="gpt-4o")

# create the agent executor, combing the model and the tools.
agent_executor = chat_agent_executor.create_tool_calling_executor(model, tools)
#about invoice emails or email which has some amount due or fee.

response = agent_executor.invoke({"messages": [HumanMessage(content="""My name is 'The AI Dev'. 
        Search in my inbox email for past 2 months
        for any invoice or bill from Singtel, Senoko.
        Get details from body of email and show the response 
        in tabular format sender email , subject, amount due , sending date, amount due date.
        Keep the returned content short.
        You have right to read attachments.""")]})
print(response["messages"])