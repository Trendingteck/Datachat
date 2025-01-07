import google.generativeai as genai
import logging
import pandas as pd

logger = logging.getLogger(__name__)

class GeminiHelper:
    def __init__(self, api_key: str):
        if not api_key:
            raise ValueError("Gemini API Key is missing.")
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def chat_with_data(self, df: pd.DataFrame, prompt: str, temperature: float = 0.7, max_tokens: int = 200) -> str:
        """
        Chat with the data using Gemini.
        """
        try:
            # Convert dataframe to string representation
            df_str = df.to_string()
            
            # Create a context-aware prompt
            full_prompt = f"""Here is the data I want to analyze:
{df_str}

Question: {prompt}

Please provide a clear and concise answer based on the data above. If the question requires calculations or data analysis, show the relevant numbers."""
            
            # Generate response with specified parameters
            response = self.model.generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                    top_p=0.8,
                    top_k=40
                )
            )
            
            return response.text if response else "No response generated."
            
        except Exception as e:
            logger.error(f"Gemini error: {str(e)}")
            return f"Error: {str(e)}"