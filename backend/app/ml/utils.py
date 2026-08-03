import pandas as pd


def detect_identifier_columns(
    dataframe: pd.DataFrame
) -> list:
    """
    Detect columns that are likely identifiers.
    """

    identifier_columns = []

    for column in dataframe.columns:

        unique_ratio = (
            dataframe[column].nunique()
            /
            len(dataframe)
        )

        if (
            unique_ratio == 1
            and dataframe[column].dtype != "object"
        ):
            identifier_columns.append(column)


    return identifier_columns


def get_analysis_columns(dataframe: pd.DataFrame):
    """
    Return numerical columns useful for analysis.
    Excludes identifier columns.
    """

    identifier_columns = detect_identifier_columns(dataframe)

    numerical_columns = (
        dataframe
        .select_dtypes(include="number")
        .columns
        .tolist()
    )

    return [
        column
        for column in numerical_columns
        if column not in identifier_columns
    ]