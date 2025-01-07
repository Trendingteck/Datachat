import anthropic
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class ClaudeModel:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Claude API Key is missing.")
        self.api_key = api_key
        self.client = anthropic.Client(api_key=self.api_key)

    def chat_with_data(self, df, prompt: str, temperature: float = 0.7, max_tokens: int = 200) -> str:
        """
        Chat with the data using Claude 3.
        """
        try:
            # Convert dataframe to string for the prompt
            data_str = df.to_string()
            full_prompt = f"{anthropic.HUMAN_PROMPT} Here is the data:\n{data_str}\n\nQuestion: {prompt}{anthropic.AI_PROMPT}"
            
            # Generate response
            response = self.client.completion(
                prompt=full_prompt,
                model="claude-3",
                max_tokens_to_sample=max_tokens,
                temperature=temperature,
            )
            return response.completion
        except Exception as e:
            logger.error(f"Claude error: {str(e)}")
            return f"Error: {str(e)}"