import re
import logging
from typing import Dict, Optional

logger = logging.getLogger(__name__)

class ResponseParser:
    def __init__(self):
        # Keywords for visualization and explanation
        self.visual_keywords = ["show", "plot", "graph", "chart", "visualize", "display"]
        self.explain_keywords = ["explain", "describe", "analyze", "interpret", "what does this mean"]

    def parse_user_intent(self, user_input: str) -> Dict[str, bool]:
        """
        Parse the user's input to determine if they want a visualization, explanation, or both.
        """
        try:
            # Convert input to lowercase for easier matching
            user_input = user_input.lower()

            # Check for visualization keywords
            wants_visual = any(keyword in user_input for keyword in self.visual_keywords)

            # Check for explanation keywords
            wants_explanation = any(keyword in user_input for keyword in self.explain_keywords)

            return {
                "wants_visual": wants_visual,
                "wants_explanation": wants_explanation,
            }
        except Exception as e:
            logger.error(f"Error parsing user intent: {str(e)}")
            return {"wants_visual": False, "wants_explanation": False}

    def extract_visual_type(self, user_input: str) -> Optional[str]:
        """
        Extract the type of visualization requested by the user.
        """
        try:
            # Common visualization types
            visual_types = {
                "bar": ["bar", "bars"],
                "line": ["line", "trend"],
                "pie": ["pie", "percentage"],
                "scatter": ["scatter", "correlation"],
                "histogram": ["histogram", "distribution"],
            }

            # Check for each visualization type
            for visual_type, keywords in visual_types.items():
                if any(keyword in user_input.lower() for keyword in keywords):
                    return visual_type

            return None
        except Exception as e:
            logger.error(f"Error extracting visual type: {str(e)}")
            return None