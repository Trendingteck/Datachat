from mistralai.client import MistralClient
from mistralai.models import ChatMessage
import logging
import pandas as pd

logger = logging.getLogger(__name__)

class MistralModel:
    def __init__(self, api_key: str, model: str = "mistral-medium"):
        if not api_key:
            raise ValueError("Mistral API Key is missing.")
        self.client = MistralClient(api_key=api_key)
        self.model = model

    def chat_with_data(self, df: pd.DataFrame, prompt: str, temperature: float = 0.7, max_tokens: int = 200) -> str:
        """
        Chat with the data using Mistral AI.
        """
        try:
            # Convert dataframe to string representation
            df_str = df.to_string()
            
            # Create a context-aware prompt
            system_prompt = """You are a helpful data analysis assistant. Analyze the provided data and answer questions about it.
When performing calculations or analysis, show your work and explain your findings clearly."""
            
            user_prompt = f"""Here is the data I want to analyze:
{df_str}

Question: {prompt}

Please provide a clear and concise answer based on the data above. If the question requires calculations or data analysis, show the relevant numbers."""
            
            # Generate response
            messages = [
                ChatMessage(role="system", content=system_prompt),
                ChatMessage(role="user", content=user_prompt)
            ]
            
            chat_response = self.client.chat(
                model=self.model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            return chat_response.choices[0].message.content if chat_response.choices else "No response generated."
            
        except Exception as e:
            logger.error(f"Mistral error: {str(e)}")
            return f"Error: {str(e)}"