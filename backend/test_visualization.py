import pandas as pd

from app.ml.visualization import generate_histograms
from app.ml.visualization import generate_boxplots
from app.ml.visualization import generate_correlation_heatmap

data = pd.read_csv(
    "../datasets/iris.csv"
)


files = generate_histograms(data)


print(files)

boxplot_files = generate_boxplots(data)


print(boxplot_files)

heatmap_file = generate_correlation_heatmap(data)   

print(heatmap_file)