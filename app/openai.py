from app.metrics import get_system_metrics
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

def create_openai_chatbot():   

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # api_key="...",  # if you prefer to pass api key in directly instaed of using env vars
        # base_url="...",
        # organization="...",
        # other params...
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a Linux optimization expert. A user will provide system performance metrics. Analyze the metrics and suggest optimization and provide your recommendation. {metrics} ",
            ),
        ]
    )

    
    chain = prompt | llm
    
    response = chain.invoke(
        {

    "metrics": get_system_metrics()
          }
    )

    return response