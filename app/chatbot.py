import requests
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda
import os
from dotenv import load_dotenv

load_dotenv()

class DeepSeekLLM:
    """
    Custom class for interacting with DeepSeek API.
    """
    def __init__(self, api_key, model="deepseek-chat", api_url="https://api.deepseek.com/chat/completions"):
        self.api_key = api_key
        self.model = model
        self.api_url = api_url

    def generate_response(self, prompt: str) -> str:
        """Make a request to the DeepSeek API."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Ensure the prompt is a plain string
        if not isinstance(prompt, str):
            prompt = str(prompt)

        payload = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": "You are a Linux optimization assistant."},
                {"role": "user", "content": prompt}
            ],
            "stream": False
        }

        response = requests.post(self.api_url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            raise ValueError(f"Error from DeepSeek API: {response.status_code} - {response.text}")


def create_chatbot(recommendations: str):
    """
    Create a chatbot instance using DeepSeek API.
    """
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
    if not deepseek_api_key:
        raise ValueError("DeepSeek API key is missing. Set DEEPSEEK_API_KEY in your environment variables.")

    # Instantiate the DeepSeek LLM
    llm = DeepSeekLLM(api_key=deepseek_api_key)

    # Wrap the LLM's generate_response method in a RunnableLambda
    runnable_llm = RunnableLambda(lambda prompt: llm.generate_response(str(prompt)))

    # Define the prompt template
    prompt_template = PromptTemplate(
        input_variables=["recommendations"],
        template="""
        You are a Linux optimization expert. A user will provide system performance metrics.
        Analyze the metrics and suggest optimizations using your knowledge and the following recommendations:
        {recommendations}
        """
    )

    # Chain the prompt with the RunnableLambda
    chain = prompt_template | runnable_llm
    return chain
