import os
import requests
from dotenv import load_dotenv

load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_URL = "https://api.deepseek.com/chat/completions"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
}

def query_deepseek_for_optimization(metrics):
    """
    Query DeepSeek API with Linux metrics for optimization suggestions.
    """
    user_query = f"Here are the current system metrics: {metrics}. How can I optimize the system?"

    payload = {
        "model": "deepseek-chat",  # Use "deepseek-reasoner" for reasoning models
        "messages": [
            {"role": "system", "content": "You are a Linux optimization assistant."},
            {"role": "user", "content": user_query}
        ],
        "stream": False
    }

    response = requests.post(DEEPSEEK_URL, json=payload, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("choices", [{}])[0].get("message", {}).get("content", "No response")
    else:
        return f"Error: {response.status_code} - {response.text}"
