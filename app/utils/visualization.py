import plotly.express as px
import pandas as pd
import logging
from typing import Optional, Dict

logger = logging.getLogger(__name__)

class DataVisualizer:
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def generate_visual(self, df: pd.DataFrame, visual_type: str) -> Optional[Dict]:
        """
        Generate a visualization based on the requested type.
        """
        try:
            if visual_type == "bar":
                fig = px.bar(df, x=df.columns[0], y=df.columns[1], title=f"Bar Chart: {df.columns[0]} vs {df.columns[1]}")
            elif visual_type == "line":
                fig = px.line(df, x=df.columns[0], y=df.columns[1], title=f"Line Chart: {df.columns[0]} vs {df.columns[1]}")
            elif visual_type == "pie":
                fig = px.pie(df, names=df.columns[0], values=df.columns[1], title=f"Pie Chart: {df.columns[0]}")
            elif visual_type == "scatter":
                fig = px.scatter(df, x=df.columns[0], y=df.columns[1], title=f"Scatter Plot: {df.columns[0]} vs {df.columns[1]}")
            elif visual_type == "histogram":
                fig = px.histogram(df, x=df.columns[0], title=f"Histogram: {df.columns[0]}")
            else:
                return None

            return {"type": "visual", "figure": fig}
        except Exception as e:
            logger.error(f"Error generating visual: {str(e)}")
            return None

    def generate_explanation(self, df: pd.DataFrame, visual_type: str) -> Optional[str]:
        """
        Generate an explanation for the visualization using the AI model.
        """
        try:
            prompt = f"Explain the {visual_type} chart showing {df.columns[0]} vs {df.columns[1]} for the following data:\n{df.to_string()}"
            return self.ai_model.chat_with_data(df, prompt)
        except Exception as e:
            logger.error(f"Error generating explanation: {str(e)}")
            return None