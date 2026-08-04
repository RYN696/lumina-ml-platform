import pandas as pd
from pandas.api.types import (
    is_bool_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
)

from app.ml.correlations import get_correlation_matrix
from app.ml.outliers import detect_outliers
from app.ml.statistics import get_numeric_statistics
from app.ml.utils import detect_identifier_columns


class DatasetProfiler:
    """
    Perform automatic profiling and analysis of a dataset.
    """

    def __init__(self, file_path: str):
        """
        Initialize the DatasetProfiler.

        Args:
            file_path: Path to the CSV dataset.
        """
        self.file_path = file_path
        self.data: pd.DataFrame | None = None

    def load_dataset(self) -> pd.DataFrame:
        """
        Load the dataset from the CSV file.

        Returns:
            The loaded pandas DataFrame.
        """
        self.data = pd.read_csv(self.file_path)
        return self.data

    def get_basic_info(self) -> dict:
        """
        Return basic information about the dataset.
        """
        return {
            "rows": self.data.shape[0],
            "columns": self.data.shape[1],
        }

    def get_columns_info(self) -> dict:
        """
        Analyze the dataset columns and their properties.
        """
        columns_info = {}

        for column in self.data.columns:
            series = self.data[column]

            if is_numeric_dtype(series):
                category = "numerical"
            elif is_bool_dtype(series):
                category = "boolean"
            elif is_datetime64_any_dtype(series):
                category = "datetime"
            else:
                category = "categorical"

            columns_info[column] = {
                "dtype": str(series.dtype),
                "category": category,
                "missing": int(series.isnull().sum()),
                "unique": int(series.nunique()),
            }

        return columns_info

    def get_missing_values(self) -> dict:
        """
        Detect missing values in the dataset.
        """
        missing = self.data.isnull().sum()

        return {
            column: int(value)
            for column, value in missing.items()
            if value > 0
        }

    def get_duplicates(self) -> dict:
        """
        Detect duplicate rows.
        """
        return {
            "duplicate_rows": int(self.data.duplicated().sum())
        }

    def get_numeric_statistics(self) -> dict:
        """
        Return descriptive statistics for numerical columns.
        """
        return get_numeric_statistics(self.data)

    def get_correlation_matrix(self) -> dict:
        """
        Return the correlation matrix.
        """
        return get_correlation_matrix(self.data)

    def get_outliers(self) -> dict:
        """
        Detect outliers using the IQR method.
        """
        return detect_outliers(self.data)

    def get_identifier_columns(self) -> list[str]:
        """
        Detect identifier columns.
        """
        return detect_identifier_columns(self.data)

    def get_constant_columns(self) -> list[str]:
        """
        Detect columns containing only one unique value.
        """
        constant_columns = []

        for column in self.data.columns:
            if self.data[column].nunique() == 1:
                constant_columns.append(column)

        return constant_columns

    def generate_report(self) -> dict:
        """
        Generate a complete profiling report.
        """
        return {
            "basic_info": self.get_basic_info(),
            "columns_info": self.get_columns_info(),
            "missing_values": self.get_missing_values(),
            "duplicates": self.get_duplicates(),
            "numeric_statistics": self.get_numeric_statistics(),
            "constant_columns": self.get_constant_columns(),
            "correlations": self.get_correlation_matrix(),
            "outliers": self.get_outliers(),
            "identifier_columns": self.get_identifier_columns(),
        }