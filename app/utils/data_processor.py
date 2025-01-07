import pandas as pd
import numpy as np
import logging
from typing import Union, Optional, Dict, List
from pathlib import Path

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self):
        self.current_df: Optional[pd.DataFrame] = None
        self.data_summary: Optional[Dict] = None
        
    def load_data(self, uploaded_file) -> Union[pd.DataFrame, None]:
        """Load data from an uploaded Excel or CSV file."""
        try:
            if uploaded_file.size == 0:
                raise ValueError("Uploaded file is empty.")
            
            # Read the file based on its extension
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            elif uploaded_file.name.endswith('.xlsx'):
                df = pd.read_excel(uploaded_file)
            else:
                raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")
            
            if df.empty:
                raise ValueError("The uploaded file contains no data.")
            
            # Store the dataframe
            self.current_df = df
            # Generate summary statistics
            self._generate_data_summary()
            
            logger.info(f"Successfully loaded data with {df.shape[0]} rows and {df.shape[1]} columns.")
            return df
        
        except Exception as e:
            logger.error(f"Error loading file: {str(e)}")
            raise ValueError(f"Error loading file: {str(e)}")
    
    def _generate_data_summary(self) -> None:
        """Generate summary statistics for the loaded dataframe."""
        if self.current_df is None:
            return
        
        self.data_summary = {
            'shape': self.current_df.shape,
            'columns': list(self.current_df.columns),
            'dtypes': self.current_df.dtypes.to_dict(),
            'missing_values': self.current_df.isnull().sum().to_dict(),
            'numeric_columns': list(self.current_df.select_dtypes(include=[np.number]).columns),
            'categorical_columns': list(self.current_df.select_dtypes(include=['object']).columns)
        }
    
    def get_context_for_query(self, query: str) -> str:
        """Generate context about the data for AI models."""
        if self.current_df is None or self.data_summary is None:
            return "No data has been loaded yet."
        
        context = [
            f"The dataset contains {self.data_summary['shape'][0]} rows and {self.data_summary['shape'][1]} columns.",
            f"Columns: {', '.join(self.data_summary['columns'])}",
            f"Numeric columns: {', '.join(self.data_summary['numeric_columns'])}",
            f"Categorical columns: {', '.join(self.data_summary['categorical_columns'])}"
        ]
        
        return "\n".join(context)
    
    def execute_query(self, query: str) -> Union[pd.DataFrame, str]:
        """Execute a pandas query on the current dataframe."""
        if self.current_df is None:
            raise ValueError("No data loaded. Please upload a file first.")
        
        try:
            # Execute the query using pandas eval
            result = self.current_df.query(query)
            return result
        except Exception as e:
            logger.error(f"Error executing query: {str(e)}")
            raise ValueError(f"Error executing query: {str(e)}")
    
    def get_sample_data(self, n_rows: int = 5) -> pd.DataFrame:
        """Get a sample of the current dataframe."""
        if self.current_df is None:
            raise ValueError("No data loaded. Please upload a file first.")
        return self.current_df.head(n_rows)