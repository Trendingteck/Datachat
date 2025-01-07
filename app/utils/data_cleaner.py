import pandas as pd
import numpy as np
import streamlit as st
import logging
from typing import List, Optional

logger = logging.getLogger(__name__)

def clean_column(df: pd.DataFrame, column: str, operation: str) -> pd.DataFrame:
    """
    Clean a specific column based on the operation.
    """
    try:
        if operation == "remove_missing":
            df[column] = df[column].replace("", np.nan).dropna()
        elif operation == "remove_duplicates":
            df = df.drop_duplicates(subset=[column])
        return df
    except Exception as e:
        logger.error(f"Error cleaning column {column}: {str(e)}")
        raise ValueError(f"Error cleaning column {column}: {str(e)}")

def clean_rows(df: pd.DataFrame, start: int, end: int) -> pd.DataFrame:
    """
    Clean specific rows (e.g., remove rows 10-60).
    """
    try:
        return df.drop(df.index[start:end])
    except Exception as e:
        logger.error(f"Error cleaning rows {start}-{end}: {str(e)}")
        raise ValueError(f"Error cleaning rows {start}-{end}: {str(e)}")

def process_cleaning_command(df: pd.DataFrame, command: str) -> Optional[pd.DataFrame]:
    """
    Process the cleaning command and return the cleaned dataframe.
    """
    try:
        if command.startswith("/clean column"):
            # Show column selection dropdown
            column = st.selectbox("Select a column to clean:", df.columns)
            operation = st.selectbox("Select an operation:", ["remove_missing", "remove_duplicates"])
            return clean_column(df, column, operation)
        
        elif command.startswith("/clean rows"):
            # Show row range input
            start = st.number_input("Start row:", min_value=0, max_value=len(df)-1, value=0)
            end = st.number_input("End row:", min_value=start+1, max_value=len(df), value=len(df))
            return clean_rows(df, start, end)
        
        else:
            return None
    except Exception as e:
        logger.error(f"Error processing cleaning command: {str(e)}")
        raise ValueError(f"Error processing cleaning command: {str(e)}")