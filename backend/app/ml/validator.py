import pandas as pd


class DatasetValidator:
    """
    Validate a dataset before preprocessing and model training.
    """

    def __init__(self, dataframe: pd.DataFrame):
        """
        Initialize the validator.

        Args:
            dataframe: Dataset to validate.
        """
        self.data = dataframe


    def validate(self) -> dict:
        """
        Run all validation checks and return a validation report.
        """

        report = {
            "status": "valid",
            "errors": [],
            "warnings": [],
        }

        report["errors"].extend(self.check_empty_dataset())
        report["errors"].extend(self.check_no_columns())
        
        report["warnings"].extend(self.check_empty_columns())
        report["warnings"].extend(self.check_constant_columns())

        if report["errors"]:
            report["status"] = "invalid"

        return report

    def check_empty_dataset(self) -> list[str]:
        """
        Check whether the dataset is empty.
        """
        errors = []

        if self.data.empty:
            errors.append("Dataset is empty.")

        return errors

    def check_no_columns(self) -> list[str]:
        """
        Check whether the dataset contains any columns.
        """
        errors = []

        if self.data.shape[1] == 0:
            errors.append("Dataset contains no columns.")

        return errors

    def check_empty_columns(self) -> list[str]:
        """
        Check for columns containing only missing values.
        """
        warnings = []

        for column in self.data.columns:
            if self.data[column].isnull().all():
                warnings.append(f"Column '{column}' contains only missing values.")

        return warnings


    def check_constant_columns(self) -> list[str]:
        """
        Check for columns containing only one unique value.
        """
        warnings = []

        for column in self.data.columns:
            if self.data[column].nunique() == 1:
                warnings.append(
                    f"Column '{column}' contains only one unique value."
                )

        return warnings
