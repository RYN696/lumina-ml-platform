import pandas as pd

from app.ml.validator import DatasetValidator


data = pd.DataFrame({
    "Name": ["Ali", "Sara", "John"],
    "Age": [20, 25, 30],
    "Country": ["Tunisia", "Tunisia", "Tunisia"],
})

validator = DatasetValidator(data)

print(validator.validate())