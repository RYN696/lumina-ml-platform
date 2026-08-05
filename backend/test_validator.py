from app.ml.profiler import DatasetProfiler
from app.ml.validator import DatasetValidator


profiler = DatasetProfiler("../datasets/iris.csv")

data = profiler.load_dataset()

validator = DatasetValidator(data)

report = validator.validate()

print(report)

