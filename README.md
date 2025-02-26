# PaymentAIAgent
This explores the use of Agents for payments . It uses PaymanAI , and langchain tool 
Then there is an gmail agent which tries to connect to your gmail account provided the keys which you have created in your gmail.
This is a test app.
Step to create your gmail project and api keys is provided in link below.

# How to clone and use
-git clone usegithubhttps url
install dependecies using requirements.txt 
- python -m install requirements.txt
setup your virtual envirnment 
- python -v venv venv

# Follow these link to setup Google API permissions 
Link https://vijaykumarkartha.medium.com/create-your-personal-gmail-ai-agent-using-langchain-da95d1a9171a
https://medium.com/@elin.fritiofsson/create-a-simple-ai-agent-for-gmail-596d92dc7778

#In case any new package to be added
install it in use local using 
-pip install packagename
then freeze the installation into requirements 
- pip freeze -r requirements.txt 
then check in the requirements .txt
- git commit -m "updated requirements"
- git push
Dont checkin your virtual env 

#This Project uses Payman ai to create a demo wallet and explores the use of agents to transfer money on behalf of user
# Enhacement - the Agent will read gmail email to find invoice from last 10 days from requesters like 
singtel , senoko, trust  for the montly bills 


 Paychain 🔗💰

Build AI agents that can send real money using natural language with LangChain and Payman. Paychain combines the power of LLMs with Payman's secure payment infrastructure to enable conversational financial transactions.

## Why Paychain?

- 🤖 **Natural Language Payments**: Let AI agents process payments through simple conversations
- 🔒 **Built on Payman**: Leverage Payman's enterprise-grade payment infrastructure
- 🚀 **Quick Integration**: Get started in minutes with our Python SDK
- 💡 **Flexible Tools**: Rich set of Payman payment operations including sending, requesting, and managing payees
- 🛠️ **Built with LangChain**: Leverage the power of the LangChain ecosystem

## Quick Start 🚀

1. Get your API keys:
   - Go to [app.paymanai.com](https://app.paymanai.com) to get your Payman API key
   - Sign up takes just a few seconds and lets you send real money with Payman
   - Get your OpenAI API key from [platform.openai.com](https://platform.openai.com)

2. Clone the repository:
```bash
git clone <repository-url>
cd paychain-examples
```

3. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the root directory:
```env
PAYMAN_API_SECRET=your_payman_api_secret  # From app.paymanai.com
OPENAI_API_KEY=your_openai_api_key
PAYMAN_ENVIRONMENT=sandbox  # or production

6. Create a credentials.json in examples folder
Download the credentials file from gmail for API Oauth Credentials
Link https://vijaykumarkartha.medium.com/create-your-personal-gmail-ai-agent-using-langchain-da95d1a9171a
https://medium.com/@elin.fritiofsson/create-a-simple-ai-agent-for-gmail-596d92dc7778

```
