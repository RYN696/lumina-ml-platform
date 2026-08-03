import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def create_output_directory():
    # create directory for generated plots

    os.makedirs(
        "reports/figures", exist_ok=True
    )

def generate_histograms(dataframe: pd.DataFrame):
    # Generate histograms for numerical columns

    create_output_directory()

    numerical_columns = get_analysis_columns(dataframe)

    generated_files = []

    for column in numerical_columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(dataframe[column], kde=True)
        plt.title(f"Distribution of {column}")
        file_path = (
            f"reports/figures/"
            f"{column}_histogram.png"
        )
        plt.savefig(file_path)
        plt.close()
        generated_files.append(file_path)

    return generated_files