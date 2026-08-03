import pandas as pd
from app.ml.utils import get_analysis_columns


def get_correlation_matrix(dataframe: pd.DataFrame) -> dict:
    #  Compute the Pearson correlation matrix for numerical columns

    analysis_columns = get_analysis_columns(dataframe)

    numerical_df = dataframe[analysis_columns]

    if numerical_df.shape[1] < 2:
        return {}
    correlation_matrix = numerical_df.corr(method="pearson")
    
    return correlation_matrix.round(3).to_dict()