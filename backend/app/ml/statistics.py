import pandas as pd


def get_numeric_statistics(dataframe: pd.DataFrame) -> dict:
    
    # Return descriptive statistics for all numerical columns.

    statistics = {}

    numerical_columns = dataframe.select_dtypes(include="number").columns

    for column in numerical_columns:

        series = dataframe[column]

        statistics[column] = {
            "count": int(series.count()),
            "min": round(float(series.min()), 3),
            "q1": round(float(series.quantile(0.25)), 3),
            "median": round(float(series.median()), 3),
            "q3": round(float(series.quantile(0.75)), 3),
            "max": round(float(series.max()), 3),
            "mean": round(float(series.mean()), 3),
            "variance": round(float(series.var()), 3),
            "std": round(float(series.std()), 3),
        }

    return statistics