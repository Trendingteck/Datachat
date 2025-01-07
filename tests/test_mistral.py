from app.utils.models.mistral import MistralHelper
import pandas as pd
import os

def test_mistral_chat_with_data():
    api_key = os.getenv("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("Missing MISTRAL_API_KEY in environment variables.")
    
    model = MistralHelper(api_key=api_key)
    df = pd.DataFrame({"column1": [1, 2, 3], "column2": ["a", "b", "c"]})
    
    response = model.chat_with_data(df, "What is the sum of column1?")
    assert response is not None, "No response received from Mistral."
    print("Test passed: Mistral responded successfully.")
