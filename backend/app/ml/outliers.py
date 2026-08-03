import pandas as pd
from app.ml.utils import get_analysis_columns

def detect_outliers(dataframe: pd.DataFrame) -> dict:
    # Detect outliers using the IQR method
    results = {}
    
    numerical_columns = get_analysis_columns(dataframe)
    for column in numerical_columns:
        series = dataframe[column]
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers_count = int(
            ((series < lower_bound) | (series > upper_bound)).sum()
        )
        results[column] = {
            "outliers": outliers_count,
            "lower_bound": round(float(lower_bound), 3),
            "upper_bound": round(float(upper_bound), 3),
        }
    return results

 