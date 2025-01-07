import requests
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class LlamaModel:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Llama API Key is missing.")
        self.api_key = api_key
        self.endpoint = "https://api.llama.ai/v1/chat"

    def chat_with_data(self, df, prompt: str, temperature: float = 0.7, max_tokens: int = 200) -> str:
        """
        Chat with the data using Llama 2.
        """
        try:
            # Convert dataframe to string for the prompt
            data_str = df.to_string()
            full_prompt = f"Here is the data:\n{data_str}\n\nQuestion: {prompt}\nAnswer:"
            
            # Generate response
            headers = {"Authorization": f"Bearer {self.api_key}"}
            data = {
                "prompt": full_prompt,
                "temperature": temperature,
                "max_tokens": max_tokens,
            }
            response = requests.post(self.endpoint, headers=headers, json=data)
            response.raise_for_status()
            return response.json()["response"]
        except Exception as e:
            logger.error(f"Llama error: {str(e)}")
            return f"Error: {str(e)}"