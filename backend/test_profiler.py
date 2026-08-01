from app.ml.profiler import DatasetProfiler

profiler = DatasetProfiler("../datasets/iris.csv")

profiler.load_dataset()
report = profiler.generate_report()
print(report)