import pandas as pd

from app.ml.validator import DatasetValidator

data = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [None, None, None],
    "C": ["x", "y", "z"]
})

validator = DatasetValidator(data)

print(validator.validate())