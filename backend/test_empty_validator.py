import pandas as pd

from app.ml.validator import DatasetValidator

data = pd.DataFrame()

validator = DatasetValidator(data)

print(validator.validate())