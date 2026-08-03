import pandas as pd

def get_correlation_matrix(dataframe: pd.DataFrame) -> dict:
    #  Compute the Pearson correlation matrix for numerical columns
    numerical_df = dataframe.select_dtypes(include="number")

    if numerical_df.shape[1] < 2:
        return {}
    correlation_matrix = numerical_df.corr(method="pearson")
    
    return correlation_matrix.round(3).to_dict()