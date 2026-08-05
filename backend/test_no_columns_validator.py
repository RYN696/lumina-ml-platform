import pandas as pd

from app.ml.validator import DatasetValidator

data = pd.DataFrame(index=range(5))

validator = DatasetValidator(data)

print(validator.validate())