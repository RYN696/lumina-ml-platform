import pandas as pd

class DatasetProfiler:
    # Automatic Dataset Analysis
    def __init__(self,file_path):
        self.file_path = file_path
        self.data = None

    def load_dataset(self):
        # Load CSV dataset
        self.data = pd.read_csv(self.file_path)
        return self.data

    def get_basic_info(self):
        # Get basic information about the dataset
        return {
            "rows": self.data.shape[0],
            "columns": self.data.shape[1]
        }

    def get_columns_info(self):
        # Analyze columns and data types
        columns = {}
        for column in self.data.columns:
            columns[column] = str(self.data[column].dtype)
        return columns

    def get_missing_values(self):
        # Detect missing values in the dataset
        missing = self.data.isnull().sum()
        return {
            column: int(value)
            for column, value in missing.items()
            if value > 0
        }

    def get_duplicates(self):
        # Detect duplicate rows in the dataset
        duplicates = self.data.duplicated().sum()
        return {
            "duplicate_rows": int(duplicates)
        }

    def generate_report(self):
        # Generate a comprehensive report of the dataset
        report = {
            "basic_info": self.get_basic_info(),
            "columns_info": self.get_columns_info(),
            "missing_values": self.get_missing_values(),
            "duplicates": self.get_duplicates()
        }
        return report