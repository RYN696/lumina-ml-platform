import pandas as pd

from app.ml.visualization import generate_histograms


data = pd.read_csv(
    "../datasets/iris.csv"
)


files = generate_histograms(data)


print(files)