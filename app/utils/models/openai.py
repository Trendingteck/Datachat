import openai
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class OpenAIChatHelper:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("OpenAI API Key is missing.")
        openai.api_key = api_key

    def chat_with_data(self, df, prompt: str, temperature: float = 0.7, max_tokens: int = 200) -> str:
        """
        Chat with the data using OpenAI GPT-4.
        """
        try:
            # Convert dataframe to string for the prompt
            data_str = df.to_string()
            full_prompt = f"Here is the data:\n{data_str}\n\nQuestion: {prompt}\nAnswer:"
            
            # Generate response
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[{"role": "user", "content": full_prompt}],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI error: {str(e)}")
            return f"Error: {str(e)}"